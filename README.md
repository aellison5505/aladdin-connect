# aladdin-connect
Python module that allows interacting with Genie Aladdin Connect devices for use with AWS Lambda

Note that shared doors are not currently supported, only doors that are owned by your account can be controlled

## Usage
```
from aladdin_connect import AladdinConnectClient

# Create session using aladdin connect credentials
client = AladdinConnectClient(email, password)
client.login()
token = client.get_token()

# Or load token if saved
client = AladdinConnectClient(email, null)
client.load(token)

# Get list of available doors
doors = client.get_doors()
my_door = doors[0]

# Issue commands for doors
client.close_door(my_door['device_id'], my_door['door_number'])
client.open_door(my_door['device_id'], my_door['door_number'])

# Get updated door status
client.get_door_status(my_door['device_id'], my_door['door_number'])

#lambda_test set envs
test_lambda.py 

```
