import boto3

client=boto3.client('ec2')

response=client.describe_vpcs()

print(response)

#how to view all vpcs in account
