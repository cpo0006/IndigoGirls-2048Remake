"""
    Created 10/17/17
    Last Modified 11/10/17

    @Author Collin OConnor
"""


from unittest import TestCase
import swipe as swipe


class swipeTest(TestCase):
    def test100_010_AcceptanceTest1(self):
        messageDictionary = {"direction": "right", "board": {"columnCount": 4, "rowCount": 4, "grid": [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}}
        resultDictionary = swipe.swipe(messageDictionary)
        result = resultDictionary["score"]
        expected = 4
        self.assertEquals(expected, result)

    def test200_010_AcceptanceTest2(self):
        messageDictionary = {"direction": "left", "board": {"columnCount": 4, "rowCount": 4, "grid": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}
        resultDictionary = swipe.swipe(messageDictionary)
        result = resultDictionary["score"]
        expected = 4
        self.assertEquals(expected, result)

        def test300_010_AcceptanceTest1(self):
            messageDictionary = {"direction": "up", "board": {"columnCount": 4, "rowCount": 4,
                                                                 "grid": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0]}}
            resultDictionary = swipe.swipe(messageDictionary)
            result = resultDictionary["score"]
            expected = 0
            self.assertEquals(expected, result)

    def test400_010_AcceptanceTest1(self):
        messageDictionary = {"direction": "down", "board": {"columnCount": 4, "rowCount": 4,
                                                          "grid": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}}
        resultDictionary = swipe.swipe(messageDictionary)
        result = resultDictionary["score"]
        expected = 0
        self.assertEquals(expected, result)

    def test500_010_AcceptanceTest5(self):
        messageDictionary = {"board": {"columnCount": 4, "rowCount": 4, "grid":[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}}
        resultDictionary = swipe.swipe(messageDictionary)
        result = resultDictionary[u"gameStatus"]
        expected = "error: direction missing"
        self.assertEquals(expected, result)

    def test500_020_AcceptanceTest5(self):
        messageDictionary = {"direction": "in","board": {"columnCount": 4, "rowCount": 4, "grid":[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}}
        resultDictionary = swipe.swipe(messageDictionary)
        result = resultDictionary[u"gameStatus"]
        expected = "error: invalid direction"
        self.assertEquals(expected, result)