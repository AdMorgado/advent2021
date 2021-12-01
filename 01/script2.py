file = open("input.txt", "r")
lines = file.readlines()

#constant
wSize = 3

count = 0

#prelogue
sum = int(lines[0])
for i in range(1, wSize):
    currValue = int(lines[i])
    sum += + int(lines[i])

for i in range(wSize, len(lines)):
    currValue = int(lines[i])
    tailValue = int(lines[i - wSize])
    
    currSum = sum + currValue - tailValue
    if(sum < currSum):
        count += 1

    sum = currSum

print(count)
