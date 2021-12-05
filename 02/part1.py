#!/usr/bin/python3

# Note: it could be further optimized by not performing whole string comparisons,
# but instead compare the first character

file = open("input.txt", "r")

hor = 0
depth = 0

while True:
    line = file.readline()
    if(line == ""):
        break

    command, x = line.split(" ")
    value = int(x)
    if command == 'up':
        depth -= value
    elif command == 'down':
        depth += value
    elif command == 'forward':
        hor += value




print(hor * depth)