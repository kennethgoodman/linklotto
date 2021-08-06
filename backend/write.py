from pprint import pprint
from decimal import Decimal
from backend.dynamodb import get_dynamodb
from backend.read import does_exist



def put_route(link_route, urls_to_amounts, title):
	assert abs(sum(urls_to_amounts.values()) - 1) < .00001, f'must be close to 1, is actually {sum(urls_to_amounts.values)}'
	dynamodb = get_dynamodb()
	table = dynamodb.Table('URLMapping')
	if not does_exist(link_route): # TODO: check if anybody has retrieved in more than 100 days, if no overwrite
		return ValueError("does exist already") # TODO convert to custom exception
	response = table.put_item(
		Item={
			'link_route': link_route,
			'title': title,
			'urls': list(urls_to_amounts.keys()),
			'weights': list(map(lambda x: Decimal(str(x)), urls_to_amounts.values()))
		}
	)
	return response

