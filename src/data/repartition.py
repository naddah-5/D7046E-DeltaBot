import csv
import matplotlib.pyplot as plt

with open("src/data/dataset/Reviews.csv", 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            i = 0
            x_serie = []
            y_serie = []
            for row in reader:
                
                # for examples
                
                
                y = int(row["HelpfulnessNumerator"]) / int(row["HelpfulnessDenominator"]) if int(row["HelpfulnessDenominator"]) !=0 else 0
                x = int(row["HelpfulnessDenominator"])
                if(x!=y):
                    x_serie.append(x)
                    y_serie.append(y)

            plt.plot(x_serie, y_serie,'bo')

            # add labels to the axes
            plt.ylabel('HelpfulnessNumerator')
            plt.xlabel('HelpfulnessDenominator')

            plt.show()
            
