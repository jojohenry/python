import boto3

#creating an S3 bucket, public access

aws_resource = boto3.resource('s3')
bucket = aws_resource.Bucket('bucketname')

response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
   
)
print(response)
