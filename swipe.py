"""
    Created 10/17/17
    Last Modified 1/10/17

    @Author Collin OConnor
"""

import random
import initialize

#Swipe Function checks for incorrect inputs and does the specified swipes
#########################################################################
def swipe(messageDictionary):
    if (u"board" not in messageDictionary): #checking direction
        resultDictionary = {"gameStatus": 'error: board missing'}
        return resultDictionary

    #reading in values:
    board = messageDictionary["board"]
    errorDictionary, validity, rowCount, columnCount = initialize.validateRowColumn(messageDictionary)
    if (validity == False):
        return errorDictionary

    if (u"grid" not in board):  # checking grid
        resultDictionary = {"gameStatus": 'error: grid missing'}
        return resultDictionary

    currentGrid = board["grid"]
    oldGrid = currentGrid[:]
    gridSize = rowCount * columnCount

    errorDictionary = validateGrid(messageDictionary, gridSize, currentGrid, oldGrid)
    if (validity == False):
        return errorDictionary

    if (u"direction" not in messageDictionary): #checking direction
        resultDictionary = {"gameStatus": 'error: direction missing'}
        return resultDictionary
    else:
        direction = messageDictionary[u"direction"]
        direction = direction.lower()

    if (direction == 'up'): #swipe up:
       resultDictionary = up(columnCount, rowCount, currentGrid, oldGrid, gridSize)

    elif (direction == 'down'):  # swipe down:
        resultDictionary = down(columnCount, rowCount, currentGrid, oldGrid, gridSize)

    elif (direction == 'left'):  # swipe left:
        resultDictionary = left(columnCount, rowCount, currentGrid, oldGrid, gridSize)

    elif (direction == 'right'):  # swipe right:
        resultDictionary = right(columnCount, rowCount, currentGrid, oldGrid, gridSize)

    else:  # no direction specified:
        resultDictionary = {"gameStatus": 'error: invalid direction'}

    return resultDictionary

#Up Function transposes the board as an upward swipe
#########################################################################
def up(columnCount, rowCount, currentGrid, oldGrid, gridSize):
    score = 0
    i = rowCount - 1
    while (i > 0):
        j = columnCount - 1
        while (j >= 0):
            if (currentGrid[i * rowCount + j] != 0):
                if(currentGrid[i * rowCount + j] == currentGrid[i * rowCount + j - rowCount]):
                    currentGrid[i * rowCount + j - rowCount] = currentGrid[i * rowCount + j] + 1
                    currentGrid[i * rowCount + j] = 0
                    score = score + 2 ** currentGrid[i * rowCount + j - rowCount]
                elif(currentGrid[i * rowCount + j - rowCount] == 0):
                    currentGrid[i * rowCount + j - rowCount] = currentGrid[i * rowCount + j]
                    currentGrid[i * rowCount + j] = 0
            j = j - 1
        i = i - 1

    currentGrid = addTile(currentGrid, gridSize)
    if (currentGrid == oldGrid):
        resultDictionary = {"gameStatus": 'error: no tiles can be shifted'}
    else:
        newBoard = {"rowCount": rowCount, "columnCount": columnCount, "grid": currentGrid}
        resultDictionary = {"score": score, "board": newBoard, "gameStatus": 'underway'}
    return resultDictionary


#Down Function transposes the board as a downward swipe
#########################################################################
def down(columnCount, rowCount, currentGrid, oldGrid, gridSize):
    score = 0
    i = 0
    while (i < rowCount - 1):
        j = 0
        while (j < columnCount):
            if (currentGrid[i * rowCount + j] != 0):
                if(currentGrid[i * rowCount + j] == currentGrid[i * rowCount + j + rowCount]):
                    currentGrid[i * rowCount + j + rowCount] = currentGrid[i * rowCount + j] + 1
                    currentGrid[i * rowCount + j] = 0
                    score = score + 2 ** currentGrid[i * rowCount + j + rowCount]
                elif(currentGrid[i * rowCount + j + rowCount] == 0):
                    currentGrid[i * rowCount + j + rowCount] = currentGrid[i * rowCount + j]
                    currentGrid[i * rowCount + j] = 0
            j = j + 1
        i = i + 1

    currentGrid = addTile(currentGrid, gridSize)
    if (currentGrid == oldGrid):
        resultDictionary = {"gameStatus": 'error: no tiles can be shifted'}
    else:
        newBoard = {"rowCount": rowCount, "columnCount": columnCount, "grid": currentGrid}
        resultDictionary = {"score": score, "board": newBoard, "gameStatus": 'underway'}
    return resultDictionary


