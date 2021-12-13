
def getClosingCharacter(char):
    if char == "(":
        return ")"
    elif char == "[":
        return "]"
    elif char == "{":
        return "}"
    elif char == "<":
        return ">"
def getScore(char):
    if char == ")":
        return 3
    if char == "]":
        return 57
    if char == "}":
        return 1197
    if char == ">":
        return 25137

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

errorScore = 0

for line in lines:
    stack = []
    for char in line:
        if not isOpeningCharacter(char, stack):
            expectedCharacter = getClosingCharacter(stack.pop())
            if char != expectedCharacter:
                errorScore += getScore(char)
                break

print(errorScore)
