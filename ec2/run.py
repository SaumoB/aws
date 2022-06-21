import subprocess

print("hello")

o=input("\n1.To create an instance of your Input name in Mumbai\n2.To show the uptime of your aws instances of a region\n\nENTER YOUR CHOICE: \t")
o=int(o)

def app():
	name=input("\n\nEnter instance name:")
	subprocess.call(['python3','/home/cbnits/aws_python/ec2/app.py','--name',name])

def details():
	region=input("\n\nEnter Region code [example:ap-south-1]:")
	subprocess.call(['python3','/home/cbnits/aws_python/ec2/details.py','','--region ',region])


def default():print("\nWRONG OPTION")

switcher={
		1:app,
		2:details,
	}
def switch(y):
  	return switcher.get(y,default)()
switch(o)