import csv
from collections import Counter
from src.data.bow_embedder import BoWEmbedder
import torch
from torch.utils.data import Dataset

class BoWEmbedderDataset(Dataset):
    def __init__(self, csv_path, column_name = "HelpfulnessScore"):
        super().__init__()

        # Lecture du fichier CSV et comptage des mots
        self.sentences = []
        word_counts = Counter()
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sentence = row[column_name].split()
                self.sentences.append(sentence)
                word_counts.update(sentence)

        # Création du dictionnaire word2idx
        self.word2idx = {word: i for i, (word, count) in enumerate(word_counts.items())}

        # Création de l'embedder BoW
        self.embedder = BoWEmbedder(self.word2idx)

    def __len__(self):
        return len(self.sentences)

    def __getitem__(self, idx):
        sentence = self.sentences[idx]
        bow = self.embedder(sentence)
        return bow
