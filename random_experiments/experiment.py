from functools import total_ordering

@total_ordering
class Dog:

    def __init__(self, age):
        self.age = age
    
    def __eq__(self, other):
        if isinstance(other, Dog):
            return other.age == self.age 
        return False

    def __lt__(self, other):
        if isinstance(other, Dog):
            return other.age > self.age 
        return False

dog1 = Dog(4)
dog2 = Dog(6)

print(dog1 < dog2) #True
print(dog1 <= dog2) #True
print(dog1 > dog2) #False
print(dog1 != dog2) #True
print(dog1 == dog2) #False
