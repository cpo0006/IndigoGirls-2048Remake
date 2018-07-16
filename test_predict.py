"""
    Created 10/17/17
    Last Modified 11/10/17

    @Author Collin OConnor
"""


from unittest import TestCase
import predict as predict


class swipeTest(TestCase):
    def test100_010_AcceptanceTest1(self):
        messageDictionary = {'direction':'left',  'moves':1, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}
        resultDictionary = predict.predict(messageDictionary)
        result = resultDictionary["highScore"]
        expected = 16
        self.assertEquals(expected, result)


    def test100_020_AcceptanceTest2(self):
        messageDictionary = {'op':'predict', 'direction':'left',  'moves':2, 'board': {'columnCount': 4, 'rowCount': 4, 'grid': [0,0,0,1,0,0,0,1,2,2,0,0,1,0,2,2]}}
        resultDictionary = predict.predict(messageDictionary)
        result = resultDictionary["lowScore"]
        expected = 16
        self.assertEquals(expected, result)

    def test100_020_AcceptanceTest2(self):
        messageDictionary = {'op': 'predict', 'direction': 'left', 'moves': 2,
                             'board': {'columnCount': "h", 'rowCount': 4,
                                       'grid': [0, 0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1, 0, 2, 2]}}
        resultDictionary = predict.predict(messageDictionary)
        result = resultDictionary["gameStatus"]
        expected = "columnCount is not an integer"
        self.assertEquals(expected, result)

