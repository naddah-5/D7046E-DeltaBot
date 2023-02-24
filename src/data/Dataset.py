import pandas as pd
import torch


class DeltaDataset(torch.utils.data.Dataset):
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
    def __len__(self):
        return len(self.df)
    def __getitem__(self, index):
        helpfullness = self.df.iloc[index]['HelpfulnessScore']
        text = self.df.iloc[index]['Text']
        return text, helpfullness 