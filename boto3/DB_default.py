import boto3

# Create a boto3 client for DynamoDB
dynamodb = boto3.client('dynamodb')

# Define the table schema
table_schema = {
    'Attribute_definitions': [
        {
            'attribute_name': 'id',
            'attribute_type': 'S'
        },
    ],
    'key_schema': [
        {
            'attribute_name': 'id',
            'key_type': 'HASH'
        },
    ],
    'provisioned_throughput': {
        'read_capacity_units': 5,
        'write_capacity_units': 5
    },
    'table_name': 'mytable'
}

# Create the table
dynamodb.create_table(**table_schema)
