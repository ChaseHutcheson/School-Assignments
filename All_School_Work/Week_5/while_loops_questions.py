num_1 = 3.4
num_2 = 7

def my_function():
    quiz = float(input(f"What is {num_1} + {num_2}: "))
    while(quiz != (num_1 + num_2)):
        print("No. That's wrong. Try again.")
        my_function()

        print("Congrats. That's the correct answer.")

my_function()