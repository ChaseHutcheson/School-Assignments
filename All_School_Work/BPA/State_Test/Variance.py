import math
import statistics

def Calculate(grillFile):
    #Define Variables
    grillTemps = []
    highestTemp = 0
    lowestTemp = 100000
    tempTotal = 0
    tempMean = None

    #Pulls Temps
    grill = open(grillFile)
    with grill as f:
        for line in f:
            for word in line.split():
                grillTemps.append(int(word))
    
    #Finds Highest
    for i in range(len(grillTemps)):
        if int(grillTemps[i]) > highestTemp:
            highestTemp = int(grillTemps[i])

    #Finds Lowest
    for i in range(len(grillTemps)):
        if int(grillTemps[i]) < lowestTemp:
            lowestTemp = int(grillTemps[i])

    #Finds Mean
    for i in range(len(grillTemps)):
        tempTotal = tempTotal + int(grillTemps[i])
    tempMean = tempTotal / len(grillTemps)

    #Gets Grill Number
    print(str(grillFile).split("All_School_Work\BPA\State_Test\Grill_"))
    

#     print(f"""
# Min: {lowestTemp}
# Max: {highestTemp}
# Mean: {tempMean}
# Standard Deviation of temps is {statistics.stdev(grillTemps)}
#     """)



Calculate("All_School_Work\BPA\State_Test\Grill_1.txt")