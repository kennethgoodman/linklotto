from pprint import pprint
from decimal import Decimal
from backend.dynamodb import get_dynamodb


def format_data_to_write(urls_to_amounts):
	rtn = []
	s = 0
	for url, decimal in urls_to_amounts.items():
		rtn.append([url, Decimal(str(decimal))])
		s += decimal
	assert abs(s - 1) < .00001, f'must be close to 1 is actually {s}'
	return rtn


def put_route(link_route, urls_to_amounts):
	assert abs(sum(urls_to_amounts.values) - 1) < .00001, f'must be close to 1, is actually {sum(urls_to_amounts.values)}'
	dynamodb = get_dynamodb()
	table = dynamodb.Table('URLMapping')
	response = table.put_item(
		Item={
			'link_route': link_route,
			'urls': list(urls_to_amounts.keys())
			'weights': list(urls_to_amounts.values())
		}
	)
	return response

