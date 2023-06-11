import pytest

from Checkout import Checkout

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

'''
# Can create instance of Checkout Class
def test_CanInstantiateCheckout():
    co = Checkout()

# Can create instance of Checkout Class
# can add item price
def test_CanAddItemPrice(checkout):
    checkout.addItemPrice("a", 1)

# can add item
def test_CanAddItem(checkout):
    checkout.addItem("a")
'''

# can calculate the current total
def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1


# can add multiple items and get correct total
def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

# can add discount rules
def test_canAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)


# @pytest.mark.skip
# can apply discount rules to the total
def test_canApplyDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2



def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("c")


