from backend.dynamodb import get_dynamodb


def get_route(link_route):
	dynamodb = get_dynamodb()
	table = dynamodb.Table('URLMapping')
	try:
		response = table.get_item(Key={'link_route': link_route})
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		return response

if __name__ == '__main__':
	print(get_route('facebook'))