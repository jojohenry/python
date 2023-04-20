import boto3

#list all ec2 instances running

ec2_client=boto3.client('ec2')

response=ec2_client.describe_instances()

#print(response)

data=response['Reservations'][0] ####Reservation is name of dictionary holding ec2 info
data_instance=data['Instances']#Instances is the key
for i in range (len(data_instance)):
    print(f"instance id is {data_instance[i]['InstanceId']}")#instanceId is the value
