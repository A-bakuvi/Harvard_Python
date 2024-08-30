#imports a function named Figlet from pyfiglet library to help us get the fonts
from pyfiglet import Figlet
#imports a library named random to be able to make random choices if the user doesnt input anything
import random
#imports a library named system(sys) in order to access the command line
import sys

def main():
    # we assigned Figlet() to figlet in order to use the function
    figlet = Figlet()
    # if the user doesnt input anything to the command line then we make a random choice of fonts then print it on screen by random.choice()
    if len(sys.argv) == 1:
        rando = random.choice(figlet.getFonts())
        figlet.setFont(font=rando)
        # getting users input and printing the font by it
        inp = input("Enter Text: ")
        print(figlet.renderText(inp))
    #if the user enters -f or --font right after the name of program and then chooses from one of the fonts in Figlet() and writes it right
    #after -f or --font then it prints the correct font after getting the input from the user
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or "--font":
            font = sys.argv[2]
            if font in figlet.getFonts():
                figlet.setFont(font=font)
                # getting users input and printing the correct font by it
                inp = input("Enter Text: ")
                print(figlet.renderText(inp))
            #for any other case we just print "Invalid Usage" then exit the program
            else:
                print("Invalid Usage")
                sys.exit[1]
        #for any other case we just print "Invalid Usage" then exit the program
        else:
            print("Invalid Usage")
            sys.exit[1]
    #for any other case we just print "Invalid Usage" then exit the program
    else:
        print("Invalid Usage")
        sys.exit[1]
# makes the main function work at the end
if __name__ == "__main__":
    main()


































































































































































"""from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

c = input("Input: ",sys.argv[1:3])
if sys.argv[1] != "-f" or "--font":
    sys.exit
if sys.argv[2] != figlet.getFonts():
    sys.exit
if sys.argv == 1:
    a = figlet.setFont(random.choice)
    print(figlet.renderText(a))
if sys.argv == 3:
    b = figlet.setFont(font=c)
    print(figlet.renderText(b))
c = input("Input: ",sys.argv[1:3])
"""

"""
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and sys.argv[1] == ("-f" or "--font"):
    isRandomFont = False
else:
    print("Invalid Usage")
    sys.exit(1)


if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        print("invalid Usage")
        sys.exit(1)
else:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font = f)

c = input("Input: ")
print("Output: ")
print(figlet.renderText(c))
"""