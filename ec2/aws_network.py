import boto3
from botocore.exceptions import ClientError
#import json

def create_custom_vpc(ip_cidr):
    """
    Creates a custom VPC with the specified configuration.
    """
    try:

        resource=boto3.resource('ec2')
        print("creating VPC.....")
        response = resource.create_vpc(CidrBlock=ip_cidr,
                                           InstanceTenancy='default',
                                           TagSpecifications=[{
                                               'ResourceType':
                                               'vpc',
                                               'Tags': [{
                                                   'Key':
                                                   'Name',
                                                   'Value':
                                                   'test_vpc'
                                               }]
                                           }])
        print("\n\n VPC CREATED")
    except ClientError:
        print('Could not create a custom vpc.')
        raise
    else:
        return response


def create_custom_subnet(az, vpc_id, cidr_block):
    vpc_resource = boto3.resource("ec2")
    try:
        print("Creating Subnet......")
        response = vpc_resource.create_subnet(TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [{
                    'Key': 'Name',
                    'Value': 'Test_Subnet'
                }]
            },
        ],
                                              AvailabilityZone=az,
                                              VpcId=vpc_id,
                                              CidrBlock=cidr_block)

        print("\n\n Subnet Created .")
    except ClientError:
        print('Could not create a custom subnet.')
        raise
    else:
        return response


'''
def create_default_subnet(az):
    try:
        vpc_client=boto3.client('ec2')
        response = vpc_client.create_default_subnet(AvailabilityZone=az)

    except ClientError:
        print('Could not create default subnet.')
        raise
    else:
        return response



if __name__ == '__main__':
    # Constants
    CIDR_BLOCK = '192.168.1.0/20'
    VPC_ID = 'vpc-048604f523ad01d74'
    AZ = 'ap-south-1a'
   
    print('Creating a custom Subnet...')
    custom_subnet = create_custom_subnet(AZ, VPC_ID, CIDR_BLOCK)
    print('Custom Subnet is created with Subnet ID: {custom_subnet.id}')
'''