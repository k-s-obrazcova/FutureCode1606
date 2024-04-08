import socket as sc

sock = sc.socket(sc.AF_INET,sc.SOCK_DGRAM)

sock.bind(('localhost', 8888))

while True:
    try:
        result = sock.recv(1024)
        print(f"Message: {result.decode('utf-8')}")
    except Exception as e:
        print(e)
        sock.close()
        break


# import socket as sc
# sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
# sock.bind(('localhost', 8888))
# result = sock.recv(1024)
#
# print("Message: ", result.decode('utf-8'))
#
# sock.close()