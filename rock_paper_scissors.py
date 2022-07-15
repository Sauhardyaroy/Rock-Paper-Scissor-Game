import random

def gameWin(comp, you):

    if comp == you:
        return None

    elif comp== 'r':
        if you== 's':
            return False
        elif you== 'p':
            return True

    elif comp== 'p':
        if you== 'r':
            return False
        elif you== 's':
            return True

    elif comp== 's':
        if you== 'p':
            return False
        elif you== 'r':
            return True

print("computer turn : rock(r), paper(p), scizor(s)")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("your turn : rock(r), paper(p), scizor(s)")  
a = gameWin(comp, you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("game tied")
elif a:
    print("you win")
else:
    print("you lose")        
