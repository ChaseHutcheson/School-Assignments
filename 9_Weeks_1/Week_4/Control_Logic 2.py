char_name = input("What is your name? ").title()
char_class = input("What kind of adventurer are you? ").title()

def welcome_screen():
    if (char_name == "Ninja" and char_class == "Mage"):
        print("Hello Warrior...")
    elif (char_name == "Bob" or char_class == "Builder"):
        print("I bet you like to build things.")
    elif (char_name != "Bob" and char_name != "Ninja"):
        print("Hmm... I dont think weve met.")

    if (char_name == "Bob" or char_name == "Ninja"):
        print("I figured one of you would show up.")
    else:
        print("We've reached the final else.")
    
welcome_screen()
print(char_name)