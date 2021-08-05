import boto3
dynamodb = None

def get_aws_credentials():
	with open('aws.credentials.csv', 'r') as f:
		aws_access_key_id = f.readline().split("=")[1].strip()
		aws_secret_access_key = f.readline().split("=")[1].strip()
	return (aws_access_key_id, aws_secret_access_key)

def get_dynamodb():
	global dynamodb
	if not dynamodb:
		aws_access_key_id, aws_secret_access_key = get_aws_credentials()
		dynamodb = boto3.resource('dynamodb', 
								region_name='us-east-2',
								aws_access_key_id=aws_access_key_id,
								aws_secret_access_key=aws_secret_access_key,
		)
	return dynamodb
