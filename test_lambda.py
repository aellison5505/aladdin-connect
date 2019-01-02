from lambda_func import lambda_handler
import os
from dotenv import load_dotenv
load_dotenv(override=True)

event = {
  "user": os.getenv('user'),
  "passwd": os.getenv('passed'),
  "init": os.getenv('init'),
  "init_token": os.getenv('init_token'),
  "cmd": os.getenv('cmd'),
  "door_id": os.getenv('door_id'),
  "door": os.getenv('door'),
  "portal": os.getenv('portal')

}

context = {}

ret = lambda_handler(event, context)

print(ret)
