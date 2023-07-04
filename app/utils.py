import json
from datetime import datetime


def get_operations(path) -> list[dict]:
    """
    Получаем файл с операциями
    """
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def get_execute_operation(operations: list[dict]) -> list[dict]:
    """
    Список выполненных (EXECUTED) операций
    """
    executed_operations = []
    for operation in operations:
        if operation.get('state') == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def get_sorted_operations(operations: list[dict]) -> list[dict]:
    """
    Сверху списка находятся самые последние операции (по дате).
    """
    return sorted(operations, key=lambda operation: operation["date"], reverse=True)


def convert_date(str_date: str) -> str:
    """
    Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)
    """
    date_time_obj = datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(date_time_obj, '%d.%m.%Y')


def convert_number_from(item: str) -> str:
    """
    Номер карты замаскирован и не отображается целиком
    """
    if not item:
        return ''
    item_list = item.split(' ')
    num = item_list.pop(-1)
    start_str = ' '.join(item_list)
    return f'{start_str} {num[:4]} {num[4:6]}** **** {num[-4:]}'


def convert_number_to(item: str) -> str:
    """
    Номер счета замаскирован и не отображается целиком
    """
    if not item:
        return ''
    item_list = item.split(' ')
    num = item_list.pop(-1)
    start_str = ' '.join(item_list)
    return f'{start_str} **{num[-4:]}'


def prepare_data(operation: dict) -> str:
    """
    Подготовка текста на вывод
    """
    date = convert_date(operation["date"])
    send_from = convert_number_from(operation.get("from"))
    send_to = convert_number_to(operation["to"])
    description = operation.get("description")
    amount = operation["operationAmount"]["amount"]
    currency_name = operation["operationAmount"]["currency"]["name"]
    return f'{date} {description} \n{send_from} -> {send_to} \n{amount} {currency_name}'


def get_user_dats(operations: list[dict]) -> None:
    for operation in operations[:5]:
        print(f'{prepare_data(operation)}\n')
