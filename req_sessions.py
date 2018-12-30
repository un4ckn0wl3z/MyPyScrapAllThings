import requests
import json
# builds on top of urllib3's connection pooling
# session reuses the same TCP connection if
# requests are made to the same host
# see https://en.wikipedia.org/wiki/HTTP_persistent_connection for details
session = requests.Session()
# You may pass in custom cookie
r = session.get('http://httpbin.org/get', cookies={'my-cookie': 'browser'})
print(r.text)
# '{"cookies": {"my-cookie": "test cookie"}}'
# Streaming is another nifty feature
# From http://docs.python-requests.org/en/master/user/advanced/#streaming-requests
# copyright belongs to reques.org
r = requests.get('http://httpbin.org/stream/3', stream=True)

for line in r.iter_lines():
	# filter out keep-alive new lines
	if line:
		decoded_line = line.decode('utf-8')
		print(json.loads(decoded_line))