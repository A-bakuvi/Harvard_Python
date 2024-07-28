import random
z = 0
a = 0
inp = input("level: ")
while not inp.isdigit() or int(inp)<=0:
    inp = input("level: ")
z = int(inp)

x = random.randint(1,z)
y = input("Guess: ")
while not y.isdigit() or int(y) <= 0:
    y = input("Guess: ")
#if y.isdigit():
  #  a = int(y)
a = int(y)
while True:
    if a == x:
        print("Just Right!")
        break
    elif a<x :
        print("Too small!")
    else:
        print("Too large!")
    y = int(input("Guess: "))
    while not y.isdigit() or int(y) <= 0:
        y = input("Guess: ")
    a = int(y)


































































































































"""import random
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass



while True:
    try:
        guess = int(input("Guess: "))
        if level >= guess > 0:
            randomno = random.randint(1,level)
            if level >=guess < randomno:
                print("Too small!")
            elif level >= guess > randomno:
                print("Too Large!")
            else:
                print("Just right!")
                break
        elif not guess in range():
            pass
        elif not guess.isdigit():
            pass
        else:
            pass
    except (ValueError,TypeError):
        pass"""