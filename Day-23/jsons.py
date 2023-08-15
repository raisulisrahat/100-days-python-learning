# Here i am showing Built-in JSON Module python

import json

info = '{"Name": "Rahat", "Age" : 24,"Address" : "Dhaka", "Blood": "O+", "Nationality" : "Bangladeshi"}'

x = json.loads(info)

print(x["Age"])

y = json.dumps(info)
print(y)

print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))