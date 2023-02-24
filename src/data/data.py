from numpy import shape
import torch
from DeltaCsvParser import DeltaCsvParser
import pandas as pd
import seaborn as sns
from Dataset import DeltaDataset
from fast_ml.model_development import train_valid_test_split

if __name__ == "__main__":
    """
    parser = DeltaCsvParser('src/data/dataset/Reviews.csv')
    parser.save('src/data/dataset/Processed_Data.csv')
    """
    dataset = DeltaDataset('src/data/dataset/Processed_Data.csv')

    train_size = int(len(dataset) * 0.8)
    val_size = int(len(dataset) * 0.1)
    test_size = len(dataset) -  train_size - val_size
    train,val,test = torch.utils.data.random_split(dataset, [train_size, val_size,test_size])

    print(shape(train))
