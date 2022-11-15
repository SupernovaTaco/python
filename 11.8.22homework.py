import random
import os
clear = lambda: os.system('cls')

clear()

traits = ("health", "damage", "armor", "lifesteal", "stamina", "poison resist", "fire resist")
tplnum={}


    
    
def trplusnumb():
        
    def randtrait():
        randtrait = random.choice(tuple(traits))
        
        
            
        return randtrait
    randnum = random.randint(1,1000)
    tplnum[randnum] = randtrait()
    return randnum
            
        
def repeat3():
    x = 3   
    clear()
    for _ in range(x):
        trplusnumb()
    print (tplnum)

    user = input("do you want to start/reroll? (y or n) ")
    if user == "y":
        tplnum.clear()
        repeat3()
    else:
        quit
        
    
repeat3()









