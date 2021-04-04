class Celssius:
    def __init__(self, temperature=0): # temperature becomes a dictionary 
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


human = Celssius()

human.temperature = 37

print(human.temperature)
print(human.to_fahrenheit())
print(human.__dict__)