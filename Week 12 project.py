#Create a list of services using python.IE: S3, Lambda, EC2, etc.
#The list should be empty initially.

aws_items = []

#Populate the list using append or insert.

aws_items.append('S3')
aws_items.append('Lambda')
aws_items.append('EC2')
aws_items.append('DynamoDB')
aws_items.append('CloudWatch')
aws_items.append('IAM')

#Print the list

print(aws_items)

#Print the length of the list
print(len(aws_items))

#Remove two specific services from the list by name or by index.
del aws_items[1]
del aws_items[2]

#Print the new list.
print(aws_items)

#Print the new length of the list.
print(len(aws_items))