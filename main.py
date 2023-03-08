"""
Main file, the orchestrator.
"""
from src.model.neural_model import NeuralModel
from src.train.trainer import Train
from src.data.bow_dataset import read_file_to_tensor_and_vocab
from src.data.bow_dataset import BoWEmbedderDataset
import torch

def main():
    """
    Orchestrator for running our training.
    """
    DATASET_PATH='src/data/dataset/Reviews.csv'
    
    trainer = Train(epochs=20, batch_size=10)
    x_train, y_train, vocab = read_file_to_tensor_and_vocab("src/data/dataset/sampled_dataset.csv")
    dataset = BoWEmbedderDataset(x_train, y_train)
    neural_model = NeuralModel(embedding_length=len(vocab))

    neural_model.network = trainer.run_training(dataset=dataset, network=neural_model.network, learning_rate=0.001,batch_size = 10)

    neural_model.save_network('test_network.pt')

def test_gpu() -> None:
    print("\nis cuda available?", torch.cuda.is_available())
    print("currently", torch.cuda.device_count(), "devices are available")
    print("using device", torch.cuda.current_device())
    print("which is", torch.cuda.get_device_name(torch.cuda.current_device()))


if __name__=='__main__':
    #test_gpu()
    main()