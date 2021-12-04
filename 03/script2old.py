#!/usr/bin/python3

file = open("example.txt", "r")
lines = file.readlines()

dataLength = len(lines)
lineLength = len(lines[0]) - 1

oxygen = 0
carbon = 0

leastCommonLines = lines
mostCommonLines = lines
for i in range(lineLength - 1, -1, -1):
    ones = 0
    for j in range(0, dataLength):
        if lines[j][i] == '1':
            ones += 1
    
    mostCommon = '0'
    if ones >= dataLength / 2:
        mostCommon = '1'
    leastCommon = '0'
    if ones <= dataLength / 2:
        leastCommon = '1'

    print(ones)
    print(mostCommonLines)
    print("\n\n")

    if len(mostCommonLines) > 1:
        mostCommonLines = [line for line in mostCommonLines if line[i] == mostCommon]
    if len(leastCommonLines) > 1:
        leastCommonLines = [line for line in leastCommonLines if line[i] == leastCommon]



print("-------------------\-\-\-\-\-\----------------")
print(mostCommonLines)

result = int(mostCommonLines[0]) * int(leastCommonLines[0]) 
print(result)
