import pytest
import sys
from our_function import sum_list_last_first, add, divide, Calculator


def test_positive():
    """
    Test sum_list_last_first with a list of three elements
    """
    my_list = [1, 2, 3]
    actual = sum_list_last_first(my_list)
    expected = 1.5
    assert actual == expected
    
def test_second():
    """
    Test sum_list_last_first with a list of two elements
    """
    my_list = [1, 2]
    actual = sum_list_last_first(my_list)
    expected = 1.0
    assert actual == expected, f"Це впало тому що гладіолус {expected}"

def test_none():
    my_list = [1]
    actual = sum_list_last_first(my_list)
    assert actual is None

def test_error():
    with pytest.raises(ZeroDivisionError):
        my_list = [3, 5, -3]
        sum_list_last_first(my_list)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
    
    # Тестування винятків
    with pytest.raises(ValueError):
        divide(5, 0)

def test_calculator_class():
    calc = Calculator()
    result = calc.multiply(3, 4)
    assert result == 12
    assert "3 * 4 = 12" in calc.history


@pytest.mark.parametrize("a,b,expected", [(2, 2, 4), (1, 2, 2)])
def test_calculator_parametr(a, b, expected):
    calc = Calculator()
    result = calc.multiply(a, b)
    assert result == expected

@pytest.mark.xfail
def test_div():
    a = 2 / 0
    # assert True

@pytest.mark.xfail(reason="Bug #123: subtraction logic is incorrect")
def test_subtraction_bug():
    assert 5 - 3 == 1   # wrong on purpose

@pytest.mark.xfail(sys.platform.startswith("win"), reason="Does not work on Windows")
def test_linux_only_feature():
    assert 42 == 42

# @pytest.mark.xfail(strict=True, reason="Does not work on Windows")
# def test_windows_only_feature():
#     assert 42 == 42

def test_check_server_conn(get_server):
    assert get_server == "192.168.0.1"


def test_check_files(create_files):
    assert True

def test_check_vm():
    assert True

@pytest.mark.skip(reason="Причина пропуску тесту")
def test_for_skip():
    pass

def should_skip():
    # os.name == "nt" # значить стоїть вінд
    return True  # Умова, за якої потрібно пропустити тест, наприкл. тест лише для linux

@pytest.mark.skipif(should_skip(), reason="Unsupported OS")
def test_skip_if():
    assert True

@pytest.mark.smoke
def test_count():
    actual_result = sum([1, 2])
    expected_result = 3
    assert actual_result == expected_result, f"Wrong data! actual_result: {actual_result} expected_result:{expected_result}"
