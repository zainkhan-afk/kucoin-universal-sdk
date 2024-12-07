import json
import sys

from api_meta import ApiMetaUtil


class WsSchema:
    def __init__(self, name: str, schema: dict, attr: dict):
        self.name = name
        self.schema = schema
        self.attr = attr


class WsService:
    def __init__(self, name: str):
        self.name = name
        self.public = {}
        self.private = {}

    def add_schema(self, schema: WsSchema, is_public: bool):
        if is_public:
            self.public[schema.name] = schema
        else:
            self.private[schema.name] = schema


class WsMetaUtil:

    @staticmethod
    def parse_description(sch):
        if "description" not in sch or sch['description'] == "" or sch['description'].strip() == "":
            raise Exception(f"no description found in schema {sch['name']}")

        desc_content = sch['description'].strip()
        lines = desc_content.split("\n")
        if len(lines) < 2:
            raise Exception(f"description format not ok {sch['name']}")

        attr = {}
        for line in lines:
            for prefix in ['method:', 'topic:', 'summary:', 'description:', 'push_frequency:']:
                if line.startswith(prefix):
                    attr[prefix[:-1]] = line.replace(prefix, "").strip()

        return attr

    @staticmethod
    def parse(file_path):
        try:
            with open(file_path, "r") as file:
                file_content = file.read()
            json_content = json.loads(file_content)

            service_map = {}

            for collection in json_content['schemaCollection']:
                if collection['name'] == 'Root' or collection['name'] == '根目录':
                    for root in collection['items']:
                        if root['name'] == 'ws':
                            for ws in root['items']:

                                service_name = ws['name']
                                if service_name not in service_map:
                                    service_map[service_name] = WsService(name=service_name)

                                ws_service = service_map[service_name]

                                for channels in ws['items']:
                                    for ws_schema in channels['items']:
                                        attr = WsMetaUtil.parse_description(ws_schema)
                                        ws_service.add_schema(
                                            WsSchema(ws_schema['name'], ws_schema, attr),
                                            channels['name'] == 'Public')
            return service_map


        except Exception as e:
            print(f"An error occurred when read meta file: {e}")
            sys.exit(1)

    @staticmethod
    def generate_response(channel, paths, schemas, service, private):

        for schema_name in channel:
            schema = channel[schema_name]
            method = schema.attr.get('method')
            topic = schema.attr.get('topic')
            if method is None or topic is None:
                raise Exception('no method or topic found in attr, name= ' + schema_name)

            sub_service = "private" if private == True else "public"
            sub_service = f'{service.lower()}_{sub_service.lower()}'
            schema_ref_name = f"{service}-{sub_service}-{schema_name}"
            schema_ref_name = schema_ref_name.replace("/", "_")
            schema_ref_name = schema_ref_name.replace("-", "_")

            path_name = '/' + method + topic.replace('{', '_').replace('}', '_')

            original_schema = schema.schema["schema"]["jsonSchema"]
            example = original_schema['x-example'] if 'x-example' in original_schema else ''
            example = example.replace('"', '\\"')
            path = {
                "trace": {
                    "summary": schema.attr.get('summary'),
                    "deprecated": "false",
                    "description": schema.attr.get('description'),
                    "tags": [],
                    "parameters": [],
                    "x-sdk-service": service,
                    "x-sdk-sub-service": sub_service,
                    "x-sdk-private": private,
                    "x-sdk-method-name": method,
                    "x-topic": topic,
                    "x-push_frequency": schema.attr.get('push_frequency'),
                    'x-response-example': example,
                    "responses": {
                        "200": {
                            "description": "",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": f"#/components/schemas/{schema_ref_name}"
                                    }
                                }
                            }
                        }
                    }}}

            if 'x-example' in original_schema:
                del original_schema['x-example']

            paths[path_name] = path
            schemas[schema_ref_name] = schema.schema["schema"]["jsonSchema"]

            ApiMetaUtil.update_schema(schemas[schema_ref_name])

    @staticmethod
    def generator_ws_openapi(service_name, ws_service):
        paths_public = {}
        schemas_public = {}

        WsMetaUtil.generate_response(ws_service.public, paths_public, schemas_public, service_name, False)

        openapi_public = {
            "openapi": "3.0.1",
            "info": {
                "title": service_name.lower(),
                "description": f"{service_name.lower()}_public",
                "version": "1.0.0"
            },
            "tags": [],
            "paths": paths_public,
            "components": {
                "schemas": schemas_public
            }
        }

        paths_private = {}
        schemas_private = {}
        WsMetaUtil.generate_response(ws_service.private, paths_private, schemas_private, service_name, True)

        openapi_private = {
            "openapi": "3.0.1",
            "info": {
                "title": service_name.lower(),
                "description": f"{service_name.lower()}_private",
                "version": "1.0.0"
            },
            "tags": [],
            "paths": paths_private,
            "components": {
                "schemas": schemas_private
            }
        }
        return [('private', openapi_private), ('public', openapi_public)]

    @staticmethod
    def write(out_path, openapi):
        try:
            with open(out_path, 'w', encoding='utf-8') as file:
                json.dump(openapi, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"An error occurred when generate ws specification file: {e}")
            sys.exit(1)
