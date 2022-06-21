import subprocess

#print("hello")

o=input("\n1.To create a Bucket\n2.To show the buckets\n\nENTER YOUR CHOICE: \t")
o=int(o)

def create():
	name=input("\n\nEnter bucket name:")
	subprocess.call(['python3','/home/cbnits/aws_python/s3/create.py','--name',name])

def show():
	#region=input("\n\nEnter Region code [example:ap-south-1]:")
	subprocess.call(['python3','/home/cbnits/aws_python/s3/show.py',])

def default():print("\nWRONG OPTION")

switcher={
		1:create,
		2:show,
	}
def switch(y):
  	return switcher.get(y,default)()
switch(o)