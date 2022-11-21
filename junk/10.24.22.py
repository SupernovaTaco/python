
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



names = ("joe")


def namecheck (username):
    if username in names:
        return True
    else:
        return False

def login ():
    print("enter user name: ")
    userinput = input()
    return userinput

user = login()
validuser = namecheck(user)
while validuser == False:
    print("have a nice day")
    user = login()
    validuser = namecheck(user)

print("joe MAMA")

print("what is your name?")
name = input()

def isjoemama():
    if name == "joe":
        return True
    else:
        return False

if isjoemama == False:
    print("have a nice day.")
if isjoemama == True:
    print("joe MAMA")'''

    

nameiskosta = True
if nameiskosta:
    print("getroasted")


 



