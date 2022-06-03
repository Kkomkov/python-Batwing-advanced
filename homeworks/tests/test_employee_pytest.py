from employee import *
import requests_mock

def test_monthly_schedule(requests_mock):
    employee = Employee(1,12,1000)
    month=2
    url = f"http://company.com/{employee.last}/{month}"
    requests_mock.get(url,status_code=200,text="textx")
    assert employee.monthly_schedule(month)=="textx"
    
    
    requests_mock.get(url,status_code=404,text="aaa")
    assert employee.monthly_schedule(month)=='Bad Response!'