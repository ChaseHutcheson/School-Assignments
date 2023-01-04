Pennies = int(input("How many pennies do you have? "))

def Pennies_to_Change():
    #Dollars
    Dollars = Pennies//100
    Dollars2 = Pennies % 100
    print(f"Dollar Bils = {Dollars}")

    Quarters = Dollars2 // 25
    Quarters2 = Dollars2 % 25
    print(f"Quarters = {Quarters}")

    Dimes = Quarters2 // 10
    Dimes2 = Quarters2 % 10
    print(f"Dimes = {Dimes}")

    Nickels = Dimes2 // 5
    Nickels2 = Dimes2 % 5
    print(f"Nickels = {Nickels}")

    Pennies2 = Nickels2
    print(f"Pennies = {Pennies2}")

Pennies_to_Change()