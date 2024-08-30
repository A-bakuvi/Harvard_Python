import sys
def main():
    try:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(sys.argv) == 2:
            if not sys.argv[1].endswith(".py"):
                print("Not a Python file")
                sys.exit(1)
            elif not open(sys.argv[1], "r"):
                print("File does not exist")
                sys.exit(1)
    except FileNotFoundError:
        print("File does not exist")
    else:
        f = loc(sys.argv[1])
        print(f)

def loc(file):
    i = 0
    with open(file, "r") as file_name:
        for f in file_name:
            strip_line = f.lstrip()
            if not strip_line.startswith("#") and strip_line:
                i += 1
    return i


if __name__ == "__main__":
    main()