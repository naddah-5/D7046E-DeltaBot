import torch
import torch.nn
import torch.testing
import unittest
from neural_model import NeuralModel

class TestModel(unittest.TestCase):
    def test_save_and_load_network(self):
        test_model = NeuralModel()
        loaded_model = NeuralModel()

        test_model.save_network("test.pt")
        loaded_model.load_network("test.pt")

        test_net = test_model.network.state_dict()
        loaded_net = loaded_model.network.state_dict()

        for key in test_net:
            torch.testing.assert_allclose(test_net[key], loaded_net[key])

if __name__ == '__main__':
    unittest.main()