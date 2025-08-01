import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("москва", "Москва"),
    ("привет, мир", "Привет, мир"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Привет", "Привет"),
    (" привет", "привет"),
    ("", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_value", [
    None,
    123,
    ['list'],
])
def test_trim_negative(input_value):
    with pytest.raises((TypeError, AttributeError)):
        string_utils.trim(input_value)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Привет", "р", True),
    ("Привет!", "!", True),
    ("", "", True),
    ("135", "5", True),
    ("Привет", "В", False),
    ("Привет", "t", False),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_string, input_symbol", [
    ("Привет", "$"),
    (["list"], "в"),
])
def test_contains_negative(input_string, input_symbol):
    actual_result = string_utils.contains(input_string, input_symbol)
    assert actual_result is False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Привет мир", " ", "Приветмир"),
    ("Привет!", "!", "Привет"),
    ("Привет", "т", "Приве"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_value, symbol", [
    ("Привет", "%"),
    ("Привет", "g"),
    ("Привет", "3"),
])
def test_delete_symbol_negative(input_value, symbol):
    result = string_utils.delete_symbol(input_value, symbol)
    assert result == input_value
