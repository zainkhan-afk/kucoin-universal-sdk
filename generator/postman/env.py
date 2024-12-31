import json
import sys

from costant import outputPath


class Env:
    def gen_env(self):
        values = [
            {
                "key": "spot_endpoint",
                "value": "api.kucoin.com",
                "type": "default",
                "enable": True,
            },
            {
                "key": "futures_endpoint",
                "value": "api-futures.kucoin.com",
                "type": "default",
                "enable": True,
            },
            {
                "key": "broker_endpoint",
                "value": "api-broker.kucoin.com",
                "type": "default",
                "enable": True,
            },
            {
                "key": "API_KEY",
                "value": "",
                "type": "secret",
                "enabled": True
            },
            {
                "key": "API_SECRET",
                "value": "",
                "type": "secret",
                "enabled": True
            },
            {
                "key": "API_PASSPHRASE",
                "value": "",
                "type": "secret",
                "enabled": True
            }
            ,
            {
                "key": "BROKER_NAME",
                "value": "",
                "type": "secret",
                "enabled": True
            }
            ,
            {
                "key": "BROKER_PARTNER",
                "value": "",
                "type": "secret",
                "enabled": True
            }
            ,
            {
                "key": "BROKER_KEY",
                "value": "",
                "type": "secret",
                "enabled": True
            }
        ]

        env_obj = {
            "id": "0deee4de-080a-4246-a95d-3eee14126248",
            "name": "KuCoin API Production",
            "values": values,
            "_postman_variable_scope": "environment",
        }
        return env_obj

    def write_env(self, env_obj):
        try:
            out_path = f"{outputPath}/env.json"
            with open(out_path, 'w', encoding='utf-8') as file:
                json.dump(env_obj, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"An error occurred when generate postman env file: {e}")
            sys.exit(1)

    def generate(self):
        env_obj = self.gen_env()
        self.write_env(env_obj)
