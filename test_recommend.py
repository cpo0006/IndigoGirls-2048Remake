"""
    Created 11/10/17
    Last Modified 11/10/17

    @Author Collin OConnor
"""


from unittest import TestCase
import recommend as recommend

class swipeTest(TestCase):
    def test100_010_AcceptanceTest1(self):
        messageDictionary = {"board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]}}
        resultDictionary = recommend.recommend(messageDictionary)
        result = resultDictionary["score"]
        expected = 16
        self.assertEquals(expected, result)

    def test100_020_AcceptanceTest1(self):
        messageDictionary = {"moves": 2, "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]}}
        resultDictionary = recommend.recommend(messageDictionary)
        result = resultDictionary["score"]
        if (result == 16 or result == 18 or result == 20 or result == 22 or result == 24 or result == 26 or
          result == 28 or result == 30 or result == 32 or result == 34): #all possible values given the board with two moves
            self.assertEquals(1, 1)
        else:
            self.assertEquals(0,1)

    def test200_010_AcceptanceTest2(self):
        messageDictionary = {"moves": "abc", "board": {"columnCount": 4, "rowCount": 4, "grid": [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]}}
        resultDictionary = recommend.recommend(messageDictionary)
        result = resultDictionary["gameStatus"]
        expected = "error: improper value for moves"
        self.assertEquals(expected, result)