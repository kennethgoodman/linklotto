from pprint import pprint
import boto3
from decimal import Decimal
from dynamodb import get_dynamodb


def put_route(link_route, *, dynamodb=None):
    dynamodb = get_dynamodb()
    table = dynamodb.Table('URLMapping')
	response = table.put_item(
		Item={
		    'link_route': 'facebook',
		    'urls': [
		    	['https://www.facebook.com', Decimal('.99')],
		    	['https://www.youtube.com/watch?v=m1yWUWhamj4', Decimal('.01')]
		    ]
		}
	)
    return response

