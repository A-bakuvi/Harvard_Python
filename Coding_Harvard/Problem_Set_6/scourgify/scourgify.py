import sys
import csv

def main():
    try:
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(sys.argv) == 3:
            if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
                print("Not a csv file")
                sys.exit(1)
            elif not open(sys.argv[1], "r"):
                print("File doesn't exist")
    except FileNotFoundError:
        print("File doesn't exist")
        sys.exit(1)

    else:
        student_data(sys.argv[1], sys.argv[2])

def student_data(file_before,file_after):
    with open(file_before, "r") as file:
        Dictreader = csv.DictReader(file)
        student = list(Dictreader)
    with open(file_after,"w",newline ='') as fil:
        writer = csv.DictWriter(fil, fieldnames=["first","last", "house"])
        writer.writerow({"first": "first","last":"last", "house": "house"})
        for s in student:
            last_name,first_name = s['name'].split(",")
            house = s['house']
            writer.writerow({"first": first_name.strip(),"last":last_name, "house": house})




#store name to write on file later
#write data in file_after



if __name__ == "__main__":
    main()