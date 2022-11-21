
def getgroceryitem ():
    item = input("what do you need to buy?: ")
    return item

grocerylist = []

answer = "intial"

while len(answer) > 0:
    print("type in a new item to add it to the list or press enter to quit")
    answer = getgroceryitem()
    if answer != ' ':
        grocerylist.append(answer)

print(grocerylist)