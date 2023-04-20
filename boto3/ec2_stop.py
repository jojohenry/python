import boto3

ec2_resource=boto3.resource('ec2')


instances=ec2_resource.instances.filter(Filters=[
    {'Name': 'instance-state-name', 'Values': 
        ['running']},{'Name': 'tag:Environment', 'Values': ['Dev']}])
for instance in instances:
    id=instance.id
    ec2_resource.instances.filter(InstanceIds=[id]).stop()
    print("Stopped instance with id " + id)



