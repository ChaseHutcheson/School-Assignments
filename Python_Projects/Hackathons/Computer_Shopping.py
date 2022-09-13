msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zephyrus_m16_price = 1849.79

def most_expensive(laptop_1, laptop_2, laptop_3, laptop_4):
    most_expensive = 0
    if laptop_1 > most_expensive:
        most_expensive = laptop_1
    else:
        most_expensive = most_expensive

    if laptop_2 > most_expensive:
        most_expensive = laptop_2
    else:
        most_expensive = most_expensive

    if laptop_2 > most_expensive:
        most_expensive = laptop_2
    else:
        most_expensive = most_expensive

    if laptop_3 > most_expensive:
        most_expensive = laptop_4
    else:
        most_expensive = most_expensive

    print(f"The most expensive laptop ammount is: {most_expensive}")

def least_expensive(laptop_1, laptop_2, laptop_3, laptop_4):
    least_expensive = 1000000000
    if laptop_1 < least_expensive:
        least_expensive = laptop_1
    else:
        least_expensive = least_expensive

    if laptop_2 < least_expensive:
        least_expensive = laptop_2
    else:
        least_expensive = least_expensive

    if laptop_2 < least_expensive:
        least_expensive = laptop_2
    else:
        least_expensive = least_expensive

    if laptop_3 < least_expensive:
        least_expensive = laptop_4
    else:
        least_expensive = least_expensive

    print(f"The least expensive laptop ammount is: {least_expensive}")

def rounded(laptop_1, laptop_2, laptop_3, laptop_4):
    decimal = laptop_1 = int(laptop_1)
    if decimal >= .50:
        laptop_1 = laptop_1 + 1
        print(f"The rounded price of the MSI RTX A5000 is {laptop_1}")
    else:
        laptop_1 = int(laptop_1)
        print(f"The rounded price of the MSI RTX A5000 is {laptop_1}")

    decimal = laptop_2 = int(laptop_2)
    if decimal >= .50:
        laptop_2 = laptop_2 + 1
        print(f"The rounded price of the Gigabyte Aero is {laptop_2}")
    else:
        laptop_2 = int(laptop_2)
        print(f"The rounded price of the Gigabyte Aero is {laptop_2}")

    decimal = laptop_3 = int(laptop_3)
    if decimal >= .50:
        laptop_3 = laptop_3 + 1
        print(f"The rounded price of the Razer Blade 15 is {laptop_3}")
    else:
        laptop_3 = int(laptop_3)
        print(f"The rounded price of the Razer Blade 15 is {laptop_3}")

    decimal = laptop_4 = int(laptop_4)
    if decimal >= .50:
        laptop_4 = laptop_4 + 1
        print(f"The rounded price of the Asus Zephyrus is {laptop_4}")
    else:
        laptop_4 = int(laptop_4)
        print(f"The rounded price of the Asus Zephyrus is {laptop_4}")

def average(laptop_1, laptop_2, laptop_3, laptop_4):
    sum = laptop_1 + laptop_2 + laptop_3 + laptop_4
    average = round(sum / 4, 2)
    
    print(f"The average price of all computers is: {average}")

most_expensive(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price)
least_expensive(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price)
rounded(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price)
average(msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price)