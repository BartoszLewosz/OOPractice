from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self):
        self.abs_atr = 10

    @abstractmethod
    def foo(self):
        print("foo method from Base class")
        # raise NotImplementedError()

    @abstractmethod
    def bar(self):
        print("bar method from Base class")
        # raise NotImplementedError()

    @property
    @abstractmethod
    def add_abs_attr(self):
        return self.abs_atr + 8


class Concrete(Base):
    def __init__(self):
        super().__init__()
        self.sub_attr = 20  # instantiate/inherit from Base class

    def foo(self):
        print("foo method from Concrete(Base)")

    def bar(self):
        print("bar method from Concrete(Base)")

    @property
    def add_abs_attr(self):
        return self.abs_atr + 1

    def add_sub_attr(self):
        return self.sub_attr + 2


# b = Base()
# b.foo()
# b.bar()

c = Concrete()
c.foo()
c.bar()
print(c.abs_atr)
print(c.sub_attr)
print(c.add_abs_attr)
print(c.add_sub_attr())
