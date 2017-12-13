
import json
import requests

payload = {'type': 'ADD', 'data': 1.5}

r = requests.post('http://localhost:4567/test', data=json.dumps(payload) )

print( json.loads( r.text )  )

