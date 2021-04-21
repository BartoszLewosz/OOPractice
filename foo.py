print("before import")
import math

print("before funcA")
def funcA():
    print("funcA...")

print("before funcB")
def funcB():
    print(f"FuncB {math.sqrt(100)}")

print("Before __name__ guard")
if __name__=='__main__':
    funcA()
    funcB()
print("After __name__ guard")