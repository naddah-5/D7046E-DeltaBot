import csv
import nltk
import re


class DeltaCsvParser:
    def __init__(self, csv_path : str):
        self.data = []
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            i=0
            for row in reader:
                data_row = {"Text": row["Text"], "Score": row["Score"]}
                i+=1
                if(i%1000==0):
                    print('\rRow : ',i,end="")
                    if(i>10000):
                        break
                

                data_row["Text"] = self.pre_procesing(data_row["Text"])

                score =  self.score_calculator(int(data_row["Score"]))

                self.data.append((data_row['Text'],score))

        
    def score_calculator(self,num : int)-> int:
        
        if num <2.5:
            return 0
        else:
            return 1
        

    def pre_procesing(self, review : str)->list:

        formattedString = re.sub('<.*?>', 'link', review)

        # Cleaning special character from the review
        review = re.sub(pattern='[^a-zA-Z]', repl=' ', string=formattedString)

        # Converting the entire review into lower case
        review = review.lower()

        # Tokenizing the review by words
        words = review.split()
        
        return words

    def save(self, output_path : str) -> None:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["Text", "Score"])
            writer.writeheader()
            self.sample()
            for text,score in self.data:
                writer.writerow({'Text':text,'Score':score})

    def sample(self):
        count_0=0
        count_1=0
        data = []
        for text,score in self.data:
            if score == 0:
                count_0 +=1
            else :
                count_1 +=1
        mini = min(count_1,count_0)
        count_0=0
        count_1=0
        for text,score in self.data:
            if (score == 0 and count_0 < mini):
                data.append((text,score))
                count_0 +=1
            elif (score == 1 and count_1 < mini) :
                data.append((text,score))
                count_1 +=1
        self.data = data


#parser = DeltaCsvParser("src/data/dataset/Reviews.csv")
#parser.save("src/data/dataset/output.csv")
