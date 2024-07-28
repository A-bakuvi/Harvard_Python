import re



def main():
    print(convert(input("Hours: ")))

def convert(s):
    output = re.search(r"^([0]?[0-9]|[1][0-2])(?::([0-5][0-9]))? (AM|PM) to ([0]?[0-9]|[1][0-2])(?::([0-5][0-9]))? (AM|PM)$",s)
    new_starting_minutes = 0
    new_ending_minutes = 0
    if output:
        starting_hour,starting_minutes,starting_am_pm,ending_hour,ending_minutes,ending_am_pm = output.groups()
        if starting_minutes == None:
            starting_minutes = 00
        new_starting_minutes = int(starting_minutes)
        if ending_minutes == None:
            ending_minutes = 00
        new_ending_minutes = int(ending_minutes)
        new_starting_hour = int(starting_hour)
        hour_start = new_starting_hour % 12
        if starting_am_pm == "PM":
            hour_start += 12
        else:
            hour_start += 0
        new_ending_hour = int(ending_hour)
        hour_end = new_ending_hour % 12
        if ending_am_pm == "PM":
            hour_end += 12
        else:
            hour_end += 0
        return f"{hour_start:02}:{new_starting_minutes:02} to {hour_end:02}:{new_ending_minutes:02}"
    else:
        raise ValueError()




if __name__ == "__main__":
    main()