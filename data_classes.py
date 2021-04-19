from dataclasses import dataclass, field, fields
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    name: str
    #lon: float = 0.0
    lon: float = field(default= 0.0, metadata={'unit': 'degrees'}, repr=False)
    lat: float = field(default= 0.0, repr=False)

    def distance_to(self, other):
        r = 6371
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2 + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


oslo = Position('Oslo', 10.8, 59.9)
vancouver = Position('V', -123.1, 49.3)
pos_1 = Position('Oslo', 10.75, 59.91)
pos_2 = Position('somewhere')
gdansk = Position('Gdansk', 54.35, 18.64)
krakow = Position('Krakow', 50.06, 19.94)
print(pos_1)
print(pos_2)
# print(krakow.distance_to(gdansk))
print(fields(Position))

