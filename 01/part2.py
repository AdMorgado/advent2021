#!/usr/bin/python3

file = open("input.txt", "r")

#constant
wSize = 3


#rotating array to hold the last wSize elements
winIdx = 0
window = []

#prelogue
for i in range(0, wSize):
    currValue = int(file.readline())
    window.append(currValue)

count = 0
sum = sum(window)
while True:
    currLine = file.readline()
    if(currLine == ""):
        break
    
    currValue = int(currLine)
    currSum = sum + currValue - window[winIdx]
    if(sum < currSum):
        count += 1

    sum = currSum
    window[winIdx] = currValue
    winIdx += 1
    if winIdx >= wSize:
        winIdx = 0

print(count)
