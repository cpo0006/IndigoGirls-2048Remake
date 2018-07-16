"""
    Created 11/10/17
    Last Modified 11/10/17

    @Author Collin OConnor
"""


from unittest import TestCase
import status as status
import json

class swipeTest(TestCase):
    def test100_010_AcceptanceTest1(self):
        messageDictionary = {"tile": 2, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]}}
        resultDictionary = status.status(messageDictionary)
        result = resultDictionary["gameStatus"]
        expected = "win"
        self.assertEquals(expected, result)

    def test200_010_AcceptanceTest2(self):
        messageDictionary = {"tile": 512,"board": {"columnCount": 4, "rowCount": 4, "grid": [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]}}
        resultDictionary = status.status(messageDictionary)
        result = resultDictionary["gameStatus"]
        expected = "lose"
        self.assertEquals(expected, result)

    def test300_010_AcceptanceTest3(self):
        messageDictionary = {"tile": 512,"board": {"columnCount": 4, "rowCount": 4, "grid": [1, 0, 3, 1, 5, 6, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8]}}
        resultDictionary = status.status(messageDictionary)
        result = resultDictionary["gameStatus"]
        expected = "underway"
        self.assertEquals(expected, result)

    def test200_010_AcceptanceTest2(self):
        messageDictionary = {"tile": 200000,"board": {"columnCount": 4, "rowCount": 4, "grid": [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]}}
        resultDictionary = status.status(messageDictionary)
        result = resultDictionary["gameStatus"]
        expected = "error: invalid tile value"
        self.assertEquals(expected, result)