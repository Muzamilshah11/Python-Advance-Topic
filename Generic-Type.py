# This function will work for any type of object as long as it is passed as an argument. This is an example of polymorphism in Python.


from typing import TypeVar
T= TypeVar('T') #  Generic Type  (یعنی کوئی بھی قسم کا ڈیٹا لے سکتا ہے)

def magicbox(item:T) -> T:
    return item

print(magicbox("Pencil"))
print(magicbox(10))
print(magicbox(['Book','Pen','Color','Size',10,20]))

