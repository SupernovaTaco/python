'''
from filecmp import cmp
from math import ceil, floor


absolutevalue = abs(-7)
print(absolutevalue)

ceilvalue = ceil(99.87) #ceil always pushes float to next full number
print(ceilvalue)

floorvalue = floor(99.99) #floor pushes float to previous full number
print(floorvalue)

comparevalue = cmp(1, 2) #outputs true/false depending on if the numbers are the same 
print(comparevalue)

def printme (str):
    print (str)
    return

printme("imsocool")

def multiply (intA, intB):
    answer = intA * intB
    print(answer)
    return answer


x = multiply(92, 10)
print(round(x,-3))


''''''
from math import pi


users = {"leo" : "leonard aguillon" , "bolis" : "olivia aguillon" , "bee" : "livier aguillon", "SupernovaTaco" : "Donald Martin"}

def greetuser (username):
    fullname = users[username]
   # print(fullname)
    return fullname

name = greetuser("SupernovaTaco")
print ("Welcome " + name + "!") 


print(pi)
print(round(pi,100000))


print("enter the password")
password = input()




names = {"leo" : "leonard aguillon" , "bolis" : "olivia aguillon" , "bee" : "livier aguillon", "taco" : "donald martin"}

def namecheck (username):
    if username in names:
        return True
    else:
        return False

def getuser (username):
    fullname = names[username]
    return fullname


def login ():
    print("enter user name: ")
    userinput = input()
    return userinput

user = login()
validuser = namecheck(user)
while validuser == False:
    print("The username provided does not match any in our database. Please try again.")

validuser = namecheck(user)
print("hello, " + getuser(user))
 '''


names = {"leo" : "leonard aguillon" , "bolis" : "olivia aguillon" , "bee" : "livier aguillon", "taco" : "donald martin"}

def namecheck (username):
    if username in names:
        return True
    else:
        return False

def getuser (username):
    fullname = names[username]
    return fullname


def login ():
    print("enter user name: ")
    userinput = input()
    return userinput

user = login()
validuser = namecheck(user)
while validuser == False:
    print("The username provided does not match any in our database. Please try again.")
    user = login()
    validuser = namecheck(user)

print("welcome, " + getuser(user)) 









