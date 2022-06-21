import argparse
import subprocess

print("WELCOME")

parser = argparse.ArgumentParser()
parser.add_argument('--opt',type=int)

args = parser.parse_args()

if not args.opt:
    opt=input("\n1.Ec2\n2.S3\n\nENTER YOUR CHOICE :",)
    opt=int(opt)
else: 
    print("\n\nYou Chose 2: S3")
    opt=args.opt

def ec2():subprocess.call(['python3','/home/cbnits/aws_python/ec2/run.py'])
    
def s3():subprocess.call(['python3','/home/cbnits/aws_python/s3/run.py'])
    
def default():print("\nWRONG OPTION")

switcher={
		1:ec2,
		2:s3,
	}
def switch(x):
  	return switcher.get(x,default)()
switch(opt)