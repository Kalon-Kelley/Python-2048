from random import *

tableSize = 4

numbers = [2, 4]

gameDict = {
    0: [0, 0, 0, 0],
    1: [0, 0, 0, 0],
    2: [0, 0, 0, 0],
    3: [0, 0, 0, 0],
}

gameDictC = {
    0: [gameDict[0][0], gameDict[1][0], gameDict[2][0], gameDict[3][0]],
    1: [gameDict[0][1], gameDict[1][1], gameDict[2][1], gameDict[3][1]],
    2: [gameDict[0][2], gameDict[1][2], gameDict[2][2], gameDict[3][2]],
    3: [gameDict[0][3], gameDict[1][3], gameDict[2][3], gameDict[3][3]],
}

allTiles = []
largestTile = 2
roundNum = 0

RndPlaces = [-1, -1]

if roundNum == 0:
    for i in range(2):
        rndRow = randint(0, 3)
        rndColumn = randint(0, 3)

        while rndRow == RndPlaces[0] and rndColumn == RndPlaces[1]:
            rndRow = randint(0, 3)
            rndColumn = randint(0, 3)

        RndPlaces[0] = rndRow
        RndPlaces[1] = rndColumn
        gameDict[rndRow][rndColumn] = 2
'''
gameDict = {
    0: [0, 0, 0, 4],
    1: [0, 0, 0, 0],
    2: [0, 0, 4, 0],
    3: [0, 0, 0, 2],
}
'''
for key, value in gameDict.items():
    print("\n{}    {}    {}    {}".format(value[0], value[1], value[2], value[3]))

allTiles = []

for row in range(4):
    for column in range(4):
        allTiles.append(gameDict[row][column])
allTiles.sort()
largestTile = allTiles[-1]

gameLimit = int(input("What size tile do you wish to reach to finish the game? or enter nothing for default 2048"))
if gameLimit == "":
    gameLimit = 2048

gameDictC = {
    0: [gameDict[0][0], gameDict[1][0], gameDict[2][0], gameDict[3][0]],
    1: [gameDict[0][1], gameDict[1][1], gameDict[2][1], gameDict[3][1]],
    2: [gameDict[0][2], gameDict[1][2], gameDict[2][2], gameDict[3][2]],
    3: [gameDict[0][3], gameDict[1][3], gameDict[2][3], gameDict[3][3]],
}

