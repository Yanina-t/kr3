import json
from unittest.mock import patch, mock_open
from app.utils import get_operations, get_execute_operation, get_sorted_operations, convert_date, convert_number_from, \
    convert_number_to, prepare_data


def test_get_operations(operations):
    with patch("builtins.open", mock_open(read_data=json.dumps(operations))):
        assert get_operations("path/to/open") == operations


def test_get_execute_operation(operations):
    for el in get_execute_operation(operations):
        assert el["state"] == "EXECUTED"


def test_sorted_operations(operations):
    operation_def = get_sorted_operations(operations)
    assert operations[0] != operation_def[0]


def test_convert_date():
    data_def_ = convert_date("2019-07-03T18:35:29.512364")
    assert data_def_ == "03.07.2019"


def test_convert_number_from():
    number_from = convert_number_from('MasterCard 7158300734726758')
    assert number_from == 'MasterCard 7158 30** **** 6758'


def test_convert_number_to():
    number_to = convert_number_to('Счет 35383033474447895560')
    assert number_to == 'Счет **5560'


def test_prepare_data(operations):
    for el in operations:
        num = prepare_data(el)
        assert num
