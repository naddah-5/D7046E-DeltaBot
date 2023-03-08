"""
Main file, the orchestrator.
"""
import torch

from src.client.client import Client
from src.model.neural_model import NeuralModel
from src.train.trainer import Train
from src.data.data import DeltaData
from src.data.delta_embedder import DeltaEmbedder


def main():
    """
    Orchestrator for running our training.
    """
    DATASET_PATH = 'src/data/dataset/Reviews.csv'
    neural_model = NeuralModel()
    trainer = Train(epochs=30, batch_size=10)
    data = DeltaData(embedder=DeltaEmbedder(),
                     embedding_size=300, csv_proceed_path="src/data/medium_sampled_dataset.csv")

    neural_model.network = trainer.run_training(dataset=data, network=neural_model.network, learning_rate=0.001)
    neural_model.save_network('network.pt')

if __name__ == '__main__':
    # main()

    model = NeuralModel()
    model.network.load_state_dict(torch.load('network.pt'))
    client = Client(model.network)
    client.run()
