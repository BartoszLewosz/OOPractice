import pytest
from day_13 import *


class TestClassEmployee:
    @pytest.fixture
    def emp_1(self):
        emp_1 = Employee(101, 'John', '01/02/2016', 2016, 9.5)
        return emp_1

    @pytest.fixture
    def mngr_1(self, emp_1):
        mngr_1 = Manager(202, 'Daniel', '12/12/12', 2010, 11.5, [emp_1])
        return mngr_1

    def test_correctness_of_Employee_attributes(self, emp_1):
        #Employee(emp_id, name, start_date, start_year, pay)
        assert emp_1.emp_id == 101
        assert emp_1.name == 'John'
        assert emp_1.start_date == '01/02/2016'
        assert emp_1.start_year == 2016
        assert emp_1.pay == 9.5

    def test_correctness_of_Manager_attributes(self, mngr_1):
        # Manager(emp_id, name, start_date, start_year, pay)
        assert mngr_1.emp_id == 202
        assert mngr_1.name == 'Daniel'
        assert mngr_1.start_date == '12/12/12'
        assert mngr_1.start_year == 2010
        assert mngr_1.pay == 11.5

    def test_use_headset(self, emp_1):
        assert emp_1.use_headset(
            'message from emp_1') == "John says on headset: 'message from emp_1'"

    def test_if_emp_1_is_subordinate_to_mngr_1(self, emp_1, mngr_1):
        assert emp_1 in mngr_1.employees == [emp_1]
