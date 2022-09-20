char_name = input("What is your name? ").title()

def welcome_screen():
    if (char_name == "Ninja"):
        print("Hello Warrior...")
    if (char_name == "Bob"):
        print("I bet you like to build things.")
    if (char_name != "Bob" and char_name != "Ninja"):
        print("Hmm... I dont think weve met.")
    if (char_name == "Bob" or char_name == "Ninja"):
        print("I figured one of you would show up.")
    
welcome_screen()
print(char_name)