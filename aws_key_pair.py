import boto3
#from dotenv import load_dotenv
import os

#key_path=config["key_path"]
#key_name=config["key_name"]

#class Key():
def create_keypair(key,key_path):
    try:
        client=boto3.client("ec2")
        key_pair=client.create_key_pair(KeyName=key)
        private_key=key_pair["KeyMaterial"]
        with os.fdopen(os.open(key_path,os.O_WRONLY|os.O_CREAT,0o400),"w+") as handle:
            handle.write(private_key)
    except Exception as e:
        print (e)

