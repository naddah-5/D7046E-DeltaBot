import csv
import nltk
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class DeltaCsvParser:
    def __init__(self, csv_path : str):
        self.data = []
        self.stemmer = PorterStemmer()
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            i = 0
            for row in reader:
                
                # for examples
                if(i > 10) :
                    break
                i = i+1

                if row["HelpfulnessNumerator"] <= row["HelpfulnessDenominator"]:
                    data_row = {"Text": row["Text"], "HelpfulnessNumerator": row["HelpfulnessNumerator"], "HelpfulnessDenominator": row["HelpfulnessDenominator"]}

                    data_row["Text"] = self.preProcesing(data_row["Text"])

                    helpfullnessscrore =  self.scoreCalculator(int(data_row['HelpfulnessNumerator']),int(data_row['HelpfulnessDenominator']))

                    self.data.append((data_row['Text'],helpfullnessscrore))

        
    def scoreCalculator(self,num : int,den :int )-> int:
        if den == 0:
            return 0

        ratio = num/den
        if ratio <= 0.3:
            return 1
        elif 0.3 < ratio <= 0.4:
            return 2
        elif 0.4 < ratio <= 0.6:
            return 3
        elif 0.6 < ratio <= 0.7:
            return 4
        else:
            return 5
        

    def preProcesing(self, review : str)->list:
        # Cleaning special character from the review
        review = re.sub(pattern='[^a-zA-Z]', repl=' ', string=review)

        # Converting the entire review into lower case
        review = review.lower()

        # Tokenizing the review by words
        words = review.split()

        # Removing the stop words
        filtered_words = [word for word in words if word not in set(stopwords.words('english'))]

        stemmered_word = [self.stemmer.stem(word) for word in filtered_words]
        
        return stemmered_word

    def save(self, output_path : str) -> None:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Text", "HelpfulnessScore"])
            writer.writeheader()
            for text,helpfullness in self.data:
                writer.writerow({'Text':text,'HelpfulnessScore':helpfullness})