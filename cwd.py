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
def change_dir(destination):
    cwd = os.getcwd()
    os.chdir(destination)
    os.chdir(cwd)