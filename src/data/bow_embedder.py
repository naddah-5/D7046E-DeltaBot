import torch
class BoWEmbedder:
    def __init__(self, word2idx):
        self.word2idx = word2idx
        self.vocab_size = len(word2idx)

    def __call__(self, sentence):
        bow = torch.zeros(self.vocab_size)
        for word in sentence:
            if word in self.word2idx:
                bow[self.word2idx[word]] += 1
        return bow
