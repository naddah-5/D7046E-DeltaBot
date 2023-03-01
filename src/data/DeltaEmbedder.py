import numpy
import torch
from gensim.models import KeyedVectors

# Load embeddings from the pre-trained file
import gensim.downloader as api


class DeltaEmbedder:
    def __init__(self):
        self.wv = api.load('word2vec-google-news-300')
    
    def __call__(self,tensor : torch.tensor, embedding_length : int) -> list:

        # Initate your embedding
        embedding = torch.zeros(embedding_length)
        
        # What do we loop over?
        for word in tensor:
            try:
                embedding += self.wv[word]/len(tensor)
            except:
                pass
                    
        return embedding