"""
This file, 'pytest_example.py', is used to test 'py_example.py' functions.
'pytest_example.py' and 'py_example.py' must exist in same directory
'python requests" must also be installed

Invoke with verbosity via 'pytest -vrP'
Invoke without verbosity via 'pytest'
"""
#   function imports    
from py_example import display_name_weekday, display_name_weekend
from py_example import display_OS_version, display_python_module_name
from py_example import divide, file_remove, fizzbuzz
from py_example import get_joke, get_random_int, is_weekday, len_joke
#   standard library imports
from io import StringIO
import datetime
import sys
#   Pytest import(s)
### from pytest_mock import MockerFixture
import pytest
#   unittest imports
from unittest import mock
from unittest.mock import MagicMock, Mock, patch
import unittest

def test_display_OS_version():
    display_OS_version()

def test_display_python_module_name():
    """Ensure that module ( py_example ) includes appropriate import statement(s)"""
    print('Testing Module:', end=' ')
    display_python_module_name()

def test_divide_negatives():
    dividend = -14
    divisor = -5
    expected_result = 2.8
    floor_division_result = 2
    result = divide(dividend, divisor)
    # Get function name
    func_name = sys._getframe().f_code.co_name
    if result == floor_division_result:
        print(f"\n'{func_name}()' - Division incorrectly coded as floor division returned '{result}'"
        f"instead of '{expected_result}'")
    assert result == expected_result

def test_divide_mixed_01():
    dividend = -14
    divisor = 5
    expected_result = -2.8
    floor_division_result = -3
    result = divide(dividend, divisor)
    # Get function name
    func_name = sys._getframe().f_code.co_name
    if result == floor_division_result:
        print(f"\n'{func_name}()' - Division incorrectly coded as floor division returned '{result}'"
        f"instead of '{expected_result}'")
    assert result == expected_result

def test_divide_mixed_02():
    dividend = 14
    divisor = -5
    expected_result = -2.8
    floor_division_result = -3
    result = divide(dividend, divisor)
    # Get function name
    func_name = sys._getframe().f_code.co_name
    if result == floor_division_result:
        print(f"\n'{func_name}()' - Division incorrectly coded as floor division returned '{result}'"
        f"instead of '{expected_result}'")
    assert result == expected_result

def test_divide_positives():
    dividend = 14
    divisor = 5
    expected_result = 2.8
    floor_division_result = 2
    result = divide(dividend, divisor)
    # Get function name
    func_name = sys._getframe().f_code.co_name
    if result == floor_division_result:
        print(f"\n'{func_name}()' - Division incorrectly coded as floor division returned '{result}'"
        f"instead of '{expected_result}'")
    assert result == expected_result

def test_divide_bad_value_01():
    dividend = 11
    divisor = 'a'
    with pytest.raises(ValueError):
        divide(dividend, divisor)

def test_divide_bad_value_02():
    dividend = 'b'
    divisor = 22
    with pytest.raises(ValueError):
        divide(dividend, divisor)

def test_divide_by_zero_11():
    # Preferred syntax
    dividend = 11
    divisor = 0
    with pytest.raises(ZeroDivisionError):
        divide(dividend, divisor)

def test_divide_by_zero_22():
    # Alternative syntax
    dividend = 22
    divisor = 0
    with pytest.raises(ZeroDivisionError):
        divide(dividend, divisor)

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_200_OK_get_joke(mock_requests):
    # HTTP Status Code 200 - OK
    # The expected_response should == the mocked URL response
    mock_response = MagicMock(status_code = 200)
    test_string = 'Mocked ( OK ) URL response_string'
    mock_response.json.return_value = {'value': test_string}
    mock_requests.get.return_value = mock_response
    expected_response = test_string
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_301_get_joke(mock_requests):
    # HTTP Status Code 301 - Permanent Redirect
    # Expecting ONLY the expected_response associated with the status_code
    mock_response = MagicMock(status_code = 301)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '301 - Permanent Redirect'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_302_get_joke(mock_requests):
    # HTTP Status Code 302 - Temporary Redirect
    # Expecting ONLY the expected_response associated with the status_code
    mock_response = MagicMock(status_code = 302)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '302 - Temporary Redirect'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_401_get_joke(mock_requests):
    # HTTP Status Code 401 - Unauthorized
    # Expecting ONLY the expected_response associated with the status_code
    mock_response = MagicMock(status_code = 401)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '401 - Unauthorized'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_403_get_joke(mock_requests):
    # HTTP Status Code 403 - Forbidden
    # Expecting ONLY the expected_response associated with the status_code
    mock_response = MagicMock(status_code = 403)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '403 - Forbidden'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_404_get_joke(mock_requests):
    # HTTP Status Code 404 - Not Found
    # Expecting ONLY the expected_response associated with the status_code
    mock_response = MagicMock(status_code = 404)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '404 - Not Found'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_410_get_joke(mock_requests):
    # HTTP Status Code 410 - Gone
    # Expecting ONLY the expected_response associated with the status_code
    mock_response = MagicMock(status_code = 410)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '410 - Gone'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_500_get_joke(mock_requests):
    # HTTP Status Code 500 - Internal Server Error
    # Expecting ONLY the expected_response associated with the status_code
    mock_response = MagicMock(status_code = 500)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '500 - Internal Server Error'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_502_get_joke(mock_requests):
    # HTTP Status Code 502 - Bad Gateway
    # Expecting ONLY the expected_response associated with the status_code
    # Expecting ONLY the expected_response
    mock_response = MagicMock(status_code = 502)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '502 - Bad Gateway'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_503_get_joke(mock_requests):
    # HTTP Status Code 503 - Service Unavailable
    # Expecting ONLY the expected_response associated with the status_code
    # Expecting ONLY the expected_response
    mock_response = MagicMock(status_code = 503)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '503 - Service Unavailable'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.requests', autospec=True)
