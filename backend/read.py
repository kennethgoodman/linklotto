from backend.dynamodb import get_dynamodb


def _get_if_exist(link_route, table):
	try:
		item = table.get_item(Key={'link_route': link_route})
	except boto.dynamodb.exceptions.DynamoDBKeyNotFoundError:
		item = None
	return item

def does_exist(link_route):
	dynamodb = get_dynamodb()
	table = dynamodb.Table('URLMapping')
	return _get_if_exist(link_route, table) is not None


def get_route(link_route):
	dynamodb = get_dynamodb()
	table = dynamodb.Table('URLMapping')
	try:
		response = _get_if_exist()
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		return response

if __name__ == '__main__':
	print(get_route('facebook'))