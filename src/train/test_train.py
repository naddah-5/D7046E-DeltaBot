import unittest
from trainer import Train

class TestTraining(unittest.TestCase):

    def test_defaults(self):
        test = Train()
        self.assertEqual(test.batch_size, 10)
        self.assertEqual(test.epochs, 1)

    

if __name__ == '__main__':
    unittest.main()