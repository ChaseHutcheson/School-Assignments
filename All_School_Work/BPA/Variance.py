from genericpath import isfile
from importlib.resources import path
import os
import statistics
from unittest import result


dir_path = 'All_School_Work\\BPA\\State_Test'
count = 1

for path in os.listdir(dir_path):
    def Calculate():
        #Define Variables
        global count
        highestTemp = 0
        lowestTemp = 100000
        tempTotal = 0
        grillFile = f"All_School_Work\\BPA\\State_Test\\Grill_{str(count)}.txt"
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

        for i in range(len(grillTemps)):
            if (int(grillTemps[i]) - int(tempMean) < int(deviation) * 2):
                result = "Fail! "
                whyResult = "Too Hot: "
            elif (int(grillTemps[i]) - int(tempMean) > int(deviation) * 2):
                result = "Fail! "
                whyResult = "Too Cold: "
            elif (int(grillTemps[i]) - int(tempMean) > (deviation) * 2) and (int(grillTemps[i]) - int(tempMean) < int(deviation) * 2):
                result = "Fail! "
                whyResult = "Too Hot and Too Cold: "
            if  (int(grillTemps[i]) - int(tempMean) < (deviation) * 2) and (int(grillTemps[i]) - int(tempMean) > int(deviation) * 2):
                result = "Pass! "
                whyResult = ""

        
        return result, whyResult, grillname, lowestTemp, highestTemp, tempMean, deviation, grillTemps

    def Print():
        print(f"""
        Grill {Calculate()[2]}
        Min: {Calculate()[3]}
        Max: {Calculate()[4]}
        Mean {Calculate()[5]}
        Standard Deveiation of temps is {Calculate()[6]}
        {Calculate()[1]}{Calculate()[0]}
        """)

        if os.path.isfile(os.path.join(dir_path, path)):
            global count
            if count == 5:
                count = 5
            else:
                count += 1

    Print()