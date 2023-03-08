from collections import Counter
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
        helpfullness = self.df.iloc[index]['HelpfulnessScore']
        text = self.df.iloc[index]['Text']
        return self.embedder(text, self.embedding_size), helpfullness 
    


class BoWDataset(Dataset):
    def __init__(self, csv_path):
        super().__init__()
        self.data = pd.read_csv(csv_path)
        self.word2idx = self.build_vocab()
        self.idx2word = {idx: word for word, idx in self.word2idx.items()}
        self.vocab_size = len(self.word2idx)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sentence = self.data[idx]
        bow = torch.zeros(self.vocab_size)
        for word in sentence:
            bow[self.word2idx[word]] += 1
        return bow

    def build_vocab(self):
        words = [word for sentence in self.data["Text"] for word in sentence]
        word_counts = Counter(words)
        word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        word2idx = {word: idx for idx, (word, _) in enumerate(word_counts)}
        return word2idx