#Left Function transposes the board as a left swipe
#########################################################################
def left(columnCount, rowCount, currentGrid, oldGrid, gridSize):
    score = 0
    i = 0
    while (i < rowCount):
        j = columnCount - 1
        while (j > 0):
            if (currentGrid[i * rowCount + j] != 0):
                if(currentGrid[i * rowCount + j] == currentGrid[i * rowCount + j - 1]):
                    currentGrid[i * rowCount + j - 1] = currentGrid[i * rowCount + j] + 1
                    currentGrid[i * rowCount + j] = 0
                    score = score + 2 ** currentGrid[i * rowCount + j - 1]
                elif(currentGrid[i * rowCount + j  - 1] == 0):
                    currentGrid[i * rowCount + j - 1] = currentGrid[i * rowCount + j]
                    currentGrid[i * rowCount + j] = 0
            j = j - 1
        i = i + 1

    currentGrid = addTile(currentGrid, gridSize)
    if (currentGrid == oldGrid):
        resultDictionary = {"gameStatus": 'error: no tiles can be shifted'}
    else:
        newBoard = {"rowCount": rowCount, "columnCount": columnCount, "grid": currentGrid}
        resultDictionary = {"score": score, "board": newBoard, "gameStatus": 'underway'}
    return resultDictionary


#Right Function transposes the board as a right swipe
#########################################################################
def right(columnCount, rowCount, currentGrid, oldGrid, gridSize):
    score = 0
    i = 0
    while (i < rowCount):
        j = 0
        while (j < columnCount - 1):
            if (currentGrid[i * rowCount + j] != 0):
                if(currentGrid[i * rowCount + j] == currentGrid[i * rowCount + j + 1]):
                    currentGrid[i * rowCount + j + 1] = currentGrid[i * rowCount + j] + 1
                    currentGrid[i * rowCount + j] = 0
                    score = score + 2 ** currentGrid[i * rowCount + j + 1]
                elif(currentGrid[i * rowCount + j + 1] == 0):
                    currentGrid[i * rowCount + j + 1] = currentGrid[i * rowCount + j]
                    currentGrid[i * rowCount + j] = 0
            j = j + 1
        i = i + 1

    currentGrid = addTile(currentGrid, gridSize)
    if (currentGrid == oldGrid):
        resultDictionary = {"gameStatus": 'error: no tiles can be shifted'}
    else:
        newBoard = {"rowCount": rowCount, "columnCount": columnCount, "grid": currentGrid}
        resultDictionary = {"score": score, "board": newBoard, "gameStatus": 'underway'}
    return resultDictionary

#addTile function adds a random tile to the current grid in a random location
#######################################################################
def addTile(currentGrid,gridSize):
    valLoc = 0
    newVal = random.random()  # getting random value and location
    if (newVal <= 0.25):
        newVal = 2
    else:
        newVal = 1

    zeroCount = False
    locFound = False
    i = 0
    while (i < gridSize):
        if (currentGrid[i] == 0):
            zeroCount = True
        i = i + 1

    if (zeroCount == True):
        while(locFound == False):
            valLoc = random.randint(0, gridSize - 1)
            if(currentGrid[valLoc] == 0):
                locFound = True
                currentGrid[valLoc] = newVal

    return currentGrid

#validateGrid valides the grid elements and size
######################################################
def validateGrid(messageDictionary, gridSize, currentGrid, oldGrid):
    validity = True
    if (gridSize != len(currentGrid)): #checking board
        resultDictionary = {"gameStatus": 'error: invalid board'}
        validity = False
        return resultDictionary, validity

    i = 0
    elementCount = 0
    while (i < gridSize):   #checking grid
        if not (isinstance(oldGrid[i], int)):
            resultDictionary = {"gameStatus": 'grid element is not an integer'}
            validity = False
            return resultDictionary, validity
        if (oldGrid[i] < 0 or oldGrid[i] > gridSize):
            resultDictionary = {"gameStatus": 'grid element is invalid value'}
            validity = False
            return resultDictionary, validity
        i = i + 1
        elementCount = elementCount + 1

    if (elementCount < 2):
        resultDictionary = {"gameStatus": 'not enough grid elements'}
        validity = False
        return resultDictionary, validity

    return messageDictionary, validity