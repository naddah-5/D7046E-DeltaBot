"""
DEPRICATED: can be modified to clean out other data.
"""

def read_file(file_name: str) -> None:
    fileContent: list = []
    header = []
    with open(file_name, 'r') as file:
        header = file.readline()
        count = 1
        for line in file:
            splitLine = line.split(',')
            broken: bool = False
            trigger = splitLine[4]
            if count < 210 and count > 190:
                print(line)
            for i in trigger:
                char = ord(i)
                # if char is not a digit
                if char < 48 or char > 57:
                    broken = True
            if not broken:
                fileContent.append(line)
            count += 1
    
    with open('new_data.csv', 'w') as file:
        file.write(header)
        for line in range(len(fileContent)):
            file.write(fileContent[line])


if __name__ == '__main__':
    read_file('Reviews.csv')