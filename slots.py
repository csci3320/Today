"""Python data types with a fixed size"""
i = 1 # See also bool, byte, float, and complex

""" Example of a class with a fixed size"""

class Criminal:
    __slots__ = "gender", "hobby"
    def __init__(self):
        self.gender = "Male"
    

Bob = Criminal()
Bob.hobby = "Swimming"
# Bob.hair_color = "Black"

print(Bob.gender)
print(Bob.hobby)

"""Example of linear data types"""

name = "Prince Humperdinck"

numbers = set([1,2,3,1]) #See also list, tuple, range, bytearray, and frozenset
print(numbers)

favorites = dict(Dad="Key Lime Pie", Mom="Apple")
print(favorites)
