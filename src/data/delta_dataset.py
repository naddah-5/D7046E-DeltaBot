from collections import Counter
import pandas as pd
import torch
from src.data.bow_dataset import BoWEmbedderDataset
from src.data.bow_dataset import read_file_to_tensor_and_vocab


class DeltaDataset(torch.utils.data.Dataset):
    def __init__(self, csv_path, embedder, embedding_size):
        self.embedder = embedder
        self.embedding_size = embedding_size
        x_train, y_train, self.vocab = read_file_to_tensor_and_vocab(csv_path)
        self.dataset = BoWEmbedderDataset(x_train, y_train)
    def __len__(self):
        return len(self.df)
    def __getitem__(self, index : int ):
        helpfullness = self.df.iloc[index]['HelpfulnessScore']
        text = self.df.iloc[index]['Text']
        return self.embedder(text, self.embedding_size), helpfullness 
    


