"""
Main file, the orchestrator.
"""
from src.model.neural_model import NeuralModel
from src.train.trainer import Train
from src.data.data import DeltaData
from src.data.delta_embedder import DeltaEmbedder
import torch

def main():
    """
    Orchestrator for running our training.
    """
    DATASET_PATH='src/data/dataset/Reviews.csv'
    neural_model = NeuralModel()
    trainer = Train(epochs=3)
    data = DeltaData(embedder=DeltaEmbedder(), embedding_size=300,csv_proceed_path="src/data/Processed_Data.csv")

    trainer.run_training(dataset=data, network=neural_model.network)

def test_gpu() -> None:
    print("\nis cuda available?", torch.cuda.is_available())
    print("currently", torch.cuda.device_count(), "devices are available")
    print("using device", torch.cuda.current_device())
    print("which is", torch.cuda.get_device_name(torch.cuda.current_device()))


if __name__=='__main__':
    #test_gpu()
    main()