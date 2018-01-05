

import urllib.request

response = urllib.request.urlopen("http://10.14.132.180:5000/forward")
response_text = response.read()
print(response_text)
