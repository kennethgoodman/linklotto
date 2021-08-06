from pprint import pprint
from decimal import Decimal
from backend.dynamodb import get_dynamodb


def put_route(link_route, urls_to_amounts, title):
	assert abs(sum(urls_to_amounts.values()) - 1) < .00001, f'must be close to 1, is actually {sum(urls_to_amounts.values)}'
	dynamodb = get_dynamodb()
	table = dynamodb.Table('URLMapping')
	# TODO that nothing exists on this key yet
	response = table.put_item(
		Item={
			'link_route': link_route,
			'title': title,
			'urls': list(urls_to_amounts.keys()),
			'weights': list(map(lambda x: Decimal(str(x)), urls_to_amounts.values()))
		}
	)
	return response

