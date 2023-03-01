import torch
import torch.nn as nn
import copy

def NeuralModel():
    def __init__(self, embedding_length:int = 300):
        self.network = nn.Sequential(
            nn.Linear(embedding_length, 100),
            nn.Sigmoid(),
            nn.Linear(100, 6),
            nn.Softmax()
        )
    
    def save_network(self, model_name: str):
        torch.save(self.network, model_name)