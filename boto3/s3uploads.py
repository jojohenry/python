import boto3
import os
import glob

s3_resource = boto3.client('s3')

#how to upload single file to s3
    
s3_resource.upload_file(
    Filename='test.txt',
    Bucket='mybucket-boto3',
    Key='test.txt')
    
#see working directory
cwd = os.cwd()
cwd = cwd + '/upload/'

#upload multiple files to s3

#see files in working directory
files = glob.glob(cwd + '*.png')
print(files)

for file in files:
    s3_resource = boto3.resource('s3')
    s3_resource.upload_file(
    Filename='test',
    Bucket='mybucket-boto3',
    Key='test')    
