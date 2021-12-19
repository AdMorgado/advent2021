#!/usr/bin/python3

numOfDays = 80

fishes = [0] * 9
with open("input.txt", "r") as file:
    values = [int(num) for num in file.read().split(",")]

    for val in values:
        fishes[val] += 1

for i in range(numOfDays):
    newFishes = [0] * 9

    for j in range(8):
        newFishes[j] = fishes[j + 1]

    newFishes[8] = fishes[0]
    newFishes[6] += fishes[0]

    fishes = newFishes

print(sum(fishes))
