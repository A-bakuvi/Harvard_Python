from tabulate import tabulate
import sys
import csv

def main():
    try:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(sys.argv) == 2:
            if not sys.argv[1].endswith(".csv"):
                print("Not a csv file")
                sys.exit(1)
            elif not open(sys.argv[1], "r"):
                print("File doesn't exist")
                sys.exit(1)
    except FileNotFoundError:
        print("File doesn't exist")
        sys.exit(1)

    ascii(sys.argv[1])

def ascii(file_name):
    with open(file_name, "r") as file:
        read = csv.reader(file)
        names = list(read)
        header = names[0]
        table_data = names[1:]
        print(tabulate(table_data, header, tablefmt="grid"))





if __name__ == "__main__":
    main()