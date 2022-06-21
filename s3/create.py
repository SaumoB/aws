import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name')

args = parser.parse_args()
try:
    print("\n Creating Bucket \n")
    s3=boto3.client('s3',region_name="us-east-1")
    s3.create_bucket(Bucket=args.name)
    print("\n Bucket Created \n")
except Exception as e:
    print(e)