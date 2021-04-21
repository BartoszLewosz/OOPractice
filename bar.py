from foo import *
print(f"Hello from {__name__}!")

def funcA():
    print("funcA from bar.py")

if __name__=='__main__':
    print(f"Hello from {__name__}!!!!")