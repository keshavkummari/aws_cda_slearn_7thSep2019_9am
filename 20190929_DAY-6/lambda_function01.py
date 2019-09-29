def lambda_handler(event, context):
    print("In Lambda Handler")
    
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            
        },
        "body": "Keshav Kummari"
        
        
    }
    return resp 

print(lambda_handler('AWS','Lambda'))