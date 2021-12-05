#!/usr/bin/python3

drawnNumbers = []
boards = []

def paragraphToBoard(raw):
    rows = raw.split("\n")
    rows = [row.split() for row in rows]
    return [
        [int(elem) for elem in row]
        for row in rows] 

with open("input.txt", "r") as file:
    
    paragraphs = file.read().split("\n\n")
    drawnNumbers = list(map(int, paragraphs[0].split(",")))

    paragraphs = paragraphs[1:]
    boards = [paragraphToBoard(paragraph) for paragraph in paragraphs]

# booleanBoards[0][y] for row, booleanBoards[1][x] for columns 
booleanBoards = [[[False]*5 for n in range(5)] for ligma in range(len(boards))] 

#for board in booleanBoards:
#print(booleanBoards)

found = False

isColumn = False
targetIndex = 0

#booleanboard input, with target x and y
def hasBoardWon(board, y, x):
    #check column
    columnValues = [False, False, False, False, False] 
    for targetY in range(5):
        columnValues[targetY] = board[targetY][x]

    return all(board[y]) or all(columnValues)

#while found == False:
for num in drawnNumbers:
    for idx, board in enumerate(boards):
        for y, row in enumerate(board):
            for x, value in enumerate(row):
                if num == value:
                    booleanBoards[idx][y][x] = True

                    if(hasBoardWon(booleanBoards[idx], y, x)):
                        found = True    

        if found == True:
            break
    if found == True:
        break

#print(idx)
#for board in booleanBoards:
#    print(board)
    
score = 0
for y in range(5):
    for x in range(5):
        if booleanBoards[idx][y][x] == False:
            value = boards[idx][y][x]
            score += value

print(score * num)
