from validator_collection import validators,checkers
import sys


def main():
    print(response(input("What's your email adress?: ")))
def response(y):
        if checkers.is_email(y):
            print("Valid")
            sys.exit(0)
        else:
            print("Invalid")
            sys.exit(0)

if __name__ == "__main__":
    main()