import boto3

s3_resource = boto3.client('s3')

s3_resource.delete_object(Bucket='bucketname', Key='keyname')


import os
import glob

s3_resource.list_objects(Bucket='bucketname')["Contents"]

#iteration
for object in objects:
    print(object['Key'])
    s3_resource.delete_object(Bucket='bucketname', Key=object['Key'])
    
    
        
