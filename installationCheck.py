"""
    Created 9/16/17
    Last Modified 11/10/17

    @Authors David Umphress / Collin OConnor
"""

import dispatch as dispatch
import swipe as swipe
import recommend as recommend
import status as status
import predict as predict

validJson = '{"op": "initializeGame"}'
validResult = dispatch.dispatch(validJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson, validResult))

errorJson = '{"op": "unknown"}'
errorResult = dispatch.dispatch(errorJson)
print(("Input string:\t{0}\nOutput string:\t{1}\n\n").format(errorJson, errorResult))

validJson2 = '{"op": "initializeGame", "rowCount": 2}'
validResult2 = dispatch.dispatch(validJson2)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson2, validResult2))

validJson3 = '{"op": "initializeGame", "rowCount": 2, "columnCount": 2}'
validResult3 = dispatch.dispatch(validJson3)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson3, validResult3))

validJson4 = '{"op": "initializeGame", "rowCount": two, "columnCount": 2}'
validResult4 = dispatch.dispatch(validJson4)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson4, validResult4))

validJson5 = '{"op": "initializeGame", "rowCount": 101, "columnCount": 2}'
validResult5 = dispatch.dispatch(validJson5)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson5, validResult5))

validJson6 = '{"op": "initializeGame", "rowCount": 1, "columnCount": 2}'
validResult6 = dispatch.dispatch(validJson6)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson6, validResult6))

messageDictionary = {"op": "swipe", "direction": "up", "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}
resultDictionary = swipe.swipe(messageDictionary)
print resultDictionary

messageDictionary = {"op": "swipe", "direction": "LEFT", "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}
resultDictionary = swipe.swipe(messageDictionary)
print resultDictionary

messageDictionary = {"op": "swipe", "direction": "right", "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}
resultDictionary = swipe.swipe(messageDictionary)
print resultDictionary

messageDictionary = {"op": "swipe", "direction": "down", "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}
resultDictionary = swipe.swipe(messageDictionary)
print resultDictionary

messageDictionary = {"op": "swipe", "direction": "down", "board": {"rowCount": 4, "columnCount": 4, "grid": [20, 20, 1, 1, 20, 20, 1, 1, 20, 1, 1, 1, 9, 10, 12, 11]}}
resultDictionary = swipe.swipe(messageDictionary)
print resultDictionary

messageDictionary = {"op": "swipe", "direction": "up", "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 2, 3, 4, 1, 3, 2, 1, 5, 6, 7, 8, 9, 10, 12, 11]}}
resultDictionary = swipe.swipe(messageDictionary)
print resultDictionary

messageDictionary = {"op": "swipe", "direction": "left", "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 1, 3, 4, 4, 3, 2, 1, 5, 6, 7, 8, 9, 10, 12, 11]}}
resultDictionary = swipe.swipe(messageDictionary)
print resultDictionary

messageDictionary = {"op": "swipe", "direction": "LeFt", "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 1, 1, 4, 4, 3, 2, 1, 5, 6, 7, 8, 9, 10, 12, 11]}}
resultDictionary = swipe.swipe(messageDictionary)
print resultDictionary

validJson7 = '{"op": "initializeGame", "rowCount": "i", "columnCount": 2}'
validResult7 = dispatch.dispatch(validJson7)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson7, validResult7))

validJson8 = '{"op": "initializeGame", "rowCount": 4, "columnCount": 0}'
validResult8 = dispatch.dispatch(validJson8)
print(("Input string:\t{0}\nOutput string:\t{1}\n").format(validJson8, validResult8))

messageDictionary = {"op": "recommend", "moves": 1, "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 1, 1, 4, 4, 3, 2, 1, 5, 6, 7, 8, 9, 10, 12, 11]}}
resultDictionary = recommend.recommend(messageDictionary)
print resultDictionary

messageDictionary = {"op": "recommend", "moves": 5, "board": {"rowCount": 4, "columnCount": 4, "grid": [0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1, 1, 2, 0]}}
resultDictionary = recommend.recommend(messageDictionary)
print resultDictionary

messageDictionary = {"op": "recommend", "moves": 999, "board": {"rowCount": 4, "columnCount": 4, "grid": [0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1, 1, 2, 0]}}
resultDictionary = recommend.recommend(messageDictionary)
print resultDictionary

messageDictionary = {"op": "status", "board": {"rowCount": 4, "columnCount": 4, "grid": [0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1, 1, 2, 0]}}
resultDictionary = status.status(messageDictionary)
print resultDictionary

messageDictionary = {"op": "status", "tile": 2048, "board": {"rowCount": 4, "columnCount": 4, "grid": [1, 2, 3, 4, 2, 1, 4, 3, 5, 6, 7, 8, 7, 8, 6, 5]}}
resultDictionary = status.status(messageDictionary)
print resultDictionary

messageDictionary = {"op": "status","tile": 2, "board": {"rowCount": 2, "columnCount": 2, "grid": [1, 2, 3, 4]}}
resultDictionary = status.status(messageDictionary)
print resultDictionary

messageDictionary = {"op": "recommend", "moves": -1, "board": {"rowCount": 4, "columnCount": 4, "grid": [0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1, 1, 2, 0]}}
resultDictionary = recommend.recommend(messageDictionary)
print resultDictionary

messageDictionary = {"op": "recommend", "moves": 2, "board": {"rowCount": 4, "columnCount": 4, "grid": ["e", 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1, 1, 2, 0]}}
resultDictionary = recommend.recommend(messageDictionary)
print resultDictionary

messageDictionary = {"op": "recommend", "moves": 0, "board": {"rowCount": 4, "columnCount": 4, "grid": [0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1, 1, 2, 0]}}
resultDictionary = recommend.recommend(messageDictionary)
print resultDictionary

messageDictionary = {"op": "status","tile": 9999, "board": {"rowCount": 2, "columnCount": 2, "grid": [1, 2, 3, 4]}}
resultDictionary = status.status(messageDictionary)
print resultDictionary

messageDictionary = {"op": "status", "board": {"rowCount": "h", "columnCount": 4, "grid": [0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1, 1, 2, 0]}}
resultDictionary = status.status(messageDictionary)
print resultDictionary

messageDictionary = {"op": "predict", "moves": 5, "board": {"rowCount": 4, "columnCount": 4, "grid": [0, 1, 0, 1, 1, 0, 0, 2, 2, 1, 0, 2, 1, 1, 2, 0]}}
resultDictionary = predict.predict(messageDictionary)
print resultDictionary