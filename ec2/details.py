import boto3
from datetime import datetime,timezone,timedelta

now=datetime.now(timezone.utc)
ec2 = boto3.client('ec2')
reservations = ec2.describe_instances().get("Reservations")
for reservation in reservations:
    for instance in reservation["Instances"]:
        launch=instance["LaunchTime"]
        for tag in instance["Tags"]:
            if tag['Key']=='Name': name = tag['Value']
        # if (instance["State"]["Name"])!="running":
        #    stop=

        print("\nVM:",name," is running for:",(now-launch).days,"days\n")