def test_504_get_joke(mock_requests):
    # HTTP Status Code 504 - Gateway Timeout
    # Expecting ONLY the expected_response associated with the status_code
    mock_response = MagicMock(status_code = 504)
    mock_response.json.return_value = {'value': 'place_holding_string'}
    mock_requests.get.return_value = mock_response
    expected_response = '504 - Gateway Timeout'
    assert get_joke() == expected_response

# unittest imports required here
@patch('py_example.get_joke', autospec=True)
def test_len_joke(mock_get_joke):
    # Test a function that calls another function
    test_string = "len_joke()' in module 'py_example.py' called 'get_joke()'"
    mock_get_joke.return_value = test_string
    assert len_joke() == len(test_string)

# unittest imports required here
@patch('sys.stdout', new_callable=StringIO)
# Cannot use 'autospec' and 'new_callable' together
# @patch('sys.stdout', new_callable=StringIO, autospec=True)
def test_display_name_weekday(mock_stdout):
# Mimic ( 'stdout' ) from print() used in tested function
    test_name = 'random_formatted_day_name'
    expected_formatted_result = f"'display_name_weekday()' Day of the week == {test_name}\n"
    display_name_weekday(test_name)
    assert mock_stdout.getvalue() == expected_formatted_result

# unittest imports required here
@patch('sys.stdout', new_callable=StringIO)
# Cannot use 'autospec' and 'new_callable' together
# @patch('sys.stdout', new_callable=StringIO, autospec=True)
def test_display_name_weekend(mock_stdout):
# Mimic ( 'stdout' ) from print() used in tested function
    test_name = 'random_formatted_day_name'
    expected_formatted_result = f"'display_name_weekend()' Day of the week == {test_name}\n"
    display_name_weekend(test_name)
#    self.assertEqual(mock_stdout.getvalue(), expected_formatted_result)
    assert mock_stdout.getvalue() == expected_formatted_result

# unittest imports required here
@mock.patch('py_example.os.path')
@mock.patch('py_example.os')
# autospec=True throws errors
def test_file_remove(mock_os, mock_path):
    # set up the mock
    mock_path.isfile.return_value = False
    file_remove("any path")
    # test that the remove call was NOT called.
    coding_error_improper_file_removal_attempt = ("\nCoding error. Improper file removal attempt. "
    "Test for it's existence FIRST!!")
    assert mock_os.remove.called == False, coding_error_improper_file_removal_attempt
    # make the file 'exist'
    mock_path.isfile.return_value = True
    # Ensure that the correct argument was passed to the remove call
    file_remove("any path")
    mock_os.remove.assert_called_with("any path")
    # Ensure that 'file_remove()' contains just a SINGLE remove call
    invalid_call_count = "Only ONE removal attempt was expected"
    assert mock_os.remove.call_count == 1, invalid_call_count

# unittest imports required here
@mock.patch('py_example.randint', return_value=7, autospec=True)
def test_get_random_int(mock_randint):
# Mimic ( 'randint' ) used in tested function
# Code in tested function ( returned_value = modifier + roll )
# Adjust mocked randint return value and modifier parameter to suit
    modifier = 2
    expected_result = 9
    assert get_random_int(modifier) == expected_result
    # Verify that randint was called with expected parameters
    mock_randint.assert_called_once_with(1, 8)

# unittest imports required here
def test_weekend():
# Mimic ( 'datetime' ) used in tested function
    # Weekend test dates
    # Day 05 Saturday == 2018_1006
    # Day 06 Sunday == 2018_1007
    mock_date = Mock(wraps=datetime.datetime, autospec=True)
    saturday = datetime.datetime(year=2018, month=10, day=6)
    sunday = datetime.datetime(year=2018, month=10, day=7)
    mock_date.now.return_value = saturday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_weekday()
    mock_date.now.return_value = sunday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_weekday()

# unittest imports required here
def test_weekday():
# Mimic ( 'datetime' ) used in tested function
    # Weekday test dates
    # Day 00 Monday == 2018_1001
    # Day 01 Tuesday == 2018_1002
    # Day 02 Wednesday == 2018_1003
    # Day 03 Thursday == 2018_1004
    # Day 04 Friday == 2018_1005
    mock_date = Mock(wraps=datetime.datetime, autospec=True)
    monday = datetime.datetime(year=2018, month=10, day=1)
    tuesday = datetime.datetime(year=2018, month=10, day=2)
    wednesday = datetime.datetime(year=2018, month=10, day=3)
    thursday = datetime.datetime(year=2018, month=10, day=4)
    friday = datetime.datetime(year=2018, month=10, day=5)
    mock_date.now.return_value = monday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_weekday()
    mock_date.now.return_value = tuesday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_weekday()
    mock_date.now.return_value = wednesday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_weekday()
    mock_date.now.return_value = thursday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_weekday()
    mock_date.now.return_value = friday
    with patch('datetime.datetime', new=mock_date):
        flag_weekday = is_weekday()

