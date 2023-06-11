import pytest


@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\n Setup Module 2")


@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\n Setup Session 2")


@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\n Setup Function 2")


class TestClass:
    def test_it(self):
        print("Executing test1")
        assert True

    def test_it2(self):
        print("Executing test2")
        assert True
