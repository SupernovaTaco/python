import os, time
from datetime import datetime
clear = lambda: os.system('cls')
clear()

class checklist: #class
    description = ''
    status = False
    completed_date = 0


    def __init__(this, description, status, completed_date): #constructor
        this.description = description
        this.status = status
        this.completed_date = completed_date


    def read_list_function(filename, listform = bool): #reads the file and if 2nd perameter is false makes a list of the raw lines and if it is true it makes each like into a list
        #reads the CSV file and returns a list with all the lines
        if listform == False:
            f = open(filename, 'r')
            dirty_list = f.readlines()
            clean_list = []
            for x in dirty_list:
                clean_list.append(x.replace("\n", ""))
            clear()
            return clean_list
        elif listform == True:
            #reads the given file and turns every line into a list within much larger list
            f = open(filename, 'r')
            whole_file = []
            for line in f:
                line_list = []
                pieces = line.split(',')
                for p in pieces:
                    line_list.append(p.strip())
                whole_file.append(line_list)

            return whole_file

    def remove_list_elements(listed_line): #reverses checklist.read_list_function('x', True)
        finished_line = ', '.join(map(str, listed_line))
        return finished_line

#start program
current_time = datetime.now()
unix_time = (time.mktime(current_time.timetuple()))
try: #checks if file exists and removes old completed items
    old_list = checklist.read_list_function('checklist_save_data.csv', True)
    for line in old_list:
        if line[2] == 'incomplete':
            pass
        elif int(float(line[2])) < (unix_time - 604800):
            old_list.remove(line)
    f = open('checklist_save_data.csv', 'w')
    for line in old_list:
        fixed_line = checklist.remove_list_elements(line)
        f.write(fixed_line + '\n')
    f.close()
except: #if program has issue opening the file, it creates a new one
    f = open('checklist_save_data.csv', 'w')
    f.close()

while True: #main loop
    clear()
    main_menu = input('[1] - read checklist\n[2] - read only incomplete items\n[3] - read only complete items\n[4] - mark an item as complete\n[5] - delete an item\n[6] - add an item\n[7] - exit the program\n--> ')
    
    if main_menu == '1': #read all
        for line in checklist.read_list_function('checklist_save_data.csv', False):
            print(line)
        input('press enter to continue: ')

    if main_menu == '2': #read incomplete
        clear()
        x = 0
        y = 0
        for line in checklist.read_list_function('checklist_save_data.csv', True):
            x += 1
            if line[1] == 'complete=False':
                y += 1
                print(checklist.remove_list_elements(line).replace('\n', ''))
        print(x - y, 'ommited items')
        input('press enter to continue: ')
            
    if main_menu == '3': #read complete
        clear()
        x = 0
        y = 0
        for line in checklist.read_list_function('checklist_save_data.csv', True):
            x += 1
            if line[1] == 'complete=True':
                y += 1
                print(checklist.remove_list_elements(line).replace('\n', ''))
        print(x - y, 'ommited items')
        input('press enter to continue: ')

    if main_menu == '4': #mark item as complete
        clear()

        while True:
            delete_list = checklist.read_list_function('checklist_save_data.csv', False)
            completed = []
            clear()
            x = 0
            for line in delete_list:
                x += 1
                print(x, '-', line)
            user_delete_choice = input('Enter the line number of the item you would like to complete, or press enter to stop completing items: ')
            delete_list_lines = len(delete_list)
            
            if user_delete_choice == '':
                break
            elif user_delete_choice.isdigit() == False:
                print('Not a valid input!')
                time.sleep(0.75)
            elif int(user_delete_choice) <= delete_list_lines and int(user_delete_choice) > 0:
                whole_file = checklist.read_list_function('checklist_save_data.csv', True)
                items = whole_file[int(user_delete_choice) - 1]
                
                if items[1] == 'complete=False':
                    items[1] = 'complete=True'
                    items[2] = str(unix_time)
                    whole_file.remove(whole_file[int(user_delete_choice) - 1])
                    whole_file.append(items)
                    f = open('checklist_save_data.csv', 'w')
                    for line in whole_file:
                        line_data = checklist.remove_list_elements(line)
                        f.write(line_data + "\n")
                    f.close()
                
            else:
                print('Not a valid input!')
                time.sleep(0.75)

    if main_menu == '5': #delete item
        clear()

        delete_list = checklist.read_list_function('checklist_save_data.csv', False)
        while True:
            clear()
            x = 0
            for line in delete_list:
                x += 1
                print(x, '-', line)
            user_delete_choice = input('Enter the line number of the item you would like to delete, or press enter to stop deleting items: ')
            delete_list_lines = len(delete_list)
            
            if user_delete_choice == '':
                break
            elif user_delete_choice.isdigit() == False:
                print('Not a valid input!')
                time.sleep(0.75)
            elif int(user_delete_choice) <= delete_list_lines and int(user_delete_choice) > 0:
                delete_list.remove(delete_list[int(user_delete_choice) - 1])
                f = open('checklist_save_data.csv', 'w')
                for line in delete_list:
                    f.write(str(line) + '\n')
                f.close()
            else:
                print('Not a valid input!')
                time.sleep(1)

    if main_menu == '6': #add new item
        clear()
        while True:
            clear()
            taskname = input('Label your task or press enter to return to main menu: ')
            if taskname == '':
                break
            else:
                clear()
                f = open('checklist_save_data.csv', 'a')
                print(str(taskname) + ', complete=False, ' + 'incomplete')
                user_confirm = input('Is this correct? [y/n]: ')
                if user_confirm == 'y':
                    clear()
                    f.write(str(taskname) + ', complete=False, ' + 'incomplete' + '\n')
                    print('Added task!')
                    time.sleep(0.75)
                else:
                    clear()
                    print('Task not added')
                    time.sleep(0.75)
                f.close()

    if main_menu == '7': #clear and quit
        clear()
        quit()