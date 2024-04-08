import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

sock.connect(('localhost', 8888))

while True:
    message = input("Введите сообщение: ")

    sock.send(message.encode())