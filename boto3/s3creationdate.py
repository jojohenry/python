import boto3

s3_resource = boto3.client('s3')

s3_resource.list_buckets()

creation_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]

#use the created creation date variable to output creation date of specific buckets.
for bucket in s3_resource.list_buckets()['Buckets']:
    print(bucket)
    
