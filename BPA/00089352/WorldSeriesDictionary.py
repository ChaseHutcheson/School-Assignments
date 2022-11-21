#00089352

#Define the Dicts
Teams = {}
Years = {}

#Open and Read the Data File
txtOpen = open("BPA\\00089352\WorldSeriesDictonary.txt", "r")
txtRead = txtOpen.readlines()

#Format and add Data to Dicts
for i in range(len(txtRead)):

    #Remove unneeded space
    teamNames = txtRead[i].rstrip("\n")

    #Account for year the World Series wasnt Played. If the year is one of the two, the every year after is +1 to account for it
    teamYear = 1903 + i
    if teamYear >= 1904:
        teamYear += 1
    if teamYear >= 1994:
        teamYear += 1

    #Append data to Teams Dict. the data is formated as "Year:Team"
    Teams[str(teamYear)] = teamNames

    #Counts wins for each team. If teamName is in Teams, then you +1. if not, you makie it equal to 1
    if teamNames in Years:
        Years[teamNames] += 1
    else:
        Years[teamNames] = 1

#Ask user for input
userYear = int(input("What year do you wish to know about (1903 - 2021)? "))

#Tells user about unplayed years
if userYear == 1904 or userYear == 1994:
    print(f"Sorry, There wasnt a World Series in {userYear}.")

#Tells user the limits of the database
elif int(userYear) < 1903  or int(userYear) > 2022:
    print("Our data doesnt got contain that year")
    
#Prints if all previous ifs are false
else:
    print(f"The winner of the {str(userYear)} World Series was the {Teams[str(userYear)]}. They won the World Series {Years[Teams[str(userYear)]]} times. ")