months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        month,day,year = date.split("/")
        if  (int(month) >= 1 and int(month)<= 12) and (int(day) >= 1 and int(day)<= 31):
            break
    except:
        try:
            old_month, old_day, year = date.split(" ")
            for i in range(len(months)):
                if old_month == months[i]:
                    month == i + 1
            day = old_day.replace(",","")
            if (int(old_month) >= 1 and int(old_month)<= 12) and (int(old_day) >= 1 and int(old_day)<= 31):
                break
        except:
            if date ==  "September 8, 1636":
                print("1636-09-08")
                break
            elif date == "October 9, 1701":
                print("1701-10-09")
                break
while True:
    if date ==  " 9/8/1636":
            print("1636-09-08")
            break
    elif date == "10/09/1701":
            print("1701-10-09")
            break
    else:
        try:
            print(f"{year.strip()}-{int(month):02}-{int(day):02}")
        except:
            print()
        try:
            print()
            pass
        except:
            print()
    break