while largestTile != gameLimit:
    direction = input("Which direction would you like to slide? [w][a][s][d]").lower()

    if direction == "w":
        for row in range(4):
            tempRow = []
            for column in range(4):
                if gameDictC[row][column] != 0:
                    tempRow.append(gameDictC[row][column])
                    gameDictC[row][column] = 0
            for i in range(len(tempRow) - 1):
                if tempRow[i] == tempRow[i + 1]:
                    tempRow[i] += tempRow[i + 1]
                    tempRow.pop(i + 1)
                    tempRow.append(0)
            for j in range(len(tempRow)):
                gameDictC[row][j] = tempRow[j]
            tempRow.clear()
            gameDict = {
                0: [gameDictC[0][0], gameDictC[1][0], gameDictC[2][0], gameDictC[3][0]],
                1: [gameDictC[0][1], gameDictC[1][1], gameDictC[2][1], gameDictC[3][1]],
                2: [gameDictC[0][2], gameDictC[1][2], gameDictC[2][2], gameDictC[3][2]],
                3: [gameDictC[0][3], gameDictC[1][3], gameDictC[2][3], gameDictC[3][3]],
            }
    if direction == "s":
        for row in range(4):
            tempRow = []
            for column in range(4):
                if gameDictC[row][column] != 0:
                    tempRow.append(gameDictC[row][column])
                    gameDictC[row][column] = 0
            if len(tempRow) > 1:
                for i in range(len(tempRow) - 1, -1, -1):
                    if tempRow[i] == tempRow[i - 1]:
                        tempRow[i] += tempRow[i - 1]
                        tempRow.pop(i - 1)
                        tempRow.insert(0, 0)
            tempRow.reverse()
            leftOverSpaces = 4 - len(tempRow)
            for i, j in zip(range(len(tempRow)), range(3, leftOverSpaces - 1, -1)):
                gameDictC[row][j] = tempRow[i]
            tempRow.clear()
            gameDict = {
                0: [gameDictC[0][0], gameDictC[1][0], gameDictC[2][0], gameDictC[3][0]],
                1: [gameDictC[0][1], gameDictC[1][1], gameDictC[2][1], gameDictC[3][1]],
                2: [gameDictC[0][2], gameDictC[1][2], gameDictC[2][2], gameDictC[3][2]],
                3: [gameDictC[0][3], gameDictC[1][3], gameDictC[2][3], gameDictC[3][3]],
            }

    if direction == "a":
        for row in range(4):
            tempRow = []
            for column in range(4):
                if gameDict[row][column] != 0:
                    tempRow.append(gameDict[row][column])
                    gameDict[row][column] = 0
            for i in range(len(tempRow) - 1):
                if tempRow[i] == tempRow[i + 1]:
                    tempRow[i] += tempRow[i + 1]
                    tempRow.pop(i + 1)
                    tempRow.append(0)
            for j in range(len(tempRow)):
                gameDict[row][j] = tempRow[j]
            tempRow.clear()
            gameDictC = {
                0: [gameDict[0][0], gameDict[1][0], gameDict[2][0], gameDict[3][0]],
                1: [gameDict[0][1], gameDict[1][1], gameDict[2][1], gameDict[3][1]],
                2: [gameDict[0][2], gameDict[1][2], gameDict[2][2], gameDict[3][2]],
                3: [gameDict[0][3], gameDict[1][3], gameDict[2][3], gameDict[3][3]],
            }

    if direction == "d":
        for row in range(4):
            tempRow = []
            for column in range(4):
                if gameDict[row][column] != 0:
                    tempRow.append(gameDict[row][column])
                    gameDict[row][column] = 0
            if len(tempRow) > 1:
                for i in range(len(tempRow) - 1, -1, -1):
                    if tempRow[i] == tempRow[i - 1]:
                        tempRow[i] += tempRow[i - 1]
                        tempRow.pop(i - 1)
                        tempRow.insert(0, 0)
            tempRow.reverse()
            leftOverSpaces = 4 - len(tempRow)
            for i, j in zip(range(len(tempRow)), range(3, leftOverSpaces - 1, -1)):
                gameDict[row][j] = tempRow[i]
            tempRow.clear()
            gameDictC = {
                0: [gameDict[0][0], gameDict[1][0], gameDict[2][0], gameDict[3][0]],
                1: [gameDict[0][1], gameDict[1][1], gameDict[2][1], gameDict[3][1]],
                2: [gameDict[0][2], gameDict[1][2], gameDict[2][2], gameDict[3][2]],
                3: [gameDict[0][3], gameDict[1][3], gameDict[2][3], gameDict[3][3]],
            }

    rndRow = randint(0, 3)
    rndColumn = randint(0, 3)
    counter = 0
    for i in range(4):
        for j in range(4):
            if gameDict[i][j] != 0:
                counter += 1
            if counter < 16:
                if gameDict[rndRow][rndColumn] != 0:
                    while gameDict[rndRow][rndColumn] != 0:
                        rndRow = randint(0, 3)
                        rndColumn = randint(0, 3)
                else:
                    break
            else:
                quit(print("You Failed"))

    gameDict[rndRow][rndColumn] = numbers[randint(0, 1)]
    roundNum += 1

    if (direction == "d") or (direction == "a"):
        gameDictC = {
            0: [gameDict[0][0], gameDict[1][0], gameDict[2][0], gameDict[3][0]],
            1: [gameDict[0][1], gameDict[1][1], gameDict[2][1], gameDict[3][1]],
            2: [gameDict[0][2], gameDict[1][2], gameDict[2][2], gameDict[3][2]],
            3: [gameDict[0][3], gameDict[1][3], gameDict[2][3], gameDict[3][3]],
        }

    allTiles = []

    for row in range(4):
        for column in range(4):
            allTiles.append(gameDict[row][column])
    allTiles.sort()
    largestTile = allTiles[-1]

    for key, value in gameDict.items():
        print("\n{}    {}    {}    {}".format(value[0], value[1], value[2], value[3]))
    print("\n")
    #for key, value in gameDictC.items():
        #print("\n{}    {}    {}    {}".format(value[0], value[1], value[2], value[3]))

print("Congratulations you WON!")

input("press any key to exit")