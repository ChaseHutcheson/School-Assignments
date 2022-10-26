from genericpath import isfile
from importlib.resources import path
import os
import statistics
from unittest import result



def Calculate():
    #Define Variables
    highestTemp = 0
    lowestTemp = 100000
    tempTotal = 0
    grillFile = "All_School_Work\\BPA\\State_Test\\Grill_1.txt"
    grillTemps = []
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

    #Gets Deviation
    deviation = statistics.stdev(grillTemps)

    #Gets Name
    grillname = grillFile.replace('All_School_Work\\BPA\\State_Test\\Grill_', '')
    grillname = grillname.replace('.txt', '')
    grillFile = grillFile.replace("1", str(int(grillname) + 1))
    
    return grillname, lowestTemp, highestTemp, tempMean, deviation, grillTemps
    grillname + 1

def Print():
    Calculate()
    for i in range(len(Calculate()[5])):
        if (int(Calculate()[5][i] - int(Calculate()[3]) > (int(Calculate()[4]) * 2))):
            result = "Fail"
            whyResult = "Too Hot: "
        if (int(Calculate()[5][i]) - int(Calculate()[3]) < (int(Calculate()[4]) * 2)):
            result = "Fail"
            whyResult = "Too Cold: "
        if (int(Calculate()[5][i]) - int(Calculate()[3])) == (int(Calculate()[4]) * 2):
            result = "Fail"
            whyResult = "Too Hot and Too Cold: "
        else:
            result = "Pass!"
            whyResult = ""

    print(f"""
    Grill {Calculate()[0]}
    Min: {Calculate()[1]}
    Max: {Calculate()[2]}
    Mean {Calculate()[3]}
    Standard Deveiation of temps is {Calculate()[4]}
    {whyResult}{result}
    """)

Print()
Print()
Print()
Print()
Print()