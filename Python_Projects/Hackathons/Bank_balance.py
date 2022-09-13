customer_name = input("Welcome, what is your name? ")

starting_balance = 5000.25

print(f"Hello {customer_name} you're starting balance is {starting_balance}")

pay_check = float(input("How much of your paycheck would you like to deposit? "))

expenditure_item = input("Looks like you went shopping. What did you buy? ")

expenditure = float(input(f"How much does {expenditure_item} cost? "))

def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
    ending_balance = balance + deposits - expense_amount
    print(f"Good day, {user_name}. After spending money on {expense_item} in the amount of {expense_amount}, your current checking balance is: {ending_balance}")

checking_balance(customer_name, starting_balance, pay_check, expenditure_item, expenditure)