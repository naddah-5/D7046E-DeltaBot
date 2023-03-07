"""
Main file, the orchestrator.
"""
import torch
from torch import nn

from src.client.client import Client
from src.model.neural_model import NeuralModel
from src.train.trainer import Train
from src.data.data import DeltaData
from src.data.delta_embedder import DeltaEmbedder
from src.data.delta_csv_parser import DeltaCsvParser


def main():
    """
    Orchestrator for running our training.
    """
    DATASET_PATH = 'src/data/dataset/Reviews.csv'
    neural_model = NeuralModel()
    trainer = Train(epochs=10, batch_size=10)
    data = DeltaData(embedder=DeltaEmbedder(), embedding_size=300,
                     csv_proceed_path="src/data/dataset/Processed_Data_test_medium.csv")

    trainer.run_training(dataset=data, network=neural_model.network, learning_rate=0.01)


if __name__ == '__main__':
    # main()

    model = NeuralModel()
    model.network.load_state_dict(torch.load('src/model/model.pt'))
    client = Client(model.network)
    client.run()
