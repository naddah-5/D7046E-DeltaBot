import unittest 
from DeltaCsvParser import DeltaCsvParser

class TestDeltaCsvParser(unittest.TestCase):

    def test_init(self):
        parser = DeltaCsvParser("src/data/dataset/Test_reviews.csv")
        self.assertEqual(parser.data,[(['bought','sever','vital','can',
    'dog',
    'food',
    'product',
    'found',
    'good',
    'qualiti',
    'product',
    'look',
    'like',
    'stew',
    'process',
    'meat',
    'smell',
    'better',
    'labrador',
    'finicki',
    'appreci',
    'product',
    'better'],
   5)])

    def test_score_calculator(self):
        parser = DeltaCsvParser("src/data/dataset/Test_reviews.csv")
        self.assertEqual(parser.scoreCalculator(5,0),0)
        self.assertEqual(parser.scoreCalculator(2,10),1)
        self.assertEqual(parser.scoreCalculator(2,6),2)
        self.assertEqual(parser.scoreCalculator(2,4),3)
        self.assertEqual(parser.scoreCalculator(65,100),4)
        self.assertEqual(parser.scoreCalculator(10,10),5)

    def test_preProcessing(self):
        parser = DeltaCsvParser("src/data/dataset/Test_reviews.csv")
        self.assertEqual(["hello","someth","drove"],parser.preProcesing("hello Something drove < !"))




unittest.main() 
    


