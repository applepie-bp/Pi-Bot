

import urllib.request

response = urllib.request.urlopen("http://10.14.132.189/forward")
response_text = response.read()
print(response_text)
