import boto3
#from dotenv import load_dotenv
import os

#key_path=config["key_path"]
#key_name=config["key_name"]

#class Key():
def create_keypair(key,key_path):
    try:
        print("CREATiNG A KEY")
        client=boto3.resource("ec2")
        key_pair=client.create_key_pair(KeyName=key)
        fullname=key+".pem"
        with open(str(key_path+fullname), 'w') as file:
            file.write(key_pair.key_material)
        print("Key CREATED")
    except Exception as e:
        print ("Key already Exist")
        print(e)