from abc import ABC, abstractmethod
import datetime


def uppercare(func):
    def wrapper(*args, **kwargs):
        original_method = func(*args, **kwargs)
        modified_method = original_method.upper()
        return modified_method
    return wrapper


class Employee:
    """ Creates an employee of company """

    annual_payraise = 1.04

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int):
        self.emp_id = emp_id
        self.name = name
        self.start_date = start_date
        self.start_year = start_year
        self.pay = pay
        self._training = {
            'introduction': False,
            'health_&_safety': False,
            'customer_service': False
        }

    # getter
    @property
    def training(self):
        # print("getter...")
        return self._training

    @training.setter
    def training(self, topic_and_result):
        # print("setting Value...")
        topic, result = topic_and_result.split(' ')
        self._training[topic] = True

    @property
    def age(self) -> int:
        now = datetime.datetime.now().year
        return now - self.start_year

    @uppercare
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


emp_1 = Employee(101, "John", "01/03/2010", 2000, 9.5)


class Manager(Employee):
    """ Creates a managing position of company """

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int, employees=None):
        super().__init__(emp_id, name, start_date, start_year, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def show_employees_id(self):
        for e_id in self.employees:
            print(f"{e_id.emp_id}")

    def refund(self):
        print(f"{self.name} is doing refund.")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(emp_id: {self.emp_id}, Name: {self.name}, Start date: {self.start_date}, Pay: {self.pay}, Employees: {self.employees})"


mngr_1 = Manager(201, "Mark", "01/02/1999", 50000, [emp_1])


class StoreManager(Employee):
    """ Creates a store manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int):
        super().__init__(emp_1, name, start_date, start_year, pay)

    # __repr__ as Employee


class DeputyManager(Employee):
    """ Creates a deputy manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int):
        super().__init__(emp_1, name, start_date, pay)

    # __repr__ as Employee


class ShiftManager(Employee):
    """ Creates a shift manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int):
        super().__init__(emp_1, name, start_date, pay)

    # __repr__ as Employee


class CustomerAssistant(Employee):
    """ Creates a customer assistant """

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int, week_hours: int):
        super().__init__(emp_id, name, start_date, start_year, pay)
        self.week_hours = week_hours

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(emp_id:{self.emp_id}, name:{self.name}, start_date:{self.start_date}, pay per hour:{self.pay}, week_hours:{self.week_hours})"

    def refund(self):
        print(f"{self.name} is doing refund.")


def do_refund(thing):
    try:
        thing.refund()
    except (AttributeError, TypeError) as e:
        print(e)


class Skill(ABC):
    '''Creates employee's skill. This an abstract class Skill'''

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @property
    @abstractmethod
    def describe_skill(self):
        pass

    @abstractmethod
    def use_skill(self):
        pass

    @abstractmethod
    def show_full_skill(self):
        pass

    def __repr__(self):
        return (
            f"{self.__class__.__name__}\n"
            f"Name of the skill: {self.name}\n"
            f"Description: {self.description}"
        )


class Delivery(Skill):
    def __init__(self, name: str, description: str, difficulty: str = 'Normal'):
        super().__init__(name, description)
        self.difficulty = difficulty

    @property
    def describe_skill(self) -> str:
        return(f"{self.name} - This skill show that you can do delivery in efficient and correct way.")

    def use_skill(self):
        print(f"Using skill: {name}")

    @property
    def show_full_skill(self):
        return (
            f"{self.__class__.__name__}\n"
            f"Skill: {self.name}\n"
            f"Description: {self.description}\n"
            f"Difficulty: {self.difficulty}"
        )


emp_2 = CustomerAssistant(102, "Jane", "02/03/2010", 2020, 9.5, 25)
mngr_1.training = 'introduction True'

skill_1 = Delivery(
    'Fruit and veg', 'The standard is 15 min per pallet', 'Hard')
# print(skill_1.describe_skill)
# print(skill_1.difficulty)

print(skill_1.show_full_skill)
# from abc import ABC, abstractmethod


# class Base(ABC):
#     def __init__(self):
#         self.abs_atr = 10

#     @abstractmethod
#     def foo(self):
#         print("foo method from Base class")
#         # raise NotImplementedError()

#     @abstractmethod
#     def bar(self):
#         print("bar method from Base class")
#         # raise NotImplementedError()

#     @property
#     @abstractmethod
#     def add_abs_attr(self):
#         return self.abs_atr + 8


# class Concrete(Base):
#     def __init__(self):
#         super().__init__()
#         self.sub_attr = 20  # instantiate/inherit from Base class

#     def foo(self):
#         print("foo method from Concrete(Base)")

#     def bar(self):
#         print("bar method from Concrete(Base)")

#     @property
#     def add_abs_attr(self):
#         return self.abs_atr + 1

#     def add_sub_attr(self):
#         return self.sub_attr + 2


# # b = Base()
# # b.foo()
# # b.bar()

# c = Concrete()
# c.foo()
# c.bar()
# print(c.abs_atr)
# print(c.sub_attr)
# print(c.add_abs_attr)
# print(c.add_sub_attr())
