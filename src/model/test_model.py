"""
Testing module.
"""

import unittest
import torch
import torch.nn as nn
import torch.testing
from neural_model import NeuralModel

class TestModel(unittest.TestCase):
    """
    Unit testing for the NeuralModel class.
    """

    def test_save_and_load_network(self):
        """
        Verify that saving and loading networks work as intended.
        """
        test_model = NeuralModel()
        loaded_model = NeuralModel()

        test_model.save_network("test.pt")
        loaded_model.load_network("test.pt")

        test_net = test_model.network.state_dict()
        loaded_net = loaded_model.network.state_dict()

        for key in test_net:
            torch.testing.assert_allclose(test_net[key], loaded_net[key])

    def test_define_network(self):
        """
        Verify that we can manuallly define our networks.
        """
        test_model = NeuralModel()
        new_model = nn.Sequential(
            nn.Linear(3, 1),
            nn.Sigmoid(),
            nn.Softmax()
        )
        test_model.define_network(new_network=new_model)
        self.assertEqual(new_model, test_model.network)

if __name__ == '__main__':
    unittest.main()