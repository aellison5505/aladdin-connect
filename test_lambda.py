from lambda_func import lambda_handler
import sys

event = {
  "user": sys.argv[1],
  "passwd": sys.argv[2],
  "token": sys.argv[3]
}

ret = lambda_handler(event, None)

print(ret)
