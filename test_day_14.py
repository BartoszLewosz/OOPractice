import pytest
from day_13 import *

@pytest.fixture
def emp_1():
    emp_1 = Employee(101, 'John', '01/02/2016', 2016, 9.5)
    return emp_1

def test_use_headset(emp_1):
    assert emp_1.use_headset('message from emp_1') == "John says on headset: 'message from emp_1'"
    