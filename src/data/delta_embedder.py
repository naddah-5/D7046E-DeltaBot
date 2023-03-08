import numpy
import torch
from gensim.models import KeyedVectors

# Load embeddings from the pre-trained file
import gensim.downloader as api


class DeltaEmbedder:
    def init(self):
        self.wv = api.load('word2vec-google-news-300')

    def __call__(self,list : list, embedding_length : int):

        # Initate your embedding
        embedding = torch.zeros(embedding_length)
        list = list.replace("[","").replace("]","").replace(",","").replace("'","").split()
        # What do we loop over?
        for word in list:
            try:
                embedding += self.wv[word]/len(list)
            except:
                pass

        return embedding
