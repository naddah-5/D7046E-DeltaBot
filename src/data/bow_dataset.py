import csv

import nltk
from nltk import word_tokenize
from torch.utils.data import Dataset
import numpy as np

#nltk.download('punkt')

class BoWEmbedderDataset(Dataset):
    def __init__(self, x, y):
        self.samples = len(x)
        self.x = x
        self.y = y

    def __getitem__(self, index):
        return self.x[index], self.y[index]

    def __len__(self):
        return self.samples
    
def read_file_to_tensor_and_vocab(file_path):
    data = []  # Contains sentence and class pairs (sentence as list of words)
    vocab = set()

    crow = 0
    with open(file_path, "r", encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            crow = crow + 1
            if crow % 100 == 0:
                print(f'Rows read: [{crow}]')
            message = row["Text"]
            label = row["HelpfulnessScore"]
            data.append((message, int(label)))
            vocab.update(message)
    
    vocab = list(dict.fromkeys(vocab))
    vocab = sorted(list(vocab))  # Contains all words from the file as single words and without duplicates

    x_train = []
    y_train = []
    ti = 0
    for (tokenized_sentence, label) in data:
        ti = ti + 1
        if ti % 1000 == 0:
            print(f'Tokenized sentences: [{ti}]')
        bow = bow_embedder(tokenized_sentence, vocab)
        x_train.append(bow)
        y_train.append(label)

    return np.array(x_train), np.array(y_train), vocab


def bow_embedder(tokenized_sentence, vocab):
    bow = np.zeros(len(vocab), dtype=np.float32)
    for index, word in enumerate(vocab):
        if word in tokenized_sentence:
            bow[index] = 1
    return bow