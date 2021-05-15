import yaml
from day_13 import *

if __name__ == "__main__":
    with open('config.yaml', 'r') as conf:
        config = yaml.safe_load(conf)

        emp_1 = Employee(**config['emp_1'])
        emp_2 = CustomerAssistant(**config['emp_2'])
        mngr_1 = Manager(**config['mngr_1'])
        store_manager_1 = StoreManager(**config['store_mngr_1'])
        store_607 = Store(**config['store_607'])



        print(emp_1)
        print(emp_2)
        print(mngr_1)
        print(store_manager_1)
        print(store_607)
