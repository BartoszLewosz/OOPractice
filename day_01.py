class Employee:

    annual_payraise = 1.04

    def __init__(self, emp_id, name, start_date):
        self.emp_id = emp_id
        self.name = name
        self.start_date = start_date
    
    def show_full_data(self):
        return f"ID: {self.emp_id} \nName: {self.name} \nStart day: {self.start_date}"

emp_1 = Employee(101, "John", "01/03/2010")

print(emp_1.show_full_data())
print("Annual payrise:" + str(emp_1.annual_payraise))

class CustomerAssistant(Employee):
    def __init__(self, emp_id, name, start_date, week_hours):
        super().__init__(emp_id, name, start_date)
        self.week_hours = week_hours

emp_2 = CustomerAssistant(102, "Jane", "02/03/2010", 25)
print(emp_2.show_full_data())
print(emp_2.week_hours)
print("Annual payrise:" + str(emp_2.annual_payraise))