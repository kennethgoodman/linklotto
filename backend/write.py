from decimal import Decimal
from backend.dynamodb import get_dynamodb
from botocore.exceptions import ClientError

def put_route(link_route, urls_to_amounts, title):
	assert abs(sum(urls_to_amounts.values()) - 1) < .00001, f'must be close to 1, is actually {sum(urls_to_amounts.values)}'
	dynamodb = get_dynamodb()
	table = dynamodb.Table('URLMapping')
	try:
		response = table.put_item(
			Item={
				'link_route': link_route,
				'title': title,
				'urls': list(urls_to_amounts.keys()),
				'weights': list(map(lambda x: Decimal(str(x)), urls_to_amounts.values()))
			},
			ConditionExpression='attribute_not_exists(link_route)' # must not exist
		)
	except ClientError as ce:
		if ce.response['Error']['Code']=='ConditionalCheckFailedException': 
			# TODO: check if anybody has retrieved in more than 100 days, if no overwrite
			raise ValueError("does exist already") # TODO convert to custom exception
		raise ce
	return response

