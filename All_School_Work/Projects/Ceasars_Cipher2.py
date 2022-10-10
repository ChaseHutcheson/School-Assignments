import string
print("Cesear's Cipher")

#Seperates Phrase into letters
phraselist = []
shiftedlist = []
encrypted = []
listcheck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
spacecheck = [-64, -63, -62, -61, -60, -59, -58, -57, -56, -55, -54, -53, -52, -51, -50, -49, -48, -47, -46, -45, -44, -43, -42, -41, -40, -39, -38, ]
not_encrypted = input("Enter a phrase (NO NUMBERS, CAPS OR SPECIAL CHARACTERS)")
shiftamount = int(input("How much do you want to shift by (1-25): "))

#converts letters to numbers
for x in not_encrypted:
    phraselist.append(ord(x) - 96)

#Shifts ltter value
for x in range(len(phraselist)):
    shiftedlist.append(int(phraselist[x]) + (shiftamount))

print(shiftedlist)

#turns numbers back into letters
for i in range(len(shiftedlist)):
    for p in range(len(listcheck)):
        if shiftedlist[i] > 26:
            shiftedlist[i] = int(shiftedlist[i]) - 26
    for k in range(len(spacecheck)):
        if shiftedlist[i] == spacecheck[k]:
            shiftedlist[i] = -64
    encrypted.append(chr(int(shiftedlist[i]) + 96))

#prints out encrypted phrase
print(*encrypted)
