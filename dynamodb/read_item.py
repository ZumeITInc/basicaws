import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb= boto3.resource('dynamodb')
table= dynamodb.Table('Movies')

##  Read an
def read_item(name=None):
    "It reads the item in dynamodb table"

    response = table.get_item(
        Key={
            'year':2020,
            'title': name
        }
    )

    item=response['Item']

    info= item['info']

    print(item)
    print(info)

    return


##Query an item in table

def query_items(year):
    response= table.query(
        KeyConditionExpression = Key('year').eq(year)
    )
    items = response["Items"]
    print(items)

    return

#query_items(0)

##Scan item in table

def scan_items(year):

    response=table.scan(
        FilterExpression =Attr('year').eq(year)
    )
    items= response["Items"]
    return items

print(scan_items(2020))

##Delete an item in table

def del_item(title):
    "it deletes the item in dynamodb table"
    response= table.delete.item(
        Key={
            'year':2020,
            'title': title
        }
    )
    print(title, "item deleted succfull")
    return

#del_item(title)