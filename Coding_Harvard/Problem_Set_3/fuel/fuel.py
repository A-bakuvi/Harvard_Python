def main():
    while True:
        inp = input("Fraction: ")
        try:
            fraction = convert(inp)
            percentage = gauge(round(fraction))
            print(percentage, sep = " ")
            break
        except(ValueError,ZeroDivisionError) as error:
             print(error)

def convert(fraction):

        try:
            x,y = fraction.split("/")
        except:
            raise ValueError
        if not x.isdigit() or not y.isdigit():
            raise ValueError
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x>y:
            raise ValueError

        inp = int(x)*100/int(y)
        return inp


def gauge(percentage):
        if percentage<=1:
            return "E"

        if percentage>=99:
            return "F"
        else:
            return f"{percentage}%"




if __name__ == "__main__":
    main()

#CONVERT
#convert is reasponsible for rounding fraction to the nearest int between 0-100.
#checks if x and/or y is not an int or if x is greater than y then raise value error
#if y is 0 then raise ZeroDivisionError

#GAUGE
#"E" if that int is less than or equal to 1,
#"F" if that int is greater than or equal to 99,
#and "Z%" otherwise, wherein Z is that same int.

"""
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
"""