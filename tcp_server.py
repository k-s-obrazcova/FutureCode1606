import socket as sc
import threading

def handle_client(client, addr):
    while True:
        result = client.recv(1024)
        if not result:
            break
        print(f'Address: {addr} \nMessage: {result.decode('utf-8')}')

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

sock.bind(('localhost', 8888))

sock.listen(3)

sock.settimeout(None)

while True:
    try:
        client,addr = sock.accept()
        client_thread = threading.Thread(target=handle_client,args=(client,addr))
        client_thread.start()
    except Exception as e:
        sock.close()
        break
