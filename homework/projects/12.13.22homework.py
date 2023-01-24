
import os
clear = lambda: os.system('cls')
clear()
from random import randint
class player:
    name = 0
    score = 0

    def __init__(this, name, score):
        this.name = name
        this.score = score

    def userfile(name):
        namefile = str(name)+'.txt'
        return namefile

    def wcsv(this, name, score):
        file = open(player.userfile(name.lower()), 'a')
        file.write(str(score) + '\n')
        file.close()

    def totalscore(name):
        total = 0
        with open(str(player.userfile(name.lower())), 'r') as inp:
            for line in inp:
                num = int(line)
                total += num
            return total
            
name = input('what is your name?: ')
clear()
useranswer = input('Rock, Paper, or Scissors?: ')
if useranswer.lower() == 'rock':
    answer = 1
elif useranswer.lower() == 'paper':
    answer = 2
elif useranswer.lower() == 'scissors':
    answer = 3
else:
    print("Sorry, looks like you didnt give a valid answer.")
    quit()

RNum = randint(1, 3)
score = 0
if RNum == 1:
    if answer == 1:
        print('It\'s a tie! Computer also chose rock.')
        nscore = score + 1
    elif answer == 2:
        print('You win! Computer chose rock, you chose paper.')
        nscore = score + 2
    elif answer == 3:
        print('You lose! Computer chose rock, you chose scissors.')
        nscore = score    
if RNum == 2:
    if answer == 1:
        print('You lose! Computer chose paper, you chose rock.')
        nscore = score
    elif answer == 2:
        print('It\'s a tie! Computer also chose paper.')
        nscore = score + 1
    elif answer == 3:
        print('You win! Computer chose paper, you chose scissors.')
        nscore = score + 2
if RNum == 3:
    if answer == 1:
        print('You win! Computer chose scissors, you chose rock.')
        nscore = score + 2
    elif answer == 2:
        print('You lose! Computer chose scissors, you chose paper.')
        nscore = score
    elif answer == 3:
        print('It\'s a tie! Computer also chose scissors.')
        nscore = score + 1

one = player(name, nscore)
two = one.wcsv(name, nscore)
print('Your total score is:', player.totalscore(name.lower()))