import csv
import nltk
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#nltk.download('stopwords')


class DeltaCsvParser:
    def __init__(self, csv_path : str):
        self.data = []
        self.stemmer = PorterStemmer()
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            i=0
            for row in reader:
                data_row = {"Text": row["Text"], "HelpfulnessNumerator": row["HelpfulnessNumerator"], "HelpfulnessDenominator": row["HelpfulnessDenominator"]}
                i+=1
                if (int(data_row["HelpfulnessNumerator"]) <= int(data_row["HelpfulnessDenominator"])):
                    
                    print('\rRow : ',i,end="")

                    data_row["Text"] = self.pre_procesing(data_row["Text"])

                    helpfullnessscrore =  self.score_calculator(int(data_row['HelpfulnessNumerator']),int(data_row['HelpfulnessDenominator']))

                    self.data.append((data_row['Text'],helpfullnessscrore))

        
    def score_calculator(self,num : int,den :int )-> int:
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
        

    def pre_procesing(self, review : str)->list:

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

    def save(self, output_path : str) -> None:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Text", "HelpfulnessScore"])
            writer.writeheader()
            for text,helpfullness in self.data:
                writer.writerow({'Text':text,'HelpfulnessScore':helpfullness})