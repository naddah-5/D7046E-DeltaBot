import torch
from DeltaCsvParser import DeltaCsvParser
from Dataset import DeltaDataset
from torch.utils.data import DataLoader

class DeltaData():
    # set a path if you want to create a new dataset
    def __init__(self, csv_source_path="",csv_proceed_path="",train_proportion =0.8,val_proportion=0.1,test_proportion=0.1):
        
        if (train_proportion+val_proportion+test_proportion) != 1:
            raise ValueError("Sum of proportion should be equal to 1")

        if(csv_proceed_path == ""):
            self.parser = DeltaCsvParser(csv_source_path)
            self.parser.save('src/data/dataset/Processed_Data.csv')
        
        self.dataset = DeltaDataset('src/data/dataset/Processed_Data.csv')
        

        self.train_size = int(len(self.dataset) * train_proportion)
        self.val_size = int(len(self.dataset) * val_proportion)
        self.test_size = len(self.dataset) -  self.train_size - self.val_size
        self.train,self.val,self.test = torch.utils.data.random_split(self.dataset, [self.train_size, self.val_size,self.test_size])

    def getTrainingSet(self):
        return self.train

    def getValidationSet(self):
        return self.val

    def getTestingSet(self):
        return self.test

if __name__ == "__main__":
    #data = DeltaData(csv_source_path='src/data/dataset/Reviews.csv')
    data = DeltaData(csv_proceed_path='src/data/dataset/Proceed_Data.csv')


    train_data = data.getTrainingSet()
    train_loader = DataLoader(train_data, batch_size=1000, shuffle=True)