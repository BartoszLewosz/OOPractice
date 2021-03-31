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

    # @staticmethod
    # def static_method(msg):
    #     return f"This is the {msg}"


emp_1 = Employee(101, "John", "01/03/2010", 9.5)
# print(emp_1.static_method("static method message passed as an argument."))
print(Employee.show_birthday_msg("Whoop Whoop! It's your birthday!"))


class Manager(Employee):
    """ Creates a managing position of company """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int, employees = None):
        super().__init__(emp_id, name, start_date, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees


mngr_1 = Manager(201, "Mark", "01/02/1999", 50000, [emp_1])
print(mngr_1.show_full_data())
print(mngr_1.employees[0])


class StoreManager(Employee):
    """ Creates a store manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int):
        super().__init__(emp_1, name, start_date, pay)


class DeputyManager(Employee):
    """ Creates a deputy manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int):
        super().__init__(emp_1, name, start_date, pay)


class ShiftManager(Employee):
    """ Creates a shift manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int):
        super().__init__(emp_1, name, start_date, pay)


class CustomerAssistant(Employee):
    """ Creates a customer assistant """

    def __init__(self, emp_id: int, name: str, start_date: str, pay: int, week_hours: int):
        super().__init__(emp_id, name, start_date, pay)
        self.week_hours = week_hours


emp_2 = CustomerAssistant(102, "Jane", "02/03/2010", 9.5, 25)
