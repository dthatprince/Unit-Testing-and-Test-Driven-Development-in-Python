from pytest import raises

'''
# fails 
def raisesValueException():
    pass
    
'''

# passes
def raisesValueException():
    raise ValueError


def test_exception():
    with raises(ValueError):
        raisesValueException()