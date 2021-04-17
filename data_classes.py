from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

pos_1 = Position('Oslo', 10.8, 59.9)

print(pos_1)
