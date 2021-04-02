class Employee:
    """ Creates an employee of company """

    annual_payraise = 1.04

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int):
        self.emp_id = emp_id
        self.name = name
        self.start_date = start_date
        self.pay = pay

    def show_full_data(self):
        return f"ID: {self.emp_id} \nName: {self.name} \nStart day: {self.start_date}"

    def meet_and_greet(self, words):
        return f"Welcome {self.name} {words}"

    @classmethod
    def set_annual_payraise(cls, amount) -> 'Employee':
        cls.annual_payraise = amount

    @staticmethod
    def show_birthday_msg(birthday_msg) -> str:
        return f"{birthday_msg}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.emp_id} - {self.name} - {self.start_date} - {self.pay})"


emp_1 = Employee(101, "John", "01/03/2010", 9.5)


class Manager(Employee):
    """ Creates a managing position of company """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int, employees=None):
        super().__init__(emp_id, name, start_date, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def show_employees_id(self):
        for e_id in self.employees:
            print(f"{e_id.emp_id}")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(emp_id: {self.emp_id}, Name: {self.name}, Start date: {self.start_date}, Pay: {self.pay}, Employees: {self.employees})"


mngr_1 = Manager(201, "Mark", "01/02/1999", 50000, [emp_1])


class StoreManager(Employee):
    """ Creates a store manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int):
        super().__init__(emp_1, name, start_date, pay)

    # __repr__ as Employee


class DeputyManager(Employee):
    """ Creates a deputy manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int):
        super().__init__(emp_1, name, start_date, pay)

    # __repr__ as Employee


class ShiftManager(Employee):
    """ Creates a shift manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int):
        super().__init__(emp_1, name, start_date, pay)

    # __repr__ as Employee


class CustomerAssistant(Employee):
    """ Creates a customer assistant """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int, week_hours: int):
        super().__init__(emp_id, name, start_date, pay)
        self.week_hours = week_hours

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(emp_id:{self.emp_id}, name:{self.name}, start_date:{self.start_date}, pay per hour:{self.pay}, week_hours:{self.week_hours})"


emp_2 = CustomerAssistant(102, "Jane", "02/03/2010", 9.5, 25)
