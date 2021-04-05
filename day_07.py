class Celssius:
    def __init__(self, temperature):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter
    def get_temperature(self):
        print("getting temperature...")
        return self._temperature # '_' in Python means to set as private - not accesible from outside the class

    # setter
    def set_temperature(self, value):
        print("setting temperature...")
        if value < -273.15:
            raise ValueError("It's impossible!!")
        self._temperature = value

human = Celssius(-37)

print(human.to_fahrenheit())