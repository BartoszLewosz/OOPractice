class Employee:
    def __init__(self, emp_id: int, name: str):
        self.emp_id = emp_id
        self.name = name
        self._training = {
            'topic_1': False,
            'topic_2': False
        }
    def __repr__(self):
        return f"{self.emp_id}, {self.name}, {self.training_dict}"
    
    @property
    def training(self):
        print("getting value...")
        return self._training

    @training.setter
    def training(self, topic_and_result):
        print("setting Value...")
        topic, result = topic_and_result.split(' ')
        self._training[topic] = True
    
emp_1 = Employee(101, "John")
emp_1.training = 'topic_1 True'
print(emp_1.training)