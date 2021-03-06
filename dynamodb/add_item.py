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



#dynamodb= boto3.resource('dynamodb')
#table= dynamodb.Table('Movies')
#
#response= table.put_item(
#    Item={
#        "year" : 2018,
#        "title" : "KGF chapter I!",
#        "info" : {
#            "directors" : [
#                "Prashanth Neel"
#            ],
#            "producer" : [
#              "Vijay Kiragandur"
#            ],
#            "release_date" : "2018-December-21",
#            "rating" : 8,
#            "genres" : [
#                "Action",
#                "Adventure"
#            ],
#            "image_url" : "https://www.google.com/imgres?imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fen%2Fc%2Fcc%2FK.G.F_Chapter_1_poster.jpg&imgrefurl=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FK.G.F%3A_Chapter_1&tbnid=fEJWBaHUgHoK6M&vet=12ahUKEwjNhISzrpDpAhXg-jgGHckECk0QMygBegUIARDnAQ..i&docid=1vfO3zLZJXMOgM&w=223&h=300&q=k.g.f&ved=2ahUKEwjNhISzrpDpAhXg-jgGHckECk0QMygBegUIARDnAQ",
#            "plot" : "A Majority of the film is set in Kolar Gold Fields and was filmed on location.",
#            "rank" : 10,
#            "running_time" : "2-hour-36-minutes",
#            "actors" : [
#                "Yash",
#                "Srinidi Shetty",
#                "Ramachandra Raju"
#           ]
#        }
#    }
#)
#
#print("Putitem successfull.....")
#print(response)
#



