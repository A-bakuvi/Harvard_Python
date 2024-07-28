import random
def main():
    level = get_level()

    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = 0
        for _ in range(3):
            print(x,"+",y,"= ", end = "")
            answer = input("")
            correct_answer += 1
            if answer.isdigit() and int(answer) == x+y:
                score = score + 1
                break

            elif not answer.isdigit() or int(answer) != x+y:
                print("EEE")

            if correct_answer == 3:
                print(x,"+",y,"=",x+y)
    print ("Score: " ,score)
def generate_integer(level):
        if level == 1:
            a = random.randint(0,9)

        elif level == 2:
            a = random.randint(10,99)

        elif level == 3:
            a = random.randint(100,999)
        else:
            raise ValueError
        return a
# returns int value for level

def get_level():
    int_level = 0
    while True:
        try:
            level = input("level: ")
            if level.isdigit() and int(level) in [1,2,3]:
                int_level = int(level)
                return int_level
        except:
            pass


if __name__ == "__main__":
    main()


#convert to functions
#check for any wrong conditions






















































"""import random
def main():
#level = input("level: ")
    z = 0
    while True:
        try:
            level = input("level: ")
            if level.isdigit() and int(level) in [1,2,3]:
                z = int(level)
                break
        except:
            pass

    for _ in range(10):
        correct_answer = 0
        score = 0
        x = 0
        y = 0
        if z == 1:
            x = random.randint(0,9)
            y = random.randint(0,9)

        elif z == 2:
            x = random.randint(10,99)
            y = random.randint(10,99)

        elif z == 3:
            x = random.randint(100,999)
            y = random.randint(100,999)

        else:
            raise ValueError

        for _ in range(3):
            print(x,"+",y,"= ")
            answer = input("answer: ")
            correct_answer += 1

            if answer == x+y:
                print(x,"+",y,"=",x+y)
                score += 1

            elif not answer.isdigit() or answer != x+y:
                print("EEE")

            if correct_answer == 3:
                print(x,"+",y,"= ",x+y)
    print ("Score: " ,score)

if __name__ == "__main__":
    main()"""

# error in correct answer
#convert to functions
#check for any wrong conditions