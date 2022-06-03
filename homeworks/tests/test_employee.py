import unittest
from mock import patch,Mock
from employee import *


class Test_Employee(unittest.TestCase):
    
    def setUp(self) -> None:
        self.employee = Employee(1,12,1000)
        super().setUp()
    
    @patch("requests.get")
    def test_monthly_schedule(self,request):       
        
        request.return_value = Mock(ok=True,text="hi")        
        self.assertEqual(self.employee.monthly_schedule(2),"hi")
        
        request.return_value = Mock(ok=False,text="hi")        
        self.assertEqual(self.employee.monthly_schedule(2),"Bad Response!")
        
    
    def test_apply_raise(self):
        pay = self.employee.pay=100
        self.employee.apply_raise()
        expected =int(pay*self.employee.raise_amt)
        self.assertEqual(self.employee.pay,expected,"apply_raise fail")
        
        
        pay = self.employee.pay=200
        self.employee.raise_amt=1.1
        self.employee.apply_raise()
        expected =int(pay*self.employee.raise_amt)
        self.assertEqual(self.employee.pay,expected,"case 2 apply_raise fail")
        
        
    def test_email(self):
        self.assertEqual(self.employee.email,'{}.{}@email.com'.format(self.employee.first, self.employee.last))
        
    def test_fullname(self):
        self.assertEqual(self.employee.fullname,'{} {}'.format(self.employee.first, self.employee.last))