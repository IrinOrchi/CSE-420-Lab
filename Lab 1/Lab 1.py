inputFile = open("i.input.txt", "r")

keywords = ("if","int","else","float")
mathOperators = ("=", "-", "*", "/", "+")
logicalOps = ("<", ">")
others = (";", ",", "{", "(", ")", "}")

keywordsSet = set()
mathOperatorsSet = set()
logicalOperatorsSet = set()
othersSet = set()
identifiersSet = set()
numValuesSet = list()

def whichType(x):
    x = x.strip()
    if x.endswith(others):
        othersSet.add(x[-1])
        x = x[0:-1]

    if x in keywords:
        keywordsSet.add(x)
    elif x in mathOperators:
        mathOperatorsSet.add(x)
    elif x in logicalOps:
        logicalOperatorsSet.add(x)
    elif x in others:
        othersSet.add(x)
    else:
        try:
            x = int(x)
            if x not in numValuesSet:
                numValuesSet.append(str(x))
        except ValueError:
            if "." in x:
                if x not in numValuesSet:
                    numValuesSet.append(str(x))
            else:
                identifiersSet.add(x)

for line in inputFile:
    lineStr = line.strip()
    lineStr = lineStr.split()
    for word in lineStr:
        whichType(word)

#delete empty string from the identifiers
identifiersSet.remove("")

print("keywords: ", end="")
print(*keywordsSet ,sep=", ")

print("Identifiers: ", end="")
print(*identifiersSet ,sep=", ")

print("Math Operators: ", end="")
print(*mathOperatorsSet ,sep=", ")

print("Logical Operators: ", end="")
print(*logicalOperatorsSet ,sep=", ")

print("Numerical Values: ", end="")
print(*numValuesSet, sep=", ")

print("Others: ", end="")
print(*othersSet ,sep=" ")