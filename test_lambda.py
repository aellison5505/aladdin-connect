from lambda_func import lambda_handler
import sys

event = {
  "user": sys.argv[1],
  "passwd": sys.argv[2],
  "init": "load",
  "init_token": sys.argv[3],
  "cmd": "get_door_status",
  "door_id": sys.argv[4],
  "door": sys.argv[5],
  "portal": sys.argv[6]

  
}

context = {}

ret = lambda_handler(event, context)

print(ret)
