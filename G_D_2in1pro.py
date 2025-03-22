from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar('T') # Generic type

@dataclass
class Magicbox(Generic[T]):
    data: T
box1 = Magicbox(10)
box2 = Magicbox([1,2,3,4,5,6,7,8,9,"hello", "world"])
box3 = Magicbox("Collection of Bookes")

print(f"{box1}\n{box2}\n{box3}")


