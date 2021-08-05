from pprint import pprint
import boto3
from decimal import Decimal
from backend.dynamodb import get_dynamodb


def format_data_to_write(urls_to_amounts):
	rtn = []
	s = 0
	for url, decimal in urls_to_amounts.items():
		rtn.append([url, Decimal(str(decimal))])
		s += decimal
	assert abs(decimal - 1) < .00001, "must be close to 1"
	return rtn


def put_route(link_route, urls_to_amounts):
	dynamodb = get_dynamodb()
	table = dynamodb.Table('URLMapping')
	response = table.put_item(
		Item={
			'link_route': 'facebook',
			'urls': format_data_to_write(urls_to_amounts)
		}
	)
	return response

