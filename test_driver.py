from aladdin_connect import AladdinConnectClient
import sys

email = sys.argv[1]
password = sys.argv[2]
token = sys.argv[3]
client = AladdinConnectClient(email, password)
client.login()
token = client.get_token()
print("Token: {}".format(token.strip('"')))
#client.load(token)
doors = client.get_doors()
print(doors)
