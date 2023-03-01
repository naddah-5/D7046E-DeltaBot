import unittest 
from DeltaCsvParser import DeltaCsvParser

class TestScoreCalculation(unittest.TestCase):

    def test_score_calculator(self):
        parser = DeltaCsvParser()
        self.assertEqual(parser.scoreCalculator(5,0),0)
        self.assertEqual(parser.scoreCalculator(2,10),1)
        self.assertEqual(parser.scoreCalculator(2,6),2)
        self.assertEqual(parser.scoreCalculator(2,4),3)
        self.assertEqual(parser.scoreCalculator(65,100),4)
        self.assertEqual(parser.scoreCalculator(10,10),5)


if __name__ == "'__main__":
    unittest.main()


