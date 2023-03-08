import re
import nltk
import torch
from torch import nn
from src.data.delta_embedder import DeltaEmbedder



class Client():

    def __init__(self, model: nn.Sequential):
        self.model = model

    def run(self):
        delta_embedder = DeltaEmbedder()
        while True :
            review = input('Enter review: ')
            processed_review = self.pre_processing(review)
            embedded_review = delta_embedder(processed_review, embedding_length=300)
            with torch.no_grad():

                prediction = self.model(embedded_review)
                predicted = prediction.argmax()

                match predicted:
                    case 0:
                        print("I would suggest that you rephrase your comment as it does not seem very helpful.")
                    case 1:
                        print("Great job on your helpful comment!")

    def pre_processing(self, review: str) -> list:
        formattedString = re.sub('<.*?>', 'link', review)

        # Cleaning special character from the review
        review = re.sub(pattern='[^a-zA-Z]', repl=' ', string=formattedString)

        # Converting the entire review into lower case
        review = review.lower()

        # Tokenizing the review by words
        words = review.split()

        return words
