
def getgroceryitem ():
    print("what do you need to buy?")
    item = input()
    return item

grocerylist = []

answer = "intial"

while len(answer) > 0:
    print("type in a new item to add it to the list or press enter to quit")
    answer = getgroceryitem()
    if answer != ' ':
        grocerylist.append(answer)

print(grocerylist)