import boto3
import manipulate
import aws_key_pair
import aws_on_error
import aws_network
import os

from dotenv import load_dotenv

load_dotenv()
key_path=os.getenv('key_path')
key_name=os.getenv('key_name')
ami_id=os.getenv('ami_id')
instance=os.getenv('instance_type')
region=os.getenv('region')
security=os.getenv('security_name')

def create_n_show ():
    try:
        manipulate.create_ec2_instance(ami_id,instance)
         

    except Exception as e:
        print(e)
        aws_on_error.del_all(key_name,security)
