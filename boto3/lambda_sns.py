import json
import boto3

def lambda_handler(event, context):
    # Get the SQS message
    message = json.loads(event['Records'][0]['body'])

    # Get the SNS client
    sns = boto3.client('sns')

    # Send the message to the SNS topic
    response = sns.publish(
        TopicArn='',
        Message=json.dumps(message)
    )

    return response
