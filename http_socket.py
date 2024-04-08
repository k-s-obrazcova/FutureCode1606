import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

sock.connect(('example.com',80))

content = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
request_http = '\n'.join(content)
print(request_http)
print('-'*20)

sock.send(request_http.encode())
result = sock.recv(65532)

print(result.decode('utf-8'))