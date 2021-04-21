import os
from contextlib import contextmanager

# cwd = os.getcwd()
# os.chdir('../../')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('venv__oop')
# print(os.listdir())
# os.chdir(cwd)

@contextmanager
def change_dir(destination: str):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('venv__oop'):
    print(os.listdir())