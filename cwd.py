import os

cwd = os.getcwd()
os.chdir('../../')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('venv__oop')
print(os.listdir())
os.chdir(cwd)

print(cwd)