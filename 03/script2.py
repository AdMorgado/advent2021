#!/usr/bin/python3

file = open("input.txt", "r")
lines = file.readlines()

dataLength = len(lines)
lineLength = len(lines[0]) - 1

mostCommons = lines
leastCommons = lines
for i in range(0, lineLength):
    ones = 0
    for j in range(0, len(mostCommons)):
        if mostCommons[j][i] == '1':
            ones += 1
    
    mostCommonNum = '0'
    if ones >= len(mostCommons) / 2:
        mostCommonNum = '1'
    if len(mostCommons) > 1:
        mostCommons = [line for line in mostCommons if line[i] == mostCommonNum]

for i in range(0, lineLength):
    ones = 0
    for j in range(0, len(leastCommons)):
        if leastCommons[j][i] == '1':
            ones += 1
    
    leastCommonNum = '0'
    if ones < len(leastCommons) / 2:
        leastCommonNum = '1'
    if len(leastCommons) > 1:
        leastCommons = [line for line in leastCommons if line[i] == leastCommonNum]

oxygen = int(mostCommons[0], 2)
carbon = int(leastCommons[0], 2)
print(oxygen * carbon)
