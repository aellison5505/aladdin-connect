from aladdin_connect import AladdinConnectClient

class lambda_bridge:

    def __init__(self, user, passwd):
        self._client = AladdinConnectClient(user, passwd)
            
    def login(self):
        self._client.login()
        return True
    
    def load(self, token):
        self._client.load(token)
        return True

    def get_token(self):
        token = self._client.get_token()
        sToken = 'Token: {}'.format(token).strip('"')
        return sToken

    def get_doors(self):
        return self._client.get_doors()

    def status(self, device, door, portal):
        doors = self._client.set_device_protal(portal, device)
        door_status = self._client.get_door_status(device, door)
        return door_status

