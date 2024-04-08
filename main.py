class OwnException(Exception):
    def __init__(self, message="Обрабатываемая пользовательская ошибка"):
        super().__init__(message)


def convert_value(value, target_type):
    try:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == bool:
            return bool(value)
        elif target_type == str:
            return str(value)
        elif target_type == list:
            return list(value)
        else:
            raise OwnException(f"Неподдерживаемый тип: {target_type}")
    except ValueError:
        raise OwnException(f"Невозможно преобразовать {value} в тип данных {target_type}")



try:
    value_result = convert_value("text",list)
    print(value_result)
except OwnException as e:
    print(f"Поймано пользовательское исключение: {e}")