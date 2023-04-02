#!/usr/bin/env python3
"""
This file, 'py_example.py', is configured for lambda zip deployment and
contains functions testable using either the pytest or unittest framework.
'python requests" must be installed.

For lambda zip deployment python requests must be zipped with this file.

Invoke with verbosity via 'pytest -vrP'
Invoke without verbosity via 'pytest'
"""
#   standard library import(s)
from random import randint
import datetime
import json
import os
import os.path
import sys
#   python related imports
import platform
import requests
#
# python related:
#
#   If a module referenced by @patch() is unavailable, UGLY errors will occur
#
# Install pip:
#   GLOBALLY ( sudo dnf install -y python3-pip )
#   LOCALLY ( pip install --user --upgrade pip )
#   InVirtualEnvironment ( Installed and PATH set via activation )
#
# Install responses:
#   GLOBALLY ( sudo pip install responses )
#   LOCALLY ( pip install --user --upgrade responses )
#   InVirtualEnvironment ( pip install responses )
#
# Display version and installation location of PIP installed package:
#   ( pip show PackageName )
#
# Update PIP installed package(s):
#   ( pip install --update requests )
#   ( pip install --update responses )
#
# Install python 'requests' in current directory via:
#   ( pip install requests -t . )
#

def display_OS_version():
    version = platform.uname()
    print(f"\n{version}\n")
    return

def display_name_weekday(day):
    print(f"'display_name_weekday()' Day of the week == {day}")
    return

def display_name_weekend(day):
    print(f"'display_name_weekend()' Day of the week == {day}")
    return

def display_python_module_name():
    print(f'{os.getcwd()}/{os.path.basename(__file__)}')
    return

def divide(x, y):
    """Divide Function"""
    if y == 0:
        # Either of the following lines can be used to throw an error
        # Use of ZeroDivisionError mimics the REPL
        raise ZeroDivisionError('DD-division by zero')
#       raise ValueError('Cannot divide by zero!')
#   isinstance considers inheritance
#   if not (isinstance(x, (int, float))):
    if type(x) not in [int, float]:
        div_01 = x
#       print(f'\ndiv_01 == {div_01}')
        raise ValueError(f"Ernie_invalid literal for int() with base 10: '{div_01}'")
#   isinstance considers inheritance
#   if not (isinstance(x, (int, float))):
    if type(y) not in [int, float]:
        div_02 = y
#       print(f'\ndiv_02 == {div_02}')
        raise ValueError(f"Ernie_invalid literal for int() with base 10: '{div_02}'")
    return x / y

def get_joke():
    joke = 'No jokes'
    try:
        # Check to see if ( requests ) has been imported
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
    except NameError as e:
        print(f'\nget_joke() - Import Error: {e}')
        sys.exit('SystemExit Exception occurred')
    if response.status_code == 200:
        joke = response.json()['value']
    elif response.status_code == 301:
        joke = '301 - Permanent Redirect'
    elif response.status_code == 302:
        joke = '302 - Temporary Redirect'
    elif response.status_code == 401:
        joke = '401 - Unauthorized'
#       print(f'401 - joke == {joke}')
    elif response.status_code == 403:
        joke = '403 - Forbidden'
    elif response.status_code == 404:
        joke = '404 - Not Found'
    elif response.status_code == 410:
        joke = '410 - Gone'
    elif response.status_code == 500:
        joke = '500 - Internal Server Error'
    elif response.status_code == 502:
        joke = '502 - Bad Gateway'
    elif response.status_code == 503:
        joke = '503 - Service Unavailable'
    elif response.status_code == 504:
        joke = '504 - Gateway Timeout'
    else:
        joke = 'Unexpected ERROR!!'
    return joke

def is_weekday():
    time_now = datetime.datetime.now()
    print(f"\n'is_weekday()' datetime_now == {time_now}")
    weekday =  time_now.strftime('%A')
    day_num = time_now.weekday()
    print(f"'is_weekday()' day_num == {day_num} of Six")
    flag_weekday = False
    # Python datetime library ( 0 - 6 ) == ( Mpnday - Sunday )
    if day_num >= 0 and day_num < 5:
        flag_weekday = True
        display_name_weekday(weekday)
    else:
        display_name_weekend(weekday)
    print(f"'is_weekday()' flag_weekday == {flag_weekday}")
    return (flag_weekday)

def len_joke():
    joke = get_joke()
#   print(f"\nMocked Joke string from get_joke():\n'{joke}'")
    return len(joke)

def file_remove(correct_file_path):
#
# Any commented 'os.remove()' call may be uncommented for unittest test code debugging
#
#    os.remove(correct_file_path)
    if os.path.isfile(correct_file_path):
        incorrect_file_path = 'junk'
#        os.remove(incorrect_file_path)
        os.remove(correct_file_path)
    return

def get_random_int(modifier):
    roll = randint(1, 8)
    result = modifier + roll
#    print(f"'get_random_int' returned '{result}'")
    return result


def fizzbuzz(index=4):
    """Test_Fizz Buzz"""
    #
    try:
        # Check to see if ( sys ) has been imported
        func_name = sys._getframe().f_code.co_name
    except NameError as e:
        print(f'\ntest_fizz_buzz() - Import Error: {e}')
    display_OS_version()
#
    list_buzz = []
    list_fizz = []
    list_fizzbuzz = []
#
    fizz_actual_results = []
    buzz_actual_results = []
    fizzbuzz_actual_results = []
#
    fizz = []
    buzz = []
    first_num = []
    last_num = []
#
    tuple_fizz = (0, 7, 4, 4, 5)
    tuple_buzz = (7, 0, 6, 7, 7)
    tuple_first_num = (-44, -44, -36, -35, -35)
    tuple_last_num = (44, 44, 36, 35, 35)
#
    fizz.extend(tuple_fizz)
    buzz.extend(tuple_buzz)
    first_num.extend(tuple_first_num)
    last_num.extend(tuple_last_num)
#
    print(f"fizz_choices:{fizz}\nbuzz_choices:{buzz}\n"
    f"first_number_evaluated:{first_num}\nlast_number_evaluat4ed:{last_num}\n"
    f"current_index_of_choices:{index}") 
#
    if fizz[index] == 0:
        print(f"\nBAD value, fizz CANNOT be == '{fizz[0]}'")
        sys.exit('SystemExit Exception occurred')
    if buzz[index] == 0:
        print(f"\nBAD value, buzz CANNOT be == '{buzz[index]}'")
        sys.exit('SystemExit Exception occurred')
    for item in range(first_num[index], last_num[index] + 1):
        if item == 0:
            continue
        ### print(item)
        if item % fizz[index] == 0 and item % buzz[index] == 0:
            temp = f'{item} == FizzBuzz'
            list_fizzbuzz.append(temp)
            ### print(list_fizzbuzz)
        if item % fizz[index] == 0:
            temp = f'{item} == Fizz'
            list_fizz.append(temp)
            ### print(list_fizz)
        if item % buzz[index] == 0:
            temp = f'{item} == Buzz'
            list_buzz.append(temp)
            ### print(list_fizzbuzz)
    return list_fizz, list_buzz, list_fizzbuzz

def test_fizzbuzz():
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
        # return status_pass
        return
    return

def lambda_handler(event, context):
    # NOTE: Blank lines to 'stdout' will be suppressed
    test_fizzbuzz()
    is_weekday()
    return

def main():
    test_fizzbuzz()
    is_weekday()
    return

if __name__ == '__main__':
    main()
    sys.exit()

#EOF
