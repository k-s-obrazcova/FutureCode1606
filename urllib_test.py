from urllib import request

responce = request.urlopen('http://example.com')

print(responce.read().decode('utf-8'))