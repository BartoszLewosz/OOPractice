import pytest
from day_13 import *

@pytest.fixture
def emp_1():
    emp_1 = Employee(101, 'John', '01/02/2016', 2016, 9.5)
    return emp_1

@pytest.fixture
def mngr_1():
    mngr_1 = Manager(202, 'Daniel', '12/12/12', 2010, 11.5, [emp_1])
    return mngr_1


def test_use_headset(emp_1):
    assert emp_1.use_headset('message from emp_1') == "John says on headset: 'message from emp_1'"
    
def test_if_emp_1_is_subordinate_to_mngr_1(emp_1, mngr_1):
    assert emp_1 in mngr_1.employees == [emp_1]