#!/usr/bin/python3

file = open("input.txt", "r")

lines = file.readlines()

arr = [0] * (len(lines[0]) - 1)

for line in lines:
    for idx, char in enumerate(line):
        if char.isdigit():
            arr[idx] += int(char)

gamma = 0
epsilon = 0

for i in range(0, len(arr)):
    print(i)
    print(arr[i])
    gamma = gamma << 1
    epsilon = epsilon << 1

    if arr[i] > (len(lines) / 2):
        gamma = gamma | 1
    else:
        epsilon = epsilon | 1

print(gamma * epsilon)
