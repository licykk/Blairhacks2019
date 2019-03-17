import boto3
import json
from Main import addItemFromDatabase

def updateDataFromDatabase():
	dynamodb=boto3.resource('dynamodb',aws_access_key_id='AKIAJ2G7XDVUD22HN3RA',aws_secret_access_key='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',region_name='us-east-1')    table = dynamodb.Table('blairfinalfinaltable')
    data = table.scan()["Items"]
    for task in data:
	    addItemFromDatabase(task["activityName"], task["duration"])

