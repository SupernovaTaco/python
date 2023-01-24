import os
clear = lambda: os.system('cls')

userfile = input("enter the name of the file you would like to create or add to: ")
f = open(userfile, "a")

def userinput():
    userinput = input("what would you like to add? ")
    f.write(userinput+"\n")

def askForItems():
    print("How many items do you have to add to your list")
    itemCount = input()
    if itemCount.isdigit():
        return int(itemCount)
    else:
        print("Looks like you had an error, valid inputs are numbers.")
        askForItems()

numberOfReceiptItems = 0
itemsEntered = 0

numberOfReceiptItems = askForItems()

while numberOfReceiptItems > 0 and itemsEntered < numberOfReceiptItems:
    itemsEntered += 1
    clear()
    print("Enter your line item", "(",itemsEntered,"/",numberOfReceiptItems,")")
    
    userinput()
    
clear()
f.close()
file1 = open(userfile, "r")
print(file1.read())
