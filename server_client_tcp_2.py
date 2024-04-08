
import socket as sc

duplextype = input("Введите тип - client или server: ")
if duplextype == "server":
    sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    sock.bind(('localhost', 9090))

    sock.listen(3)

    sock.settimeout(4)  # Установка времени ожидания (4 сек)
    sock.settimeout(0)  # == sock.setblocking(False)
    sock.settimeout(None)  # == sock.setblocking(True)

    while True:
        try:
            client, addr = sock.accept()
        except sc.error as e:
            print(e)
        except KeyboardInterrupt:
            sock.close()
            break
        else:
            while True:
                result = client.recv(1024)
                if result.decode('utf-8') == 'exit':
                    client.close()
                    break
                print('Address:', addr, '\nMessage:', result.decode('utf-8'))
elif duplextype == "client":
    sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)

    sock.connect(('127.0.0.1', 9090))  # Соединение с получателем
    # После успешного соединения

    while True:
        message = input('Напишите сообщение: ')
        sock.send(message.encode('utf-8'))  # Отправка сообщения
        if message == 'exit':
            sock.close()  # Закрытие сокета - разрыв соединения
            break
else:
    print("Ошибка")


