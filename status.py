"""
    Created 11/09/17
    Last Modified 11/10/17

    @Author Collin OConnor
"""

import math
import swipe as swipe
import initialize

#Swipe Function checks for incorrect inputs and does the specified swipes
#########################################################################
def status(messageDictionary):
    if (u"board" not in messageDictionary): #checking direction
        resultDictionary = {"gameStatus": 'error: board missing'}
        return resultDictionary

    #reading in values:
    board = messageDictionary["board"]

    board = messageDictionary["board"]
    errorDictionary, validity, rowCount, columnCount = initialize.validateRowColumn(board)
    if (validity == False):
        return errorDictionary

    if (u"grid" not in board):  # check if grid is missing
        resultDictionary = {"gameStatus": 'error: grid missing'}
        return resultDictionary

    currentGrid = board["grid"]
    oldGrid = currentGrid[:]
    gridSize = rowCount * columnCount

    errorDictionary, validity = swipe.validateGrid(messageDictionary, gridSize, currentGrid, oldGrid)
    if (validity == False):
        return errorDictionary

    #Get move count
    moves = 0
    if (u"moves" not in messageDictionary): #checking moves
        moves = 1
    else:
        if not (isinstance(messageDictionary["moves"], int)):
            resultDictionary = {"gameStatus": "error: improper value for moves"}
            return resultDictionary
        moves = messageDictionary[u"moves"]


    #check tile
    tile = 0
    if (u"tile" not in messageDictionary):  # check if grid is missing
        tile = 2 ** round(rowCount * columnCount * 0.6875)
    else:
        tile = messageDictionary["tile"]
        if (tile < 2 or tile > 2 **(rowCount * columnCount)):
            resultDictionary = {"gameStatus": "error: invalid tile value"}
            return resultDictionary

    #Check if win
    tileVal = math.log(tile, 2)
    j = 0
    while (j < gridSize):
        if (currentGrid[j] >= tileVal):
            resultDictionary = {"gameStatus": "win"}
            return resultDictionary
        j = j + 1

    #check if loss
    inputDict = {"direction": "up", "board": board}
    upMove = swipe.swipe(inputDict)
    inputDict = {"direction": "down", "board": board}
    downMove = swipe.swipe(inputDict)
    inputDict = {"direction": "left", "board": board}
    leftMove = swipe.swipe(inputDict)
    inputDict = {"direction": "right", "board": board}
    rightMove = swipe.swipe(inputDict)

    if ((upMove["gameStatus"] != "underway") and (downMove ["gameStatus"] != "underway") and
            (leftMove["gameStatus"] != "underway") and (rightMove["gameStatus"] != "underway")):
        resultDictionary = {"gameStatus": "lose"}
        return resultDictionary

    resultDictionary = {"gameStatus": "underway"}
    return resultDictionary