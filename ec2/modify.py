import resource
import time
import boto3
import manipulate as man
#import subprocess
import paramiko

def modify(region,id,disk,type,key):
 try:    
    man.stop_ec2_instance(id)
    time.sleep(7)
    ec2=boto3.client("ec2",region_name=region)
    print("\nStarting Modification")
    disk=int(disk)

    print("\n\tModifying Instance Type")
    ec2.modify_instance_attribute(
        InstanceId=id,
        InstanceType={'Value':type},
        )

    print("\n\tCreating Volume")
    response=ec2.create_volume(
    AvailabilityZone='ap-south-1a',
    Size=disk,
    VolumeType='gp2',
        )
    print ("\n",response)
    vol_id=response['VolumeId']
    time.sleep(5)

    print("\n\nAttaching Volume to Instance")
    ec2.attach_volume(
        Device= '/dev/xvdb',
        InstanceId=id,
        VolumeId=vol_id
    )
    mount(key)
    print("\nModification Succesful")
    exit()
 except Exception as e:
    print("\nModification Unsuccesful")
    print(e)
    ec2_resource = boto3.resource('ec2', region_name=region)
    volume = ec2_resource.Volume(vol_id)
    volume.delete()
    print(f'\nVolume successfully deleted')
    exit()

#####################__MOUNTING_############################
'''
#!/bash
sudo mkdir /newvolume
sudo mkfs -t ext4 /dev/xvdb
sudo mount /dev/xvdb /newvolume/
'''

def mount(user,public_dns,key_path,vol_path):
    print("\n\n\t\t\t___Starting To Mount____")
#    subprocess.call([f'sudo cd {key_path}'])
 #   subprocess.call([f'ssh -i "{key}" {user}@{public_dns}'])
 #   time.sleep(5)
 #   subprocess.call(['yes'])
#    exit()
#    subprocess.call(['sudo mkfs -t ext4 /dev/xvdb','sudo mkdir /newvolume',])
#    time.sleep(2)
#    subprocess.call(['sudo mount /dev/xvdf /newvolume/'])

    key = paramiko.RSAKey.from_private_key_file(key_path)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cmd = f"sudo mkdir /newvolume\nsudo mkfs -t ext4 {vol_path}"

    # Connect/ssh to an instance
    try:
        # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
        client.connect(hostname=public_dns, username=user, pkey=key)
        print("Connection established!")
        # Execute a command(cmd) after connecting/ssh to an instance

        stdin, stdout, stderr = client.exec_command(cmd)
        time.sleep(5)
        print(stdout.readline())
        time.sleep(5)
        stdin,stdout,stderr=client.exec_command(f"sudo mount {vol_path} /newvolume/")

        print(stdout.readline())

        # close the client connection once the job is done
        client.close()
        #exit(0)

    except Exception as e:
        #print(traceback.print_exc)
        print(e)



    print("\n\t\t____Mounting_Complete____")

########################## TesT ######################################

########################## Unmount ##################################

def unmount(user,public_dns,key_path,vol_path):
    print("\n\n\t\t\t___Starting To unmount____")

    key = paramiko.RSAKey.from_private_key_file(key_path)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cmd = f"umount -d {vol_path}"

    # Connect/ssh to an instance
    try:
        client.connect(hostname=public_dns, username=user, pkey=key)
        print("Connection established!")

        stdin, stdout, stderr = client.exec_command("cp -RT /newvolume /home/ec-2user/vol_backup")
        stdin, stdout, stderr = client.exec_command(cmd)
        time.sleep(5)
        print(stdout.read())

        # close the client connection once the job is done
        client.close()
        #exit(0)

    except Exception as e:
        #print(traceback.print_exc)
        print(e)
    print("\n\t\t____Unmounting_Complete____")

########################## detach ############################

def detach(vol,inst,):
     try:
        resource=boto3.resource(inst)
        client=boto3.client(inst)
        volume = resource.Volume()
        volume.detach_from_instance(InstanceId=inst, Force=True)
        waiter = client.get_waiter('volume_available')
        waiter.wait(VolumeIds=[vol],)
        print (" INFO : Volume Detached")
        i=input ("\nType: 1 Delete volume \n\n Anything else to Exit ")
        if i==1:
        # Deleting Volume Device details already available
         volume.delete()
         print (" INFO : Volume Deleted")

     except Exception as ERR:
        print(ERR)
        exit()




#if __name__=='__main__':
#    mount("ec2-user","ec2-65-0-205-199.ap-south-1.compute.amazonaws.com","/home/cbnits/aws_python/keys/mount.pem","/dev/sdf")
#    detach("vol-09b5fd112ee84206e","i-077d2d07d5028719f")