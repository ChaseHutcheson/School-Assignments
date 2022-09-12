# Parameters are when you pass through a value in a function. That value goes inside of the ()

char_name = input("What is your name? ")
char_role = input("What character role are you? ")

def my_function(the_name, the_role):
    print(f"Your name is {the_name}")
    print(f"Your role is {the_role}")


my_function(char_name, char_role)