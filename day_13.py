from abc import ABC, abstractmethod
import datetime
from dataclasses import dataclass
from contextlib import contextmanager


def uppercare(func):
    def wrapper(*args, **kwargs):
        original_method = func(*args, **kwargs)
        modified_method = original_method.upper()
        return modified_method
    return wrapper


def headset(func):
    def wrapper(*args):
        orignal_output = func(*args)
        name, message = orignal_output.split('says: ')
        new_output = name + 'says on headset: ' + message
        return new_output
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

    @headset
    def use_headset(self, message: str) -> str:
        return f"{self.name} says: '{message}'"

    def write_message(self, recipient: str, content: str):
        message_file = f"message_number_{GroupChatMessage.msg_number}_" + \
            f"from_{self.name}_to_{recipient}.txt"

        with GroupChatMessage(message_file, 'w') as msg:
            msg.write(content)

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
mngr_2 = Manager(202, 'Daniel', '12/12/12', 2010, 11.5, [emp_1])


class StoreManager(Employee):
    """ Creates a store manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int):
        super().__init__(emp_id, name, start_date, start_year, pay)

    # __repr__ as Employee


class DeputyManager(Employee):
    """ Creates a deputy manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int):
        super().__init__(emp_id, name, start_date, pay)

    # __repr__ as Employee


class ShiftManager(Employee):
    """ Creates a shift manager of company """

    def __init__(self, emp_id: int, name: str, start_date: str, start_year: int, pay: int):
        super().__init__(emp_id, name, start_date, start_year, pay)

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


@dataclass(frozen=True)
class Store:
    store_id: int
    store_manager: StoreManager
    open_in_year: int


class GroupChatMessage:

    msg_number = 0

    def __init__(self, message_name: str, mode: str):
        self.message_name = message_name
        self.mode = mode

    def __enter__(self):
        self.msg = open(self.message_name, self.mode)
        self.__class__.msg_number += 1
        return self.msg

    def __exit__(self, exc_type, exc_val, traceback):
        if self.msg:
            self.msg.close()


# with GroupChatMessage('extra_shift.txt', 'w') as msg:
#     msg.write("Who wants extra shift??")
emp_1.write_message('All', 'Hello everybody! Im new here!')

print(GroupChatMessage.msg_number)
#
# @contextmanager
# def group_chat_message(file, mode):
#     msg = open(file, mode)
#     try:
#         yield msg
#     finally:
#         msg.close()

# with group_chat_message('sample_def.txt', 'w') as msg:
#     msg.write("Test message using context manager as function.")

#

emp_2 = CustomerAssistant(102, "Jane", "02/03/2010", 2020, 9.5, 25)
mngr_1.training = 'introduction True'
emp_3 = ShiftManager(203, 'Dan', '12/23/2014', 2014, 28000)
store_manager_1 = StoreManager(501, "Chris", '11/12/11', 2010, 70000)

new_store = Store(607, store_manager_1, 1987)
message1 = "Hello everyone!"
emp_1.write_message('All', message1)
print(mngr_2.employees)

Employee.set_annual_payraise(1.06)
print(Employee.annual_payraise)
