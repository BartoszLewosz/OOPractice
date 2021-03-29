class Employee:
    def __init__(self, emp_id, name, start_date):
        self.emp_id = emp_id
        self.name = name
        self.start_date = start_date
    
    def show_full_data(self):
        return f"ID: {self.emp_id}\nName: {self.name}\nStart day: {self.start_date}"

emp_1 = Employee(101, "John", "01/03/2010")

print(emp_1.show_full_data())

