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
    if firstChar == 'u': #up
        aim -= value
    elif firstChar == 'd': #down
        aim += value
    elif firstChar == 'f': #forward
        hor += value
        depth += aim * value


print(hor * depth)
