def evaljoemama(name):
    if name == "joe":
        return True
    else:
        return False

print("what is your name?")
name = input()
isjoemama = evaljoemama(name)

if isjoemama == False:
    print("have a nice day.")
if isjoemama == True:
    print("joe MAMA")