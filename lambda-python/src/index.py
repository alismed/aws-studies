import json

def lambda_handler(event, context):
   sts_data = [{"access_token": "1234567890",
                "token_type": "Bearer",
                "expires_in": 300,
                "refresh_token": "0987654321",
                "scope": "apid-1234",
                "active": True }]

   return {'statusCode': 200,
           'headers': {
           "Access-Control-Allow-Origin": "*",
           "Access-Control-Allow-Methods": 'POST'
           },'body':sts_data 
   }

