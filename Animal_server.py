import socket as sc
import threading
import pickle
from AnimalModule import Animal

def handle_client(client, addr):
    while True:
        result = client.recv(4096)
        if not result:
            break
        objectNew = pickle.loads(result)
        result_name = objectNew.animal_name()
        result_type = objectNew.animal_type()
        print(result_name, '\n', result_type, '\n IP: ', addr)

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
