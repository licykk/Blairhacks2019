import boto3
import json
from Main import addItemFromDatabase

def updateDataFromDatabase():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('blairfinalfinaltable')
    data = table.scan()["Items"]
    for task in data:
	    addItemFromDatabase(task["activityName"], task["duration"])

