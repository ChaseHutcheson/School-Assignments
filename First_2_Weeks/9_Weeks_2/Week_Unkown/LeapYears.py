year = int(input("Please Enter Current Year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("Leap year.")
        else:
            print("Not Leap year.")
    else:
        print("Leap year.")
else:
    print("Not Leap year.")