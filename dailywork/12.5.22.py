from random import choice, randint
def clearfile():
    filename = "test.csv"
    f = open(filename, 'w')
    f.close
def getrandnum():
    randnum = randint(1,1000)
    return str(randnum)
def getrandname():
    names = ['ricky','bob','jill','jack','joe','Liam','Olivia','Noah','Emma','Oliver','Charlott','Elijah','Amelia','James','Ava','William','Sophia','Benjamin','Isabella','Lucas','Mia','Henry','Evelyn','Theodore','Harper']
    return choice(names)
clearfile()
x = 0
while (x < 25):
    x += 1
    f = open("test.csv", "a")
    f.write(getrandname() + "," + getrandnum() + "," + getrandnum() + "," + getrandnum() + "," + getrandnum() + "," + getrandnum() + "\n")
    f.close()