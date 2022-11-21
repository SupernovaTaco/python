'''class personA:
    age = 41
    height = 68
    Name = "leonard"
    Lname = "aguillon"

person = personA()
print(person.Name, person.Lname)

class personb:
    def _init_(self, age, name, height):
        self.age = age
        self.name = name
        self.height = height

person1 = personb(41, "leonard", 68)
if (person.age < 21):
    print(personb.name , "is old enough to drink")

person2 = personb(33, "olivia", 60)


class bills:
    def __init__(self, rent, electric, water, gas, phone):
        self.rent = rent
        self.electric = electric
        self.water = water
        self.gas = gas
        self.phone = phone



    def total(self):
        return(self.rent + self.electric + self.water + self.gas + self.phone)

    def yearlytotal(self):
        return self.total() * 12


donaldbills = bills(1350, 250, 100, 0, 115)
donaldstotal = donaldbills.total()
print(donaldbills)
print(donaldstotal)'''
x = 100
while x > 1:
    file = open("notes.txt", "r")
    print(file.read())