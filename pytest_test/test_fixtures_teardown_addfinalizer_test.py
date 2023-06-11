import pytest

@pytest.fixture()
def setup1():
    print("\n Setup 1")
    yield
    print("\n Teardown 1")

@pytest.fixture()
def setup2(request):
    print("\n Setup 2")

    def teardown_a():
        print("\n Teardown A")

    def teardown_b():
        print("\n Teardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing test1")
    assert True

def test2(setup2):
    print("Executing test2")
    assert True



'''

The example code uses Pytest fixtures to set up and tear down resources for testing.

It defines two fixtures named setup1 and setup2, and two tests named test1 and test2.

test1 uses setup1, while test2 uses setup2.

setup1 specifies its teardown code using the yield keyword. The code after the yield statement is executed after the test function completes.

setup2 specifies two teardown functions (teardown_a and teardown_b) using the addfinalizer method. These functions are executed after the test function completes.

Pytest fixtures are a powerful way to set up and tear down resources for testing, and they can help keep test code organized and maintainable.

'''