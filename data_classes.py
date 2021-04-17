from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

pos_1 = Position('Oslo', 10.8, 59.9)
pos_2 = Position('somewhere')

print(pos_1)
print(pos_2)
