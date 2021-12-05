#!/usr/bin/python3

ventLines = []
with open("example.txt", "r") as file:
    lines = file.readlines()

    for line in lines:
        left, right = line.split(" -> ")
        x1, y1 = left.split(",")
        x2, y2 = right.split(",")

        ventLine = [[int(x1), int(y1)], [int(x2), int(y2)]]
        ventLines.append(ventLine)

grid = [[0] * 10 for n in range(10)]

for line in ventLines:
    #iterate through y, same column
    if line[0][0] == line[0][1] and line[1][0] == line[1][1]:
        x1 = line[0][0]
        x2 = line[1][0]
        start = x1
        end = x2
        if x2 < x1:
            start = x2
            end = x1
        for i in range(start, end):
            grid[i][i] += 1
    elif line[0][0] == line[1][0]:
        x = line[0][0]
        y1 = line[0][1]
        y2 = line[1][1]
        start = y1
        end = y2
        if y2 < y1:
            start = y2
            end = y1
        for y in range(start, end + 1):
            grid[y][x] += 1
    #iterate through x, same row
    elif line[0][1] == line[1][1]:
        y = line[0][1]
        x1 = line[0][0]
        x2 = line[1][0]
        start = x1
        end = x2
        if x2 < x1:
            start = x2
            end = x1
        for x in range(start, end + 1):
            grid[y][x] += 1

total = 0
for row in grid:
    print(row)
    for value in row:
        if value >= 2:
            total += 1

print(total)
