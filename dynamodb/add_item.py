import boto3
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Movies')

title =input("Enter the title: ")
year = int(input("Enter the movie realsed year: "))
def add_item():
    response = table.put_item(
       Item={
            'year': year,
            'title': title,
            'info': {
                'plot':"Nothing happens at all.",
                'rating': decimal.Decimal(0)
            }
        }
    )
    print("PutItem succeeded:")
    print(json.dumps(response, indent=6, cls=DecimalEncoder))

    return

print(add_item())

