class Employee:

    annual_payraise = 1.04

    def __init__(self, emp_id, name, start_date):
        self.emp_id = emp_id
        self.name = name
        self.start_date = start_date
    
    def show_full_data(self):
        return f"ID: {self.emp_id} \nName: {self.name} \nStart day: {self.start_date}"

    def meet_and_greet(self, words):
        return f"Welcome {self.name} {words}"

    @classmethod
    def set_annual_payraise(cls, amount):
        cls.annual_payraise = amount

    @staticmethod
    def show_birthday_msg(birthday_msg):
        return f"{birthday_msg}"

    # @staticmethod
    # def static_method(msg):
    #     return f"This is the {msg}"

emp_1 = Employee(101, "John", "01/03/2010")
# print(emp_1.static_method("static method message passed as an argument."))
print(Employee.show_birthday_msg("Whoop Whoop! It's your birthday!"))


class CustomerAssistant(Employee):
    def __init__(self, emp_id, name, start_date, week_hours):
        super().__init__(emp_id, name, start_date)
        self.week_hours = week_hours

emp_2 = CustomerAssistant(102, "Jane", "02/03/2010", 25)