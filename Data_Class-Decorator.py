from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Person:
    N_language: ClassVar['str'] = "Urdu"
    Region: ClassVar['str'] = "Pakistan"
    name: str
    age: int

    def introduce(self) -> str:
        return f"Hello, my name is {self.name} and I am {self.age} years old. My National Language is {self.N_language} and I am from {self.Region}"
    
    def walk(self) -> str:
        return f"{self.name} is walking"
    
    @staticmethod
    def national_language():
        return Person.N_language
    @staticmethod
    def resident_region():
        return Person.Region
    

object1 = Person("Ali", 20)
print(object1.introduce())
print(object1.walk())
print(Person.national_language())
print(Person.resident_region())

