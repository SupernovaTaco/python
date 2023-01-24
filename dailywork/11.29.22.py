import os
clear = lambda: os.system('cls')
from random import choice, randint
clear()
def clearfiletest():
    filename = "test.csv"
    f = open(filename, 'w')
    f.close
def getrandnum():
    randnum = randint(1,1000)
    return str(randnum)
def getrandname():
    names = ['ricky','bob','jill','jack','joe','Liam','Olivia','Noah','Emma','Oliver','Charlott','Elijah','Amelia','James','Ava','William','Sophia','Benjamin','Isabella','Lucas','Mia','Henry','Evelyn','Theodore','Harper']
    return choice(names)
clearfiletest()
x = 0
while (x < 25):
    x += 1
    f = open("test.csv", "a")
    f.write(getrandname() + "," + getrandnum() + "," + getrandnum() + "," + getrandnum() + "," + getrandnum() + "," + getrandnum() + "\n")
    f.close()
class bills:
    def __init__(this, name, phone, house, electric, water, food):
        this.name = name
        this.phone = phone
        this.house = house
        this.electric = electric
        this.water = water
        this.food = food

    def total(this):
        return this.phone + this.house + this.electric + this.water + this.food

def savetofile(name, total):
    filename = 'total.txt'
    f = open(filename, 'a')
    f.write(name + ": " + str(total) + "\n")
    f.close()

def clearfile():
    filename = 'total.txt'
    f = open(filename, 'w')
    f.close()

clearfile()
f = open("test.csv", "r")
numberlines = len(f.readlines())
print(len(f.readlines()))
f.seek(0,0)
startingline = 0
runningtotal = 0
recprocc = 0
while startingline < numberlines:
    line = f.readline()
    line = line.strip()
    #print(line)

    pie = line.split(',')
    cleanpies=[]
    for pi in pie:
        cleanpies.append(pi.strip())
    
    if str(cleanpies[1]).isdigit():
        userbills = bills(cleanpies[0], int(cleanpies[1]), int(cleanpies[2]), int(cleanpies[3]), int(cleanpies[4]), int(cleanpies[5]),)
        print(userbills.name, userbills.total())
        savetofile(userbills.name, userbills.total())
        runningtotal += int(userbills.total())
        recprocc += 1
    
        
    
    '''print(userbills.electric)
    for p in pie:
        p = p.strip()
        print(p)'''

    startingline += 1
print("records processed: ", recprocc)
print("running total: ", runningtotal)
