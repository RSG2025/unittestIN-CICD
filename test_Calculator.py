import pytest
from Calculator import add,subs
#class TestCalculator(unittest.TestCase):
def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_subtract():
    assert subs(5,3) == 2
    assert subs(10,20) == 10
    