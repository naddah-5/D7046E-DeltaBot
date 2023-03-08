import numpy
import torch
from gensim.models import KeyedVectors

# Load embeddings from the pre-trained file
import gensim.downloader as api


class DeltaEmbedder:
    def __init__(self):
        pass
    
    def __call__(self,list : list, embedding_length : int) -> list:

        # Initate your embedding
        embedding = torch.zeros(embedding_length)
        
        # What do we loop over?
        for word in list:
            try:
                embedding += self.wv[word]
            except:
                pass
                    
        return embedding