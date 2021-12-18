#!/usr/bin/python3

grid = []
with open("input.txt", "r") as file:
    grid = [[int(num) for num in line] for line in file.read().split()]



gridSizeY = len(grid)
gridSizeX = len(grid[0])

lowPoints = []
for y in range(gridSizeY):
    for x in range(gridSizeX):
        currValue = grid[y][x]
        conditions = []
        if x > 0:
            conditions.append(currValue < grid[y][x-1])
        if y > 0:
            conditions.append(currValue < grid[y-1][x])
        if x < (gridSizeX-1):
            conditions.append(currValue < grid[y][x+1])
        if y < (gridSizeY-1):
            conditions.append(currValue < grid[y+1][x])
        if all(conditions):
            lowPoints.append([x,y])

riskScore = 0

for lowPoint in lowPoints:
    riskScore += grid[lowPoint[1]][lowPoint[0]] + 1

print(riskScore)

