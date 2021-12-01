file = open("input.txt", "r")

lastValue = int(file.readline())

count = 0
while True:
    currLine = file.readline()
    if(currLine == ""):
        break

    currValue = int(currLine)
    if(lastValue < currValue):
        count += 1;    

    lastValue = currValue



print(count)