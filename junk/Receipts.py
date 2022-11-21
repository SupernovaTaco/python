
#Homework

#Bonus item - keep the screen clean (google)

#Require proper login, 3 attempts - if failed, exit app with a message like "Unable to login at this time."
#Receipt calculator - Ask the user for the amounts, Take in x amount of receipts. 
#Print receipts taken in line by line, sort list by least expensive to most expensive, $xx.xx 
#When done, display the rounded total, $xxxx 


#Begin Login portion of homework 
'''
print('Enter username and password to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='admin123' and username=='receipt_admin':
        print('Welcome!')
        break
    else:
        print('Access denied. Try again.')
        count += 1
else: print('Hacker! No more tries!')
'''
#End Login portion of homework 
import os
clear = lambda: os.system('cls')
import hashlib

def askForItems():
    print("How many items do you have to add to your list")
    itemCount = input()
    if itemCount.isdigit():
        return int(itemCount)
    else:
        print("Looks like you had an error, valid inputs are numbers.")
        askForItems()

print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    username = str(hashlib.sha256(username.encode('utf-8')).hexdigest())
    password = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
    if password == "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9" and username == "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9":
        print('Welcome!')
        isAuthenticated = True
        break
    else:
        print('Access denied. Try again.')
        count += 1
else:
    print(
'''
                                                                                                                     
 @@@@@@    @@@@@@@   @@@@@@@  @@@@@@@@   @@@@@@    @@@@@@      @@@@@@@   @@@@@@@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@  
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@      @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  !@@       !@@       @@!       !@@       !@@          @@!  @@@  @@!       @@!@!@@@  @@!  @@!       @@!  @@@  
!@!  @!@  !@!       !@!       !@!       !@!       !@!          !@!  @!@  !@!       !@!!@!@!  !@!  !@!       !@!  @!@  
@!@!@!@!  !@!       !@!       @!!!:!    !!@@!!    !!@@!!       @!@  !@!  @!!!:!    @!@ !!@!  !!@  @!!!:!    @!@  !@!  
!!!@!!!!  !!!       !!!       !!!!!:     !!@!!!    !!@!!!      !@!  !!!  !!!!!:    !@!  !!!  !!!  !!!!!:    !@!  !!!  
!!:  !!!  :!!       :!!       !!:            !:!       !:!     !!:  !!!  !!:       !!:  !!!  !!:  !!:       !!:  !!!  
:!:  !:!  :!:       :!:       :!:           !:!       !:!      :!:  !:!  :!:       :!:  !:!  :!:  :!:       :!:  !:!  
::   :::   ::: :::   ::: :::   :: ::::  :::: ::   :::: ::       :::: ::   :: ::::   ::   ::   ::   :: ::::   :::: ::  
 :   : :   :: :: :   :: :: :  : :: ::   :: : :    :: : :       :: :  :   : :: ::   ::    :   :    : :: ::   :: :  :  
                                                                                                                   
'''
)
    quit()

clear()


print(
'''
   ___              _      __    _____     __         __     __          
  / _ \___ _______ (_)__  / /_  / ___/__ _/ /_____ __/ /__ _/ /____  ____
 / , _/ -_) __/ -_) / _ \/ __/ / /__/ _ `/ / __/ // / / _ `/ __/ _ \/ __/
/_/|_|\__/\__/\__/_/ .__/\__/  \___/\_,_/_/\__/\_,_/_/\_,_/\__/\___/_/  
                  /_/                                                    

'''
    )
numberOfReceiptItems = 0
itemsEntered = 0

numberOfReceiptItems = askForItems()
receiptList = []

while numberOfReceiptItems > 0 and itemsEntered < numberOfReceiptItems:
    print("Enter your line item")
    item = input()
    receiptList.append(item)
    itemsEntered += 1
convertedList = list(map(float, receiptList ))  
totaledList = sum(convertedList)
sortTotaledList = sorted(convertedList)
print(sortTotaledList)
print('Total Items Equal: ' + str(totaledList))


