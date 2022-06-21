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
    print("\nDeleting key\n")
    response = ec2.delete_key_pair(KeyName=key)
    print(response)
    print("\nkey Deleted\n")

def del_subnet(subnet):
        print("\ndeleting Subnet\n")
        response = ec2.delete_subnet(SubnetId=subnet)
        print(response)
        print("\nSubnet Deleted\n")

def del_vpc(vpc):
    print("\ndeleting VPC\n")
    response=ec2.delete_vpc(VpcId=vpc)
    print(response)
    print("\nVPC Deleted\n")

def del_all(key,security,vpc,subnet):
#    del_security(security)
    del_key(key)
    del_subnet(subnet)
    del_vpc(vpc)