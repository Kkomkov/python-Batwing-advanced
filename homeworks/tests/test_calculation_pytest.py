from ast import Add
from functions_to_test import Calculator
import pytest

def test_add():
    assert Calculator.add(1,2)==3
    
def test_substract():
    assert Calculator.subtract(7,1)==6
    assert Calculator.subtract(0,1)==-1
    
def test_multiply():
    assert Calculator.multiply(2,3)==2*3
    assert Calculator.multiply(2,0)==0
    
def test_divide():
    assert Calculator.divide(2,3)==2/3
    with pytest.raises(ValueError, match="Can not divide by zero!"):
        Calculator.divide(2,0)