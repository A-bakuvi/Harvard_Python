import random
import cowsay
import sys

print("")
print("Welcome to the game rock/paper/scissors. In this game you will be playing against the computer. If you win 3 times you will enter a quiz which will be made of 10 questions. If you get 8 or more right you will win. If you lose to the computer, well, you can always play again!")

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
        if user_score == 3:
            break
        if computer_score == 3:
            print(cowsay.stegosaurus("you lost,try again"))
            retry1 = input("Do you want to retry? (yes/no) ").lower()
            if "yes" in retry1:
                print("")
                print("Welcome to the game rock/paper/scissors. In this game you will be playing against the computer. If you win 3 times you will enter a quiz which will be made of 10 questions. If you get 8 or more right you will win. If you lose to the computer, well, you can always play again!")
                play_game()
            elif "no" in retry1:
                print("Well thank you for playing, see you later!")
                sys.exit()
            else:
                sys.exit()
    if user_score == 3 and computer_score <= 2:
        print(cowsay.dragon("Great job, you won against the computer, now time for the quiz!"))
        print("Ready for the quiz?")
        planet_quiz()

def planet_quiz():
    questions = {
        "What is the largest planet in our solar system? ": "jupiter",
        "Which planet is known as the 'Red Planet'? ": "mars",
        "What is the hottest planet in our solar system? ": "venus",
        "Which planet has the most moons? ": "jupiter",
        "What is the smallest planet in our solar system? ": "mercury",
        "Which planet has the most rings? ": "saturn",
        "Which planet is known as the 'Morning Star' or 'Evening Star'? ": "venus",
        "Which planet is closest to the Sun? ": "mercury",
        "What is the farthest planet from the Sun in our solar system? ": "neptune",
        "Which planet has the fastest rotation? ": "jupiter"
    }
    correct_answers = 0
    for question, answer in questions.items():
        user_answer = input(question).lower()
        if user_answer == answer:
            correct_answers += 1
    if correct_answers >= 8:
        print(cowsay.trex("Arggh! Congratulations, you have won the game!!!"))
        sys.exit()
    else:
        print(cowsay.daemon(f"You answered {correct_answers} questions correct but you needed 8 to pass"))
        retry = input("Do you want to retry? (yes/no) ").lower()
        if "yes" in retry:
            print("")
            print("Welcome to the game rock/paper/scissors. In this game you will be playing against the computer. If you win 3 times you will enter a quiz which will be made of 10 questions. If you get 8 or more right you will win. If you lose to the computer, well, you can always play again!")
            play_game()
        elif "no" in retry:
            print("Well thank you for playing, see you later!")
            sys.exit()
        else:
            sys.exit()

def main():
    play_game()

if __name__ == "__main__":
    main()