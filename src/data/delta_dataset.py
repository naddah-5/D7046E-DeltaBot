import pandas as pd
import torch


class DeltaDataset(torch.utils.data.Dataset):
    def __init__(self, csv_path, embedder, embedding_size):
        self.df = pd.read_csv(csv_path)
        self.embedder = embedder
        self.embedding_size = embedding_size
    def __len__(self):
        return len(self.df)
    def __getitem__(self, index : int ):
        score = self.df.iloc[index]['Score']
        text = self.df.iloc[index]['Text']
        return self.embedder(text, self.embedding_size), score 