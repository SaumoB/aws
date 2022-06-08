# Lets create EC2 instances using Python BOTO3
import boto3


def create_ec2_instance():
    try:
        print ("Creating EC2 instance")
        resource = boto3.client("ec2")
        resource.run_instances(
            ImageId="ami-079b5e5b3971bd10d",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
        )
    except Exception as e:
        print(e)


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


def stop_ec2_instance():
    try:
        print ("Stop EC2 instance")
        instance_id = describe_ec2_instance()
        resource = boto3.client("ec2")
        print(resource.stop_instances(InstanceIds=[instance_id]))
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