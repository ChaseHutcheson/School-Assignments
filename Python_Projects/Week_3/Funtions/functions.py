# DRY - Dont Repeat yourself.
# DRY - Dont Repeat yourself.
# DRY - Dont Repeat yourself.
# DRY - Dont Repeat yourself.
def directions():
    print("Turn left out of parking Lot")
    print("Drive to stop light and turn left")
    print("Drive one mile through Canfield")
    print("Starbucks is acroos the street from Sheetz")
    print("Turn Left into Starbucks")

number_of_people = int(input("How many people are asking for directions?"))

while number_of_people > 0:
    print(f"{number_of_people} - New Directions")
    directions()
    number_of_people = number_of_people - 1