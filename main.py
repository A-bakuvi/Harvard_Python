"""import random
import sys
import cowsay


def rock_paper_scissors():
    time = 3
    myScores = 0
    scores = 0
    score = 0
    myScore = 0


    while True:
        inp = input("rock,paper, or scissors?")
        moves = ["rock","paper","scissors"]
        myMove = random.choice(moves)
        if inp in moves:
            if inp == moves:
                print ("equal")
            elif inp == "rock" and myMove == "scissors":
                print("you won!") 
                score+=1
            elif inp == "paper" and myMove == "rock":
                print("you won!") 
                score+=1
            elif inp == "scissors" and myMove == "paper":
                print("you won!") 
                score+=1
            elif inp == "rock" and myMove == "paper":
                print("you lost")
                myScore+=1
            elif inp == "paper" and myMove == "scissors":
                print("you lost")
                myScore+=1
            elif inp == "scissors" and myMove == "rock":
                print("you lost")
                myScore+=1
        else:
            print("wrong input")

#also make a def time()            
        time -= 1
        print(time,"moves left")
        if time == 0:
            if score<myScore:
                print ("you lost,try again")
                myScores+=1
                print("computer =",myScores, "you = ",scores)
                break
            else:
                print("you won!")
                scores+=1
                print("computer =",myScores, "you = ",scores)
                break
            
            if myScore == 0 and score == 5:
                queestions()

def questions():

    computer_scores = 0
    print("question1")
    user_input = input("A,B,C,D?")
    print(a(user_input,computer_scores))

    print("question2")
    user_input = input("A,B,C,D?")
    print(b(user_input,computer_scores))

    print("question3")
    user_input = input("A,B,C,D?")
    print(d(user_input,computer_scores))

    print("question4")
    user_input = input("A,B,C,D?")
    print(c(user_input,computer_scores))

    print("question5")
    user_input = input("A,B,C,D?")
    print(c(user_input,computer_scores))

    print("question6")
    user_input = input("A,B,C,D?")
    print(a(user_input,computer_scores))

    print("question7")
    user_input = input("A,B,C,D?")
    print(b(user_input,computer_scores))

    print("question8")
    user_input = input("A,B,C,D?")
    print(d(user_input,computer_scores))

    print("question8")
    user_input = input("A,B,C,D?")
    print(c(user_input,computer_scores))

    print("question8")
    user_input = input("A,B,C,D?")
    print(a(user_input,computer_scores))


def a(user_input,computer_scores):
    question_scores = 0
    computer_scores = 0
    if user_input == "A":
        question_scores += 1 
        if question_scores >= 8 and computer_scores <= 2:
            cowsay.trex("you won!")
            sys.exit()
        return question_scores
    else:
        computer_scores +=1
        return computer_scores


def b(user_input,computer_scores):
    question_scores = 0
    if user_input == "B":
        question_scores += 1 
        if question_scores >= 8 and computer_scores <= 2:
            cowsay.trex("you won!")
            sys.exit()
        return question_scores
    else:
        computer_scores += 1
        return computer_scores
    

def c(user_input,computer_scores):
    question_scores = 0
    if user_input == "C":
        question_scores += 1 
        if question_scores >= 8 and computer_scores <= 2:
            cowsay.trex("you won!")
            sys.exit()
        return question_scores
    else:
        computer_scores += 1
        return computer_scores
    

def d(user_input, computer_scores):
    question_scores = 0
    if user_input == "D":
        question_scores += 1 
        if question_scores >= 8 and computer_scores <= 2:
            cowsay.trex("you won!")
            sys.exit()
        return question_scores
    else:
        computer_scores += 1
        return computer_scores




if __name__ == "__main__":
   questions()

make levels where if the player has won rounds without losing (once you have fixed the problem) then take him to the challenge where
you ask random questions about anything you want and if they win grant them the ultimate animal trophy using cowsay. And do this in another
file with open and .txt. use defA,B,C,D for doing the questions
"""

"""import random
import cowsay

def get_user_choice():
    return input("Enter your choice (rock/paper/scissors): ").lower()

def generate_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def display_scores(user_score, computer_score):
    print(f"Your score: {user_score}, Computer's score: {computer_score}")

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = generate_computer_choice()
        print("Computer chooses", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "You win!" in result:
            user_score += 1
        elif "Computer wins!" in result:
            computer_score += 1
        display_scores(user_score, computer_score)
        if user_score == 5:
            break
    if user_score == 5:
        print("Ready for the quiz?")
        planet_quiz()

def planet_quiz():
    questions = {
        "What is the largest planet in our solar system?": "jupiter",
        "Which planet is known as the 'Red Planet'?": "mars",
        "What is the hottest planet in our solar system?": "venus",
        "Which planet has the most moons?": "jupiter",
        "What is the smallest planet in our solar system?": "mercury",
        "Which planet has the most rings?": "saturn",
        "Which planet is known as the 'Morning Star' or 'Evening Star'?": "venus",
        "Which planet is closest to the Sun?": "mercury",
        "What is the farthest planet from the Sun in our solar system?": "neptune",
        "Which planet has the fastest rotation?": "jupiter"
    }
    correct_answers = 0
    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer:
            correct_answers += 1
    if correct_answers >= 8:
        print(cowsay.trex("Congratulations, you have won the game!!!"))

def main():
    play_game()

if __name__ == "__main__":
    main()"""

import random
import cowsay
import sys

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    x = input("Enter your choice (rock/paper/scissors): ").lower()
    if x in choices:
        return x
    else:
        print("Enter the correct input (rock/paper/scissors)")
        sys.exit()

def generate_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def display_scores(user_score, computer_score):
    print(f"Your score: {user_score}, Computer's score: {computer_score}")

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = generate_computer_choice()
        print("Computer chooses", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if "You win!" in result:
            user_score += 1
        elif "Computer wins!" in result:
            computer_score += 1
        display_scores(user_score, computer_score)
        if user_score == 5 :
            break
        if computer_score == 3:
            print("you lost,try again")
            sys.exit()
    if user_score == 5 and computer_score <= 2:
        print("Ready for the quiz?")
        planet_quiz()

def planet_quiz():
    questions = {
        "What is the largest planet in our solar system?": "jupiter",
        "Which planet is known as the 'Red Planet'?": "mars",
        "What is the hottest planet in our solar system?": "venus",
        "Which planet has the most moons?": "jupiter",
        "What is the smallest planet in our solar system?": "mercury",
        "Which planet has the most rings?": "saturn",
        "Which planet is known as the 'Morning Star' or 'Evening Star'?": "venus",
        "Which planet is closest to the Sun?": "mercury",
        "What is the farthest planet from the Sun in our solar system?": "neptune",
        "Which planet has the fastest rotation?": "jupiter"
    }
    correct_answers = 0
    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer:
            correct_answers += 1
    if correct_answers >= 8:
        print(cowsay.trex("Congratulations, you have won the game!!!"))

def main():
    play_game()

if __name__ == "__main__":
    main()

                    






