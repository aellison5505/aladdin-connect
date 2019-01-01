import json
from aladdin_connect import AladdinConnectClient

def lambda_handler(event, context):
    print(event)
    client = AladdinConnectClient(event['user'], event['passwd'])
    client.login()
    token = client.get_token()
    print('Token: {}'.format(token))

    # Or load token
    #client.load(token)
    
    return {
        'statusCode': 200,
        'body': "Token {}".format(token.strip('"'))
    }
