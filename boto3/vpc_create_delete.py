import boto3

client = boto3.client('ec2')


response = client.create_vpc(CidrBlock='10.0.0.0/16')
    
print(response)
    
#delete vpc
response = client.delete_vpc(VpcId='VPC-ID HERE')
