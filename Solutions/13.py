year = 2000
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year", year)
        else:
            print("Not Leap year")
    else:
        print("Leap year", year)