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

def flood(grid, pos, pool):
    if grid[pos[1]][pos[0]] == 9 or pos in pool:
        return 0
    pool.append(pos)
    resultFlood = []
    if pos[0] > 0:
        resultFlood.append(flood(grid, [pos[0]-1, pos[1]], pool))
    if pos[0]  < (gridSizeX-1):
        resultFlood.append(flood(grid, [pos[0]+1, pos[1]], pool))
    if pos[1] > 0:
        resultFlood.append(flood(grid, [pos[0], pos[1]-1], pool))
    if pos[1] < (gridSizeY-1):
        resultFlood.append(flood(grid, [pos[0], pos[1]+1], pool))
    return 1 + sum(resultFlood)

sizes = []
for point in lowPoints:
    totalSize = 1
    sizes.append(flood(grid, point, []))
    if len(sizes) > 3:
        sizes = sorted(sizes, reverse=True)[:-1]

result = 1

print(sizes)

for size in sizes:
    result = result * size

print(result)
