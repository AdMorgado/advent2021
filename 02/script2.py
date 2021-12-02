#!/usr/bin/python3

file = open("input.txt", "r")

hor = 0
depth = 0
aim = 0

while True:
    line = file.readline()
    if(line == ""):
        break

    command, x = line.split(" ")
    firstChar = command[0]
    value = int(x)
    if firstChar == 'u':
        aim -= value
    elif firstChar == 'd':
        aim += value
    elif firstChar == 'f':
        hor += value
        depth += aim * value


print(hor * depth)