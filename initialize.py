"""
    Created 9/16/17
    Last Modified 11/10/17

    @Authors David Umphress / Collin OConnor
"""

import random

# initializeGame function will initialize the starting grid
##############################################################
def initializeGame(messageDictionary):
    #validating inputs
    errorDictionary, validity, rowCount, columnCount = validateRowColumn(messageDictionary)
    if (validity == False):
        return errorDictionary

    #get grid size
    gridSize = columnCount * rowCount

    #get starting values and grid locations
    startValLocation1 = random.randint(1, gridSize)
    startValLocation2 = random.randint(1, gridSize)
    if (startValLocation1 == startValLocation2 and startValLocation2 != 1):
        startValLocation2 = startValLocation2 - 1
    if (startValLocation1 == startValLocation2 and startValLocation2 != gridSize):
        startValLocation2 = startValLocation2 + 1

    startVal1 = random.random()
    startVal2 = random.random()
    if (startVal1 <= 0.25):
        startVal1 = 2
    else:
        startVal1 = 1

    if (startVal2 <= 0.25):
        startVal2 = 2
    else:
        startVal2 = 1

    #Make Grid
    grid = [0] * gridSize
    grid[startValLocation1 - 1] = startVal1
    grid[startValLocation2 - 1] = startVal2

    #Returns dictionary with score, board, and gamestatus
    board = {'columnCount': columnCount, 'rowCount': rowCount, 'grid': grid}
    returnVal = {'score': 0, 'board': board, 'gameStatus': 'underway'}
    return returnVal

#validateRowColumn will validate the rowCount and columnCount inputs
###################################################################
def validateRowColumn(messageDictionary):
    rowCount = 0
    columnCount = 0
    validity = True
    if (u"columnCount" not in messageDictionary):
        columnCount = 4
    else:
        if not (isinstance(messageDictionary["columnCount"], int)):
            resultDictionary = {"gameStatus": 'columnCount is not an integer'}
            validity = False
            return resultDictionary, validity, rowCount, columnCount
        columnCount = messageDictionary["columnCount"]
        if (columnCount < 2 or columnCount > 99):
            resultDictionary = {"gameStatus": 'columnCount is out of bounds'}
            validity = False
            return resultDictionary, validity, rowCount, columnCount

    # get row count
    if (u"rowCount" not in messageDictionary):
        rowCount = 4
    else:
        if not (isinstance(messageDictionary["rowCount"], int)):
            resultDictionary = {"gameStatus": 'rowCount is not an integer'}
            validity = False
            return resultDictionary, validity, rowCount, columnCount
        rowCount = messageDictionary["rowCount"]
        if (rowCount < 2 or rowCount > 99):
            resultDictionary = {"gameStatus": 'rowCount is out of bounds'}
            validity = False
            return resultDictionary, validity, rowCount, columnCount
    return messageDictionary, validity, rowCount, columnCount