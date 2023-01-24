import os
import time
import random
clear = lambda: os.system('cls')
clear()
class Contact:
    ID = None
    First_name = None
    Last_name = None
    Phone_number = None
    Address = None
    
    def __init__(this, id, First_name, Last_name, Phone_number, Address):
        this.ID = id
        this.First_name = First_name
        this.Last_name = Last_name
        this.Phone_number = Phone_number
        this.Address = Address

    def Generate_ID():
        f = open('Phonebook.csv','r')
        for item in f:
            y = random.randint(10000,99999)
            if str(y) in item:
                y == random.randint(10000,99999)
        f.close()
        return y

    def Write_to_csv(this, id, First_name, Last_name, Phone_number, Address):
        f = open('Phonebook.csv','a')
        f.write(str(id) + ', ' + str(First_name) + ', ' + str(Last_name) + ', ' + str(Phone_number) + ', ' + str(Address) + '\n')
        f.close()
        
def Evaluate_User_action():
    clear()
    User_action = input('what would you like to do? \n[R] - read\n[A] - add new contact\n[X] - remove contacts from list\n[CLS] - clear the phonebook of all contacts (use with extreme caution!)\n[EXIT] - save and exit the program\n--> ')

    if User_action == 'r':
        clear()
        print('READMODE')
        f = open('Phonebook.csv','r')
        Read_Phonebook = f.read()
        print(Read_Phonebook)
        f.close()
        input('press enter to continue: ')
        
    elif User_action == 'a':
        clear()
        First_name = input('What is the FIRST name of the person you want to add to the phone book?: ')
        Last_name = input('What is the LAST name of the person you want to add to the phone book?: ')
        Phone_number = input('What is their phone number? (1234567890): ')
        Address = input('What is their address? (1223 examplestreet): ')
        id = Contact.Generate_ID()
        
        if '-' not in Phone_number or ',' not in Phone_number:
            phone_number_list = []
            for character in Phone_number:
                phone_number_list.append(character)
            phone_number_list.insert(3, '-')
            phone_number_list.insert(7, '-')
            merge_phone_number = ''.join(map(str,phone_number_list))

        clear()
        print('first name, last name, phone number, address\n\nsuggested addition:', First_name, Last_name, merge_phone_number, Address)
        User_confirmation = input('Are you sure you want to add this contact? [Y/N]: ')
        if User_confirmation.lower() == 'y':
            one = Contact(id, First_name, Last_name, merge_phone_number, Address)
            two = one.Write_to_csv(id, First_name, Last_name, merge_phone_number, Address)
            clear()
            print('contact successfully added!')
            time.sleep(1.5)
        elif User_confirmation.lower() == 'n':
            clear()
            print('contact successfully canceled!')
            time.sleep(1.5)

    elif User_action == 'x':
        User_delete_choice = input('what is the ID of the contact you would like to delete?: ')
        File_list = []
        f = open('Phonebook.csv','r')
        for item in f:
            File_list.append(item)
        new_list = [item for item in File_list if User_delete_choice not in item]
        for item in new_list:
            str(item).replace('\n','')
            
        f.close()
        f = open('Phonebook.csv','w')
        for item in new_list:
            f.write(str(item))
        f.close()
        clear()
        print('Contact successfully deleted!')
        time.sleep(1.5)

    elif User_action == 'exit':
        clear()
        print('quitting...')
        quit()        
    
    elif User_action == 'cls':
        User_confirm_delete = input('please type "CONFIRM" to delete all contacts\n--> ')
        if User_confirm_delete == 'CONFIRM':
            f = open('Phonebook.csv','w')
            f.write('ID, First name, Last name, Phone number, Address\n')
            f.close()
            clear()
            print('File successfully cleared!')
            time.sleep(1.5)
    else:
        print('Oops! looks like you didnt give a valid answer. Please try again.')
        time.sleep(1.5)

while True:
    Evaluate_User_action()