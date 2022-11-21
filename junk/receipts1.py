import os
clear = lambda: os.system('cls')
numreceipts = 0
clear()


print('Enter correct username and password combo to continue')
count=0
loggedin = 0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='admin123' and username=='admin123':
        print('Welcome!')
        loggedin += 1
    else:
        print('Access denied. Try again.')
        count += 1
else: print('No more attempts!') 
    



def askreceiptcount():
    print("How many receipts?")
    numofreceipts = input()
    if numofreceipts.isdigit():
        return int(numofreceipts)
    else:
        askreceiptcount()

numbers = []
def getreceipt():
    print("enter receipt:")
    receipt = input()
    if (len(receipt) <= 0):
        print("Invalid Name")
        getreceipt()
    else:
        numbers.append(receipt)

def getrecs():
    while len(numbers) < numreceipts:
        getreceipt()
    print(numbers)

for val in numbers:
    sum = sum+val
sum = 0
#print("The sum is", sum)
