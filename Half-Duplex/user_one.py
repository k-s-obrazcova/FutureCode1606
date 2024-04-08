import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

# Байтовое представление строки (работает с латиницей)
message_byte = b'How your day?'

# Ошибка
# message_byte_ru = b'Как прошел твой день?'


# Использование метода encode для преобразования в строку байтов
message_str = 'How your day?'
message_str = message_str.encode()

# Использование метода encode для преобразования русских символов
message_str_ru = 'Как прошел твой день?'
message_str_ru = message_str_ru.encode()


sock.sendto(message_str_ru, ('localhost', 8888))

import socket as sc

sock = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)

sock.bind(('127.0.0.1', 7654))

length_message = int(input('Введите, пожалуйста, размер ожидаемого пакет: '))

while True:
    try:
        result = sock.recv(length_message)
    except KeyboardInterrupt:
        print("Программа была досрочно завершена")
        sock.close()
    except sc.error as e:
        print(e)
        print("Принять данные не удалось")
    except Exception as e:
        print(e)
        sock.close()
        break
    else:
        print("Message: ", result.decode('utf-8'))