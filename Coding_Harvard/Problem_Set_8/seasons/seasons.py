from datetime import date
import sys
import inflect
import re


def main():
    time_input = input()

    try:
        birth_date = date.fromisoformat(time_input)
    except ValueError:
        print("Invalid date")
        sys.exit(1)

    today = date.today()
    sub = today-birth_date
    new_sub = sub.days*24*60
    p = inflect.engine()
    words = p.number_to_words(new_sub).capitalize().replace("and ","")
    print(words, "minutes")
    sys.exit(0)

def time(time_input):
    output = re.search(r"^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$",time_input)
    if time_input != output:
        return None

if __name__ == "__main__":
    main()



























"""from datetime import date
import sys
import inflect
import re


def main():

    print(time(input("Date of Birth: ")), "minutes")

def time(time_input):
    try:
        birth_date = date.fromisoformat(time_input)
    except:
        output = re.search(r"^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$",time_input)
        if time_input != output:
            sys.exit("Invalid")

    today = date.today()
    sub = today-birth_date
    new_sub = sub.days*24*60
    p = inflect.engine()
    words = p.number_to_words(new_sub).capitalize().replace("and ","")
    return words


if __name__ == "__main__":
    main()"""





"""from datetime import date
import sys
import inflect


def main():
    time_input = input("Date of Birth: ")

    try:
        birth_date = date.fromisoformat(time_input)
    except ValueError:
        print("Invalid date")
        sys.exit(1)

    today = date.today()
    sub = today-birth_date
    new_sub = sub.days*24*60
    p = inflect.engine()
    words = p.number_to_words(new_sub).capitalize().replace("and ","")
    print(words, "minutes")
    sys.exit(0)"""






"""
from datetime import timedelta
year = timedelta(days=365)
year.total_seconds()
31536000.0
"""
"""
from datetime import date
import sys
import inflect


def main():
    time_input = input("Date of Birth: ")

    try:
        birth_date = date.fromisoformat(time_input)
    except ValueError:
        print("Invalid date")
        sys.exit(1)

    today = date.today()
    yday = today.toordinal() - date(today.year, 1, 1).toordinal() + 1
    sub = today-birth_date
    new_sub = sub.days*24*60
    p = inflect.engine()
    words = p.number_to_words(new_sub)
    print(words)
"""
"""
from datetime import date
import sys
import inflect


def main():
    time_input = input("Date of Birth: ")

    try:
        birth_date = date.fromisoformat(time_input)
    except ValueError:
        print("Invalid date")
        sys.exit(1)
    today = date.today()
    sub = date.fromordinal(today.toordinal())
    s = sub - birth_date
    new_sub = s.days*24*60
    p = inflect.engine()
    words = p.number_to_words(new_sub)
    print(words)
"""
"""
from datetime import date
import sys
import inflect


def main():
    time_input = input("Date of Birth: ")

    try:
        birth_date = date.fromisoformat(time_input)
    except ValueError:
        print("Invalid date")
        sys.exit(1)

    today = date.today()
    sub = today-birth_date
    new_sub = sub.days*24*60
    p = inflect.engine()
    words = p.number_to_words(new_sub)
    print(words)




if __name__ == "__main__":
    main()
"""