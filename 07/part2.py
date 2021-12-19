#!/usr/bin/python3

values = []
with open("input.txt", "r") as file:
    values = [int(num) for num in file.read().split(",")]

def getFuelCost(length):
    return (length * (length + 1)) // 2

valuesLen = len(values)
fuelCosts = [0] * valuesLen
for pos in range(valuesLen):
    for i in range(valuesLen):
        fuelCosts[pos] += getFuelCost(abs(values[i] - pos)) 

print(min(fuelCosts))