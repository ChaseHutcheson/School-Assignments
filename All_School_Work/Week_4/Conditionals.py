from time import sleep


def The_Answer():
    password = input("What is the answer to life, the univers and everything? ")
    
    if(password == "42"):
        print("Welcome wise one. I see you've traveled the Galaxy. Lets begin.")
    elif(password != "bob"):
        print("This is no time for jokes. ")
    elif(password == "tom"):
        print("Ah yes. The funny cat that chases that mouse.")
    else:
        print("I see yoou are new. Go get more experince then come back.")

def Level_1():
    print("The man opens the door. ")
    sleep(2)
    print("An old wizard approaches you.")
    sleep(2)
    begin_quest = input("Are you ready to begin your adventure? y/n ")
    if begin_quest == "y":
        print("The adventure begins...")
    else:
        print("Your are correct, it is best if you get some sleep.")

The_Answer()
Level_1()