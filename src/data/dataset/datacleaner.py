"""
Formats line[9] of CSV data to remove links and breaklines.
"""
import re
from data_plot_formatter import read_file
import csv

# format text on line 9 of dataset
def removeFormatting(file_name: str) -> None:
    fileContent: list = []
    with open(file_name, 'r') as file:
        _ = file.readline()
        csvFile = csv.reader(file, delimiter=',', quotechar='"')
        for line in csvFile:
            unformattedString = str(line[9])
            # removes html
            formattedString = re.sub('<.*?>', '', unformattedString)
            
            newLine = [line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], formattedString]

            fileContent.append(newLine)
        #print (fileContent)

    with open('Reviews_no_html.csv', 'w') as file:
        csvFile = csv.writer(file, delimiter=',', quotechar='"')

        for line in range(len(fileContent)):
            csvFile.writerow([line] + [fileContent[line][0]] + [fileContent[line][1]] + [fileContent[line][2]] + [fileContent[line][3]] + [fileContent[line][4]] + [fileContent[line][5]] + [fileContent[line][6]] + [fileContent[line][7]] + [fileContent[line][8]] + [fileContent[line][9]])


if __name__ == '__main__':
    removeFormatting("Reviews.csv")
    # read_file('Reviews.csv')