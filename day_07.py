class Celssius:
    def __init__(self, temperature):
        ''' The actual temperature value is stored in _temperature variable.
        The temperature attribute is a property object which provides 
        an interface to this private variable. '''
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

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

    temperature = property(get_temperature, set_temperature)

human = Celssius(37)
# print(human.get_temperature()) # this line had to change from temperature to get_temperature()
# print(human.to_fahrenheit())

print(Celssius.__init__.__doc__)