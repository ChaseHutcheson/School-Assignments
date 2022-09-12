def greeting(x):
    if x < 12:
        print("Good Morning")
    else:
        print("Good Afternoon")

time = int(input("What time is it? "))

greeting(time)