def test_zfizzbuzz():
    """Changed name 'fizzbuz' to 'zfizzbuz' to influence test order"""
#   Determine which set of values to use
### index = 0
### index = 1
    index = 2
### index = 3
### index = 4
#
    list_buzz = []
    list_fizz = []
    list_fizzbuzz = []
#
    fizz_actual_results = []
    buzz_actual_results = []
    fizzbuzz_actual_results = []
#
    fizz_expected_results = []
    buzz_expected_results = []
    fizzbuzz_expected_results = []
#
    fizz_expected_results.append(
    ['-36 == Fizz', '-32 == Fizz', '-28 == Fizz', '-24 == Fizz', '-20 == Fizz', '-16 == Fizz', '-12 == Fizz', '-8 == Fizz', '-4 == Fizz', '4 == Fizz', '8 == Fizz', '12 == Fizz', '16 == Fizz', '20 == Fizz', '24 == Fizz', '28 == Fizz', '32 == Fizz', '36 == Fizz'])
    fizz_expected_results.append(
    ['-32 == Fizz', '-28 == Fizz', '-24 == Fizz', '-20 == Fizz', '-16 == Fizz', '-12 == Fizz', '-8 == Fizz', '-4 == Fizz', '4 == Fizz', '8 == Fizz', '12 == Fizz', '16 == Fizz', '20 == Fizz', '24 == Fizz', '28 == Fizz', '32 == Fizz']) 
    fizz_expected_results.append(
    ['-35 == Fizz', '-30 == Fizz', '-25 == Fizz', '-20 == Fizz', '-15 == Fizz', '-10 == Fizz', '-5 == Fizz', '5 == Fizz', '10 == Fizz', '15 == Fizz', '20 == Fizz', '25 == Fizz', '30 == Fizz', '35 == Fizz'])
    buzz_expected_results.append(
    ['-36 == Buzz', '-30 == Buzz', '-24 == Buzz', '-18 == Buzz', '-12 == Buzz', '-6 == Buzz', '6 == Buzz', '12 == Buzz', '18 == Buzz', '24 == Buzz', '30 == Buzz', '36 == Buzz'])
    buzz_expected_results.append(
    ['-35 == Buzz', '-28 == Buzz', '-21 == Buzz', '-14 == Buzz', '-7 == Buzz', '7 == Buzz', '14 == Buzz', '21 == Buzz', '28 == Buzz', '35 == Buzz'])
    buzz_expected_results.append(
    ['-35 == Buzz', '-28 == Buzz', '-21 == Buzz', '-14 == Buzz', '-7 == Buzz', '7 == Buzz', '14 == Buzz', '21 == Buzz', '28 == Buzz', '35 == Buzz'])
    fizzbuzz_expected_results.append(
    ['-36 == FizzBuzz', '-24 == FizzBuzz', '-12 == FizzBuzz', '12 == FizzBuzz', '24 == FizzBuzz', '36 == FizzBuzz'])
    fizzbuzz_expected_results.append(
    ['-28 == FizzBuzz', '28 == FizzBuzz'])
    fizzbuzz_expected_results.append(
    ['-35 == FizzBuzz', '35 == FizzBuzz'])
#
    list_fizz, list_buzz, list_fizzbuzz =  fizzbuzz(index)

    print(f"FIZZ\n{list_fizz}\nBUZZ\n{list_buzz}\nFIZZBUZZ\n{list_fizzbuzz}")
#
    flag_fizz = False
    if fizz_expected_results[index - 2] == list_fizz:
        flag_fizz = True
        print("\nExpected 'fizz' Results == Actual 'fizz'_Results")
#
    flag_buzz = False
    if buzz_expected_results[index - 2] == list_buzz:
        flag_buzz = True
        print("Expected 'buzz' Results == Actual 'buzz'_Results")
#
    flag_fizzbuzz = False
    if fizzbuzz_expected_results[index - 2] == list_fizzbuzz:
        flag_fizzbuzz = True
        print("Expected 'fizzbuzz' Results == Actual 'fizzbuzz'_Results")
#
    ### print(flag_fizz, flag_buzz, flag_fizzbuzz)
#
    status_fail = "Testing of 'fizzbuzz'  Failed"
    status_pass = "Testing of 'fizzbuzz'  Passed"
    if all ([flag_fizz, flag_buzz, flag_fizzbuzz]) == True:
        print(status_pass)
        # Returning other than 'None' is DEPRECATD
        # return status_pass
        return
    else:
        print(status_fail)
        # Returning other than 'None' is DEPRECATD
        # return status_fail
        return
    return

# EOF
