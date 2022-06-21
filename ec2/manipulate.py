# Lets create EC2 instances using Python BOTO3
import boto3
import aws_on_error
def create_ec2_instance(img_id,instance,region,vpc,subnet,key_pair,name,security,disk,core):
    try:
        print ("\nCreating EC2 instance\n")
        print(region)
        while (disk<8):
                        print
                        disk=input("\nEnter required disk size [Standard = 8]:\t")
                        disk=int(disk)
        while (core<1):
                        print
                        core=input("\nEnter at least 1 core")
                        core=int(core)

        resource = boto3.resource("ec2",region_name=region)
        insts=resource.create_instances(
            ImageId=img_id,
            MinCount=1,
            MaxCount=1,
            InstanceType=instance,
            #SecurityGroups=[security,],
            KeyName=key_pair,
            SubnetId=subnet,
            BlockDeviceMappings=[
                                    { 
                                    "DeviceName": "/dev/xvda",
                                    "Ebs" : { "VolumeSize" : disk }
                                    }
                                ],
            TagSpecifications=
                [
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value':name
                            },
                        ]
                    },
                ],
          #  CpuOptions=
           #             {
            #            'CoreCount': core,
            #           'ThreadsPerCore': 1
            #            },
                        )
        print("\n\tCreated\n")
        for inst in insts :
            return inst.id
    except Exception as e:
        print(e)
        aws_on_error.del_all(key_pair,security,vpc,subnet)

def describe_ec2_instance():
    try:
        print ("Describing EC2 instance")
        resource = boto3.client("ec2")
        print(resource.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)


def reboot_ec2_instance():
    try:
        print ("Reboot EC2 instance")
        instance_id = describe_ec2_instance()
        resource = boto3.client("ec2")
        print(resource.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def stop_ec2_instance(id):
    try:
        print ("Stop EC2 instance")
        resource = boto3.client("ec2")
        print(resource.stop_instances(InstanceIds=[id]))
    except Exception as e:
        print(e)


def start_ec2_instance():
    try:
        print ("Start EC2 instance")
        instance_id = describe_ec2_instance()
        resource = boto3.client("ec2")
        print(resource.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


def terminate_ec2_instance():
    try:
        print ("Terminate EC2 instance")
        instance_id = describe_ec2_instance()
        resource = boto3.client("ec2")
        print(resource.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)


#create_ec2_instance()
#describe_ec2_instance()
#reboot_ec2_instance()
#stop_ec2_instance()
#start_ec2_instance()
#terminate_ec2_instance()