import unittest
from functions_to_test import Calculator
 
class TestForCalculator_A(unittest.TestCase):
    
    def test_add(self):
        method_message =f"fail {Calculator.add.__doc__}"
        self.assertEqual(Calculator.add(1,2),3,method_message)
        self.assertEqual(Calculator.add(1,-1),0,method_message)

    def test_substract(self):
        method_message =f"fail {Calculator.subtract.__doc__}"
        self.assertEqual(Calculator.subtract(2,1),1,method_message)
        self.assertEqual(Calculator.subtract(0,10),0-10),method_message
    
    def test_multiply(self):
        method_message =f"fail {Calculator.subtract.__doc__}"
        self.assertEqual(Calculator.multiply(2,1),1*2,method_message)
        self.assertEqual(Calculator.multiply(0,100),0*10,method_message)
        self.assertEqual(Calculator.multiply(-1,-1),-1*-1,method_message)
        self.assertEqual(Calculator.multiply(0,0),0*0,method_message)
        
    def test_divide(self):
        method_message =f"fail {Calculator.divide.__doc__}"
        self.assertEqual(Calculator.divide(2,1),2/1,method_message)
       
        self.assertEqual(Calculator.divide(-1,-1),-1/-1,method_message)
        
        self.assertRaises(ValueError, Calculator.divide,10,0)
