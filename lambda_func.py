import json
from lamda_bridge import lambda_bridge

def lambda_handler(event, context):
    print(event)
    bridge = lambda_bridge(event['user'], event['passwd'])
    switch = {
        "login": "bridge.login()",
        "load": "bridge.load(event['init_token'])",
        "get_token": "bridge.get_token()",
        "get_doors": "bridge.get_doors()",
        "get_door_status": "bridge.status(event['door_id'], event['door'], event['portal'])"
    }
    #login or load
    ret = eval(switch.get(event['init']))
    #run command
    cmd_ret = eval(switch.get(event['cmd']))
    
    return {
        'statusCode': 200,
        'body': "{}".format(cmd_ret)
    }
