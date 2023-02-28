import csv
import nltk
import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class DeltaCsvParser:
    def __init__(self, csv_path):
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
                
                data_row = {"Text": row["Text"], "HelpfulnessNumerator": row["HelpfulnessNumerator"], "HelpfulnessDenominator": row["HelpfulnessDenominator"]}

                data_row["Text"] = self.preProcesing(data_row["Text"])

                helpfullnessscrore =  self.scoreCalculator(int(data_row['HelpfulnessNumerator']),int(data_row['HelpfulnessDenominator'])) 
                
                self.data.append((data_row['Text'],helpfullnessscrore))
        
    def scoreCalculator(self,num,den):
        if num==den:
            return num
        else:
            return 2*num-den 
        

    def preProcesing(self, review):
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

    def save(self, output_path):
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Text", "HelpfulnessScore"])
            writer.writeheader()
            for text,helpfullness in self.data:
                writer.writerow({'Text':text,'HelpfulnessScore':helpfullness})
            
