import os, time
clear = lambda: os.system('cls')
clear()

class calculator:
    label = ''
    stitch_count = 0
    price_per_1000 = 0
    price_per_color = 0
    color_count = 0
    hooping_price = 0

    def __init__(this, label, stitch_count, price_per_1000, price_per_color, color_count, hooping_price): #constructor
        #hidden values are: time_value, price_per_1000, price_per_color, hooping_price
        this.label = label
        this.stitch_count = stitch_count
        this.price_per_1000 = price_per_1000
        this.price_per_color = price_per_color
        this.color_count = color_count
        this.hooping_price = hooping_price

    def calculate_cost(this):
        stitch_price = round((this.stitch_count/1000)* float(this.price_per_1000), 0)
        total = float(this.hooping_price) + (this.color_count * float(this.price_per_color)) + stitch_price

        return total

    def calculate_digitze_cost(time_spent, hourly_rate):
        return time_spent * hourly_rate

    def read_list_function(filename, listform = bool): #reads the file and if 2nd perameter is false makes a list of the raw lines and if it is true it makes each line into a list
        if listform == False: #reads the CSV file and returns a list with all the lines
            f = open(filename, 'r')
            dirty_list = f.readlines()
            clean_list = []
            for x in dirty_list:
                clean_list.append(x.replace("\n", ""))
            clear()
            return clean_list
        elif listform == True: #reads the given file and turns every line into a list within much larger list
            f = open(filename, 'r')
            whole_file = []
            for line in f:
                line_list = []
                pieces = line.split(',')
                for p in pieces:
                    line_list.append(p.strip())
                whole_file.append(line_list)

            return whole_file


try: #tries to open necesarry files and if it has an issue it makes new ones and gives default values
    f = open('stitch_calculator.csv', 'r')
    f.close()
    calculator_hidden_values = calculator.read_list_function('stitch_calculator_values.csv', False)

except:
    f = open('stitch_calculator.csv', 'w')
    f.close()
    f = open('stitch_calculator_values.csv', 'w')
    f.write('1' + '\n' + '0.50' + '\n' + '5' + '\n' + '20')
    calculator_hidden_values = calculator.read_list_function('stitch_calculator_values.csv', False)
    f.close()

while True:

    clear()
    main_menu = input('[1] - calculate new design\n[2] - read prices\n[3] - delete a design\n[4] - change hidden values\n[10] - exit program\n--> ')

    if main_menu == '1': #calculate new design
        while True:
            clear()
            calculator_hidden_values = calculator.read_list_function('stitch_calculator_values.csv', False)
            label = input('please label your design or press enter to return to main menu: ')
            if label == '':
                clear()
                break
            stitch_count = int(input('how many stitches are in your design?: '))
            color_count = int(input('how many colors are in your design?: '))
            digitize_input = input('did you digitize the design yourself? [y/n]: ')
            if digitize_input == 'y':
                time_spent = input('how many hours did you spend working on this design?: ')
                design_cost = calculator.calculate_digitze_cost(time_spent, calculator_hidden_values[3])
            else:
                design_cost = input('what did you pay for the design?: ')


            value_input = calculator(label, stitch_count, calculator_hidden_values[0], calculator_hidden_values[1], color_count, calculator_hidden_values[2])
            total = value_input.calculate_cost()
            print('your design will cost', round(total, 2), '$')
            confirm = input('is this correct? [y/n]: ')

            if confirm == 'y':
                f = open('stitch_calculator.csv', 'a')
                f.write(str(value_input.label) + ', ' + str(round(total, 2)) + ', ' + str(value_input.stitch_count) +', ' + str(calculator_hidden_values[0]) +', ' + str(calculator_hidden_values[1]) +', ' + str(value_input.color_count) +', ' + str(calculator_hidden_values[2]) + '\n')
                f.close()
                print('task succesfully added')
                time.sleep(0.75)
            else:
                print('task not added')
                time.sleep(0.75)
                 
    elif main_menu == '2': #read prices
        file = calculator.read_list_function('stitch_calculator.csv', False)
        for line in file:
            print(line)
        input('press enter to continue: ')

    elif main_menu == '3': #delete a design

        clear()

        delete_list = calculator.read_list_function('stitch_calculator.csv', False)
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
                f = open('stitch_calculator.csv', 'w')
                for line in delete_list:
                    f.write(str(line) + '\n')
                f.close()
            else:
                print('Not a valid input!')
                time.sleep(1)

    elif main_menu == '4': #change hidden values
        while True:
            hidden_values_list = calculator.read_list_function('stitch_calculator_values.csv', False)
            print('cost per 1,000 stitches -', hidden_values_list[0])
            print('cost per color -', hidden_values_list[1])
            print('hooping cost -', hidden_values_list[2])
            print('hourly rate for digitizing -', hidden_values_list[3])

            edit_choice = input('\n[1] - change cost per 1000 stitches\n[2] - change cost per color\n[3] - change hooping cost\n[4] - change hourly rate for digitizing\n[enter] - return to main menu\n--> ')
            

            if edit_choice == '1':
                new_value = input('what would you like to change the value to?\n--> ')
                try:
                    float(new_value)
                    hidden_values_list[0] = new_value
                    f = open('stitch_calculator_values.csv', 'w')
                    for item in hidden_values_list:
                        f.write(item + '\n')
                    f.close()
                except:
                    print('not a valid input!')
                    time.sleep(0.75)

            elif edit_choice == '2':
                new_value = input('what would you like to change the value to?\n--> ')
                try:
                    float(new_value)
                    hidden_values_list[1] = new_value
                    f = open('stitch_calculator_values.csv', 'w')
                    for item in hidden_values_list:
                        f.write(item + '\n')
                    f.close()
                except:
                    print('not a valid input!')
                    time.sleep(0.75)

            elif edit_choice == '3':
                new_value = input('what would you like to change the value to?\n--> ')
                try:
                    float(new_value)
                    hidden_values_list[2] = new_value
                    f = open('stitch_calculator_values.csv', 'w')
                    for item in hidden_values_list:
                        f.write(item + '\n')
                    f.close()
                except:
                    print('not a valid input!')
                    time.sleep(0.75)

            elif edit_choice == '4':
                new_value = input('what would you like to change the value to?\n--> ')
                try:
                    float(new_value)
                    hidden_values_list[3] = new_value
                    f = open('stitch_calculator_values.csv', 'w')
                    for item in hidden_values_list:
                        f.write(item + '\n')
                    f.close()
                except:
                    print('not a valid input!')
                    time.sleep(0.75)

            elif edit_choice == '':
                clear()
                break

            else:
                print('not a valid input!')
                time.sleep(0.75)

    elif main_menu == '10': #exit the program
        clear()
        quit()
    