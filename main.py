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
    trainer = Train(epochs=10, batch_size=10)
    data = DeltaData(embedder=DeltaEmbedder(), embedding_size=300,csv_proceed_path="src/data/dataset/Processed_Data_2_medium.csv")

    neural_model.network = trainer.run_training(dataset=data, network=neural_model.network, learning_rate=0.001)
    neural_model.save_network('test_network.pt')

def test_gpu() -> None:
    print("\nis cuda available?", torch.cuda.is_available())
    print("currently", torch.cuda.device_count(), "devices are available")
    print("using device", torch.cuda.current_device())
    print("which is", torch.cuda.get_device_name(torch.cuda.current_device()))


if __name__=='__main__':
    #test_gpu()
    main()