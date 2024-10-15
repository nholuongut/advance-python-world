class Vehicle:
    can_fly = False
    number_of_weels = 0


class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color: str):
        self.color = color


my_car = Car("red")
print(my_car.__dict__)
print(type(my_car).__dict__)


# lookup2.py
class Vehicle:
    can_fly = False
    number_of_weels = 0


class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color: str):
        self.color = color


my_car = Car("red")

print(my_car.__dict__["color"])
print(type(my_car).__dict__["number_of_weels"])
print(type(my_car).__base__.__dict__["can_fly"])
