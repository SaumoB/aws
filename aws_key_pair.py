import boto3
import os
import json
import json_operations

config=json_operations.loadJsonData("./config.json")
key_path=config["key_path"]
key_name=config["key_name"]


client=boto3.client("ec2")
class Key():
    def create_keypair():
        key_pair=client.create_key_pair(KeyName=key_name)
        private_key=key_pair["KeyMaterial"]
        with os.fdopen(os.open(key_path,os.O_WRONLY|os.O_CREAT,0o400),"w+") as handle:
            handle.write(private_key)

