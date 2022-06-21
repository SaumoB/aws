key="ki"
public_dns="ser"
region="sda"
s=f'ssh -i "{key}" ec2-user@{public_dns}.{region}.compute.amazonaws.com'
print(s)