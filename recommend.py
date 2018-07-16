"""
    Created 11/09/17
    Last Modified 11/10/17

    @Author Collin OConnor
"""

import swipe as swipe
import initialize

#Swipe Function checks for incorrect inputs and does the specified swipes
#########################################################################
def recommend(messageDictionary):
    if (u"board" not in messageDictionary): #checking direction
        resultDictionary = {"gameStatus": 'error: board missing'}
        return resultDictionary

    #reading in values:
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
        else :
            if (messageDictionary["moves"] < 0):
                resultDictionary = {"gameStatus": "error: negative value for moves"}
                return resultDictionary
            if (messageDictionary["moves"] == 0):
                resultDictionary = {'score': 0, 'board': board, "gameStatus": "underway"}
                return resultDictionary
            moves = messageDictionary[u"moves"]

    #calculating recommended moves
    totalScore = 0
    inputDict = 0
    j = 0
    while (j < moves):
        inputDict = {"direction": "up", "board": board}
        upMove = swipe.swipe(inputDict)
        if (u"score" not in upMove):
            upScore = -1
        else:
            upScore = upMove["score"]
        inputDict = {"direction": "down", "board": board}
        downMove = swipe.swipe(inputDict)
        if (u"score" not in downMove):
            downScore = -1
        else:
            downScore = downMove["score"]
        inputDict = {"direction": "left", "board": board}
        leftMove = swipe.swipe(inputDict)
        if (u"score" not in leftMove):
            leftScore = -1
        else:
            leftScore = leftMove["score"]
        inputDict = {"direction": "right", "board": board}
        rightMove = swipe.swipe(inputDict)
        if (u"score" not in rightMove):
                rightScore = -1
        else:
            rightScore = rightMove["score"]

        #check if loss
        if ((upMove["gameStatus"] != "underway") and (downMove["gameStatus"] != "underway") and
                (leftMove["gameStatus"] != "underway") and (rightMove["gameStatus"] != "underway")):
            resultDictionary = {"gameStatus": "error: no tiles can be shifted for number of given moves"}
            return resultDictionary

        highScore = upScore
        if (highScore < downScore):
            highScore = downScore
        if (highScore < leftScore):
            highScore = leftScore
        if (highScore < rightScore):
            highScore = rightScore

        if (highScore == upScore):
            inputDict = upMove
        if (highScore == downScore):
            inputDict = downMove
        if (highScore == leftScore):
            inputDict = leftMove
        if (highScore == rightScore):
            inputDict = rightMove

        totalScore = totalScore + inputDict["score"]
        if (j == 0):
            resultDictionary = {"score": inputDict["score"],"board": inputDict["board"]}
        j = j + 1

    resultDictionary["gameStatus"] = inputDict["gameStatus"]
    resultDictionary["score"] = totalScore
    return resultDictionary