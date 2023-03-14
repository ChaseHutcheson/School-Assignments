import Chase_code as cc
from time import sleep


def The_Answer():
    password = input("What is the answer to life, the univers and everything? ")
    
    if(password == "42"):
        cc.CLEAR_CONSOLE()
        print("Welcome wise one. I see you've traveled the Galaxy. Lets begin.")
    elif(password != "bob"):
        cc.CLEAR_CONSOLE()
        print("This is no time for jokes. ")
    elif(password == "tom"):
        cc.CLEAR_CONSOLE()
        print("Ah yes. The funny cat that chases that mouse.")
    else:
        cc.CLEAR_CONSOLE()
        print("I see yoou are new. Go get more experince then come back.")

def Level_1():
    print("The man opens the door. ")
    cc.CLEAR_CONSOLE()
    sleep(2)
    print("An old wizard approaches you.")
    sleep(2)
    cc.CLEAR_CONSOLE()
    begin_quest = input("Are you ready to begin your adventure? y/n ")
    if begin_quest == "y":
        cc.CLEAR_CONSOLE()
        print("The adventure begins...")
    else:
        cc.CLEAR_CONSOLE()
        print("Your are correct, it is best if you get some sleep.")

The_Answer()
Level_1()