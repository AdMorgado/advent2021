

paths = []
with open("input.txt", "r") as file: 
    lines = file.read().split()

    paths = [line.split("-") for line in lines]

nodes = {}
for path in paths:
    if not path[0] in nodes:
        nodes[path[0]] = [path[1]]
    else:
        nodes[path[0]].append(path[1])
    if not path[1] in nodes:
        nodes[path[1]] = [path[0]]
    else:
        nodes[path[1]].append(path[0])


numOfPaths = 0

stack = []
for cave in nodes["start"]:
    stack.append({"node": cave, "path": ["start"]})

while stack:
    currNode = stack.pop()
    currCave = currNode["node"]
    if currCave == "end":
        numOfPaths += 1
        continue
    if currCave in currNode["path"] and currCave.islower():
        continue

    for cave in nodes[currCave]:
        newPath = currNode["path"].copy()
        newPath.append(currCave)
        newObj = {"node": cave, "path": newPath}
        stack.append(newObj)

print(numOfPaths)