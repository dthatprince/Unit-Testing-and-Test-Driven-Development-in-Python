import pytest


@pytest.mark.test1
def test1():
    print("\n Test1!")
    assert True

# cmd line arguments
# 1.  pytest -v -s : finds all tests and executes them

# 2. pytest -v -s test_cmd_line_args_1.py : only runs test1

# 3. pytest -v -s testSubDirectory/ : executes only tests in the subdirectory

# 4. pytest -v -s -k "test2" : keyword to run only test2

# 5. pytest -v -s -k "test2 or test3" : keyword to run only test2 and test3

# 6. pytest -v -s -m "test1 or test3" : run only test1 and test3 using mark expression
