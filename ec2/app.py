import boto3
import manipulate
import aws_key_pair
import aws_on_error
import aws_network
import argparse
import modify
import aws_security_group
import os
from dotenv import load_dotenv

################### Parameters #########################
load_dotenv()

key_path=os.getenv('key_path')
#key_name=os.getenv('key_name')
ami_id=str(os.getenv('ami_id'))
instance=str(os.getenv('instance_type'))
region=str(os.getenv('region'))
security=str(os.getenv('security_name'))
az=str(os.getenv('availability_zone'))
cidr=str(os.getenv('cidr'))
ip=os.getenv('ip')

################### Key Creation #####################

################### create Instance ####################
'''
def create_instance(ami_id,instance,region,subnet,key_name,name,security):
    try:
        instance_id=
        return instance_id 
    except Exception as e:
        print(e)
        aws_on_error.del_all(key_name,security,subnet)
'''
##################### Create Security ####################

def create_security():
    try:
        security_id=aws_security_group.create_security(security)
    except Exception as e:
        print (e)
        aws_on_error.del_security(security_id)

##################### Assign Security ####################

def assign_security(security_id,instance_id):
    try:
        client=boto3.client("ec2")
        instance =client.Instance(instance_id)

        instance.modify_attribute(
            Groups=[
                security_id
            ]
        )

    except Exception as e:
        print (e)

####################### Custom Network ####################

####################### Assign Subnet #####################

def assign_subnet(instance_id,id):
    try:
        client=boto3.client("ec2")
        instance =client.Instance(instance_id)

        instance.modify_attribute(
            SubnetId=id
        )
    except Exception as e:
        print (e)
####################### MODIFY #############################

def modify_inst(id,type,disk,region):
    if not id:
        print("Enter id to modify")
        exit()
    modify.modify(region,id,disk,type)

########################## MAIN ###########################

if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--disk')
    parser.add_argument('--type')
    parser.add_argument('--modify')
    parser.add_argument('--core')
    args = parser.parse_args()
    print (args.name,args.core,args.modify,args.disk,args.type)

    if args.modify:
        if not args.type:
            modify_inst(args.modify,instance,args.disk,region)
            exit()
        else:modify_inst(args.modify,args.type,args.disk,region)

    if not args.name or not args.disk or not args.core:
        print("\nUSAGE ERROR : --name <name_of_instance> --disk <storage_of_instance_in_GB> --core <number_of_core>\n\t\t[optional: --type <disk_type>]")
        print("\nTO modify an Instance : --modify <Instance-id> --disk <additional_storage>\n\t\t[optional: --type <disk_type>]")
        exit()

    aws_key_pair.create_keypair(args.name,key_path)
    vpc=aws_network.create_custom_vpc(ip)
    subnet=aws_network.create_custom_subnet(str(az),str(vpc.id),str(cidr))
    if not args.type:
        inst=manipulate.create_ec2_instance(ami_id,instance,region,vpc.id,subnet.id,args.name,args.name,security,int(args.disk),int(args.core))
    else:
        inst=manipulate.create_ec2_instance(ami_id,args.type,region,vpc.id,subnet.id,args.name,args.name,security,int(args.disk),int(args.core))


########################---------END-OF-CODE----------#############################    
