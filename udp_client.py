# import socket as sc
#
# sock = sc.socket(sc.AF_INET,sc.SOCK_DGRAM)
#
# message = input("Введите текст для передачи на сервер: ")
# message = message.encode()
#
# sock.sendto(message, ('localhost', 8888))
import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

sock.connect(('localhost', 8888))

while True:
    message = input("Введите сообщение: ")

    sock.send(message.encode())