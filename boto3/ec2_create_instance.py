import boto3

ec2 = boto3.resource('ec2')

#starting 3 instances for purpose of project
#ami is Amazon Linux, left out SSH key 
instances = ec2.create_instances(
    ImageId='ami-0b5eea76982371e91',
    MinCount=3,
    MaxCount=3,
    InstanceType='t2.micro')
    
