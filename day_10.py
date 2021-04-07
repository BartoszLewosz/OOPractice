from abc import ABC, abstractmethod

class Base:
    def foo(self):
        print("foo method from Base class")
        # raise NotImplementedError()

    def bar(self):
        print("bar method from Base class")
        # raise NotImplementedError()

class Concrete(Base): # instantiate/inherit from Base class
    def foo(self):
        print("foo method from Concrete(Base)")
        
b = Base()
# b.foo()
# b.bar()

c = Concrete()
c.foo()
c.bar()