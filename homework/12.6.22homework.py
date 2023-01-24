import os
clear = lambda: os.system('cls')
clear()
class car:
    owner = 0
    age = 0
    miles = 0
    condition = 0
    Baseprice = 0

    def __init__(this, owner, age, miles, Condition, Baseprice):
        this.owner = owner
        this.age = age
        this.miles = miles
        this.Condition = Condition
        this.Baseprice = Baseprice

    def FindValue(this, age, miles, condition, baseprice):
            NewCon = int(condition)/100
            NewP = int(baseprice)*NewCon
            newage = int(age) * 500
            newNewP = NewP - newage
            newnewNewP = newNewP - int(miles) * 0.01
            fournewp = round(newnewNewP, 2)
            return fournewp - 1000
        
#DonaldsCar = car('Donald Martin', 2, 75, 40000)
#OliviasCar = car('Olivia Aguillon', 5, 90, 35000)
#DavidFromAccountingsCar = car("David Normalperson", 3, 40, 25000)
name = input("(1/5) What is your name?: ")
age = input("(2/5) How old is your car?: ")
miles = input("(3/5) how many miles has your car traveled?: ")
cond = input("(4/5) what is the condition of your car? (1 - 100): ")
BPrice = input("(5/5) What was the price of your car brand new?: ")


one = car(name, age, miles, cond, BPrice)
two = one.FindValue(age, miles, cond, BPrice)
print("your name is", name, "and your car is worth", two, "$")