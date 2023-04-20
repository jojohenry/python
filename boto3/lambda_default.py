import boto3

# Create a boto3 client for Lambda
lambda_client = boto3.client('lambda')

# Define the function
function_name = "myfunction"
runtime = "python3.8"
role = "arn:aws:iam::1234567890:role/lambda_basic_execution"
handler = "lambda_function.lambda_handler"
zip_file = open("lambda_function.zip", "rb")

# Create the function
lambda_client.create_function(
    FunctionName=function_name,
    Runtime=runtime,
    Role=role,
    Handler=handler,
    Code={'ZipFile': zip_file.read()}
)
