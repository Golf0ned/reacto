import yaml


emojis_file = "emojis.yaml"
secrets_file = "secrets.yaml"

class Config:

    with open(emojis_file, 'r') as file:
        emojis = yaml.safe_load(file)

    with open(secrets_file, 'r') as file:
        secrets = yaml.safe_load(file)
