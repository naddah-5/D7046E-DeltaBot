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


# takes csv file and outputs a counted list of ratings
def getRatingsAsCountedAmounts(file_name: str) -> list:
    ratingList = [0, 0, 0, 0, 0]
    with open(file_name, 'r') as file:
        next(file)
        csvFile = csv.reader(file, delimiter=',', quotechar='"')
        for line in csvFile:
            rating = float(line[2])
            match rating:
                case 1.0:
                    ratingList[0] = ratingList[0]+1

                case 2.0:
                    ratingList[1] = ratingList[1]+1

                case 3.0:
                    ratingList[2] = ratingList[2]+1

                case 4.0:
                    ratingList[3] = ratingList[3]+1

                case 5.0:
                    ratingList[4] = ratingList[4]+1

                case _:
                    print("rating data is corrupt")
                    break
    return ratingList



# picks out ratings from CSV
# useful for histograms
def getRatingsAsList(file_name: str) -> list:
    ratingList = []
    with open(file_name, 'r') as file:
        next(file)
        csvFile = csv.reader(file, delimiter=',', quotechar='"')
        for line in csvFile:
            ratingList.append(line[2])
    return ratingList
    

if __name__ == '__main__':
    read_file('Reviews.csv')