from itertools import islice
class Fib:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

# f = Fib()
# print(list(islice(f, 2, 20)))

def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev + curr

f = fib()
f2 = islice(f, 0, 10)
f3 = list(islice(f, 0, 10))
print(type(f))
print(f)
print(type(f2))
print(f2)
print(type(f3))
print(f3)
