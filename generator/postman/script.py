import os


def get_script(broker: bool) -> str:

    sdk_version = os.getenv("SDK_VERSION", '')

    file_name = 'script_template.js'
    if broker:
        file_name = 'script_broker_template.js'

    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.replace('{{SDK-VERSION}}', sdk_version)
        return content