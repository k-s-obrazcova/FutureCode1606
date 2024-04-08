# import socket as sc
#
# sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
#
# sock.connect(('localhost', 8888))
#
# while True:
#     message = input("Введите сообщение: ")
#
#     sock.send(message.encode())
#
#
#

import socket as sc

# Список сообщений для отправки на сервер
messages = ["Привет", "Как дела?", "Пока"]

# Создаем и подключаем несколько клиентских сокетов
for message in messages:
    sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8888))
    sock.send(message.encode('utf-8'))
    sock.close()