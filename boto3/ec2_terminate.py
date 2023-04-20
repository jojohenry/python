import boto3

ec2_client=boto3.client('ec2')

response=ec2_client.describe_instances()

print(len(response['Reservations']))

#############################

data=response['Reservations']

ec2_list=[]
for instances in data:
    instance=instances['Instances']
    for ids in instance:
        instance_id=ids['InstanceId']
        print(instance_id)
        ec2_list.append(instance_id)
        
#####ec2_client.terminate_instances(InstanceIds=ec2_list)#####        
