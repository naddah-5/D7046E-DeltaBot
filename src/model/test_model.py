import unittest
from neural_model import NeuralModel

class TestModel(unittest.TestCase):
    def test_save_network(self):
        test_model = NeuralModel()
        test_model.save_network("test.pt")

if __name__ == '__main__':
    unittest.main()