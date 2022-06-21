import paramiko
import time
import traceback

key = paramiko.RSAKey.from_private_key_file("/home/cbnits/aws_python/keys/mount.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
cmd = "pwd"

# Connect/ssh to an instance
try:
    # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
    client.connect(hostname="ec2-3-108-228-36.ap-south-1.compute.amazonaws.com", username="ec2-user", pkey=key)
    print("Connection part is done!")
    # Execute a command(cmd) after connecting/ssh to an instance
    stdin, stdout, stderr = client.exec_command(cmd)
    time.sleep(5)
    print(stdout.read())

    # close the client connection once the job is done
    client.close()
    #exit(0)

except Exception as e:
    #print(traceback.print_exc)
    print(e)

