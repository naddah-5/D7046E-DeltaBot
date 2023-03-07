import re
import nltk
import torch
from torch import nn
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from src.data.delta_embedder import DeltaEmbedder

nltk.download('stopwords')


class Client():

    def __init__(self, model: nn.Sequential):
        self.model = model
        self.stemmer = PorterStemmer()

    def run(self):
        review = input('Enter review: ')
        processed_review = self.pre_processing(review)
        delta_embedder = DeltaEmbedder()
        embedded_review = delta_embedder(processed_review, embedding_length=300)
        with torch.no_grad():

            prediction = self.model(embedded_review)
            predicted = prediction.argmax()

            match predicted:
                case 0:
                    print(0)
                case 1:
                    print(1)
                case 2:
                    print(2)

    def pre_processing(self, review: str) -> list:
        formattedString = re.sub('<.*?>', 'link', review)

        # Cleaning special character from the review
        review = re.sub(pattern='[^a-zA-Z]', repl=' ', string=formattedString)

        # Converting the entire review into lower case
        review = review.lower()

        # Tokenizing the review by words
        words = review.split()

        # Removing the stop words
        filtered_words = [word for word in words if word not in set(stopwords.words('english'))]

        stemmered_word = [self.stemmer.stem(word) for word in filtered_words]

        return stemmered_word
