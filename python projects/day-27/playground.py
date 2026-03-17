# def add(*args):
#     print(args)
#     print(type(args))
#     sum = 0
#     for num in args:
#         sum += num
#     return sum
#
# print(add(1,8,77,232))

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") #get metodu kullanırsan boşsa none atıyor.
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan")
print(my_car.color)


