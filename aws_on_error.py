import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
def del_security(security):
    try:
        response = ec2.delete_security_group(GroupId=security)
        print('Security Group Deleted')
    except ClientError as e:
        print(e)

def del_key(key):
    response = ec2.delete_key_pair(KeyName=key)
    print(response)

def del_all(key,security):
    del_security(security)
    del_key(key)