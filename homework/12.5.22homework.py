import os
clear = lambda: os.system('cls')
clear()
class car:
    owner = 0
    age = 0
    miles = 0
    doors = 2
    wheels = 4


    def __init__(this, owner, age, miles, doors, wheels):
        this.owner = owner
        this.age = age
        this.miles = miles
        this.doors = doors
        this.wheels = wheels


DonaldsCar = car('Donald Martin', 2, 10000, 4, 4)
OliviasCar = car('Olivia Aguillon', 5, 46000, 4, 4)
DavidFromAccountingsCar = car("David Normalperson", 3, 32000, 2, 4)

cars = [DonaldsCar, OliviasCar, DavidFromAccountingsCar]

for car in cars:
    print(car.owner, "has a sweet ride")