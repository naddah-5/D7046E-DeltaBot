"""
Module for handling pytorch models.
"""

import torch
import torch.nn as nn


class NeuralModel():
    """
    Class for defining and handling our neural network.
    ### NeuralModel:
    network: nn.Sequential
    """

    def __init__(self, embedding_length: int = 300):
        self.network = nn.Sequential(
            nn.Linear(embedding_length, 1000),
            nn.Sigmoid(),
<<<<<<< HEAD
            nn.Linear(100, 2),
=======
            nn.Linear(1000, 600),
            nn.Sigmoid(),
            nn.Linear(600, 200),
            nn.Sigmoid(),
            nn.Linear(200, 3),
>>>>>>> 1a5686ed5f5cc351c61459720d50236447166c47
            nn.Softmax()
        )

    def define_network(self, new_network: nn.Sequential):
        """
        Manually overwrite the default network with your own model.
        """
        self.network = new_network

    def save_network(self, model_name: str):
        """
        Saves the specified network on disk as a state dict.
        """
        torch.save(self.network.state_dict(), model_name)

    def load_network(self, model_name: str):
        """
        Loads a specified model from disk, note that the dimensions must match.
        """
        self.network.load_state_dict(torch.load(model_name))
