
def getClosingCharacter(char):
    if char == "(":
        return ")"
    elif char == "[":
        return "]"
    elif char == "{":
        return "}"
    elif char == "<":
        return ">"

def getCharScore(char):
    if char == ")":
        return 1
    if char == "]":
        return 2
    if char == "}":
        return 3
    if char == ">":
        return 4

def isOpeningCharacter(char, stack):  
    beginningLen = len(stack)
    if char == "(":
        stack.append("(")
    elif char == "[":
        stack.append("[")
    elif char == "{":
        stack.append("{")
    elif char == "<":
        stack.append("<")
    #return true if a new element was added to stack
    return beginningLen != len(stack)


lines = []
with open("input.txt", "r") as file:
    lines = file.read().split("\n")
 
uncorruptedStacks = []
for line in lines:
    stack = []
    corrupt = False
    for char in line:
        if not isOpeningCharacter(char, stack):
            expectedCharacter = getClosingCharacter(stack.pop())
            if char != expectedCharacter:
                corrupt = True
                break
    if not corrupt and stack:
        uncorruptedStacks.append(stack)

def getScore(stack):
    errorScore = 0
    for char in reversed(stack):
        closingCharacter = getClosingCharacter(char)
        errorScore = errorScore * 5 + getCharScore(closingCharacter)
    return errorScore

scores = [getScore(stack) for stack in uncorruptedStacks]
sortedScores = sorted(scores)
print(sortedScores[len(scores) // 2])
