import random
def gameWin(comp,you):
    if comp==you:
        return None
    elif comp == "s":
        if you == "g":
            return False
        elif you == "w":
            return True
    elif comp == "g":
        if you == "w":
            return False
        elif you == "s":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True

print("comp turn: Snake(s) Water(w) Gun(g)")     
randnumber = random.randint(1,3)  
if randnumber == 1:
    comp = 's' 
elif randnumber==2:
    comp = 'w'
elif randnumber==3:
    comp = 'g'

you = input("your turn: Snake(s) Water(w) Gun(g)")
a = gameWin(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("the game is tie!")
elif a:
    print("you win!")
else:
    print("you lose!")