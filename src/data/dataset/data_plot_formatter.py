import csv

def read_file(file_name: str) -> None:
    fileContent: list = []
    with open(file_name, 'r') as file:
        _ = file.readline()
        csvFile = csv.reader(file, delimiter=',', quotechar='"')
        for line in csvFile:
            helpfulnessNumerator = int(line[4])     # top
            helpfulnessDenominator = int(line[5])   # bot


            ratingScore = float(line[6])

            # Handle division by zero, purely for graphing.
            if helpfulnessDenominator == 0:
                helpfulnessRating = helpfulnessNumerator
            else:
                helpfulnessRating = helpfulnessNumerator/helpfulnessDenominator

            newLine = [helpfulnessRating, ratingScore]
            fileContent.append(newLine)

    with open('helpdistribution.csv', 'w') as file:
        csvFile = csv.writer(file, delimiter=',', quotechar='"')
        csvFile.writerow(["id"] + ["helpfulness"] + ["rating"])

        for line in range(len(fileContent)):
            csvFile.writerow([line] + [fileContent[line][0]] + [fileContent[line][1]])


if __name__ == '__main__':
    read_file('Reviews.csv')