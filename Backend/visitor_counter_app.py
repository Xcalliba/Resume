import boto3
import os
import json
import uuid
import datetime 



def lambda_handler(event, context):
  
  dynamodb = boto3.resource('dynamodb')

  table = dynamodb.Table('site-visitor-counter')

  res = table.update_item(
    Key={"website": "numberofVisitors"},
    UpdateExpression="ADD Site :inc",
    ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues="UPDATED_NEW"
    )

    # Format dynamodb response into variable
  responseBody = json.dumps({"numberofVisitors": int(float(res["Attributes"]["Site"]))})
  print(responseBody)
   #API Response Object And Format To JSON
  apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT,DELETE" 
        },
    }

    # Return API Response
  return apiResponse