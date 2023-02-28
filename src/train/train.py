import torch
import torch.nn as nn
import torch.optim as optim
import numpy

class Train():
    """
    Takes in the hyperparameters, dataset, and the network. 
    It then performs the training routine according to the settings.
    ### Parameters:
    loss_function: nn.CrossEntropyLoss = nn.CrossEntropyLoss()  
    batch_size: int = 10
    epochs: int = 1
    """
    def __init__(
            self,
            loss_function: nn.CrossEntropyLoss = nn.CrossEntropyLoss(),
            batch_size: int = 10, 
            epochs: int = 1) -> None:
        
        self.batches = batch_size
        self.epochs = epochs
        self.loss_function = loss_function
    
    def train(self, dataset, network: nn.Sequential, learning_rate: int):
        optimizer: torch.optim.Adam = torch.optim.Adam(network.parameters(), learning_rate)
        
        best_network = None
        best_accuracy = 0

        training_data = dataset.testData()
        validation_data = dataset.validationData()

        for epoch in range(self.epochs):
            for batch_nr, (data, labels) in enumerate(training_data):
                predictions = network(data)
                loss = self.loss_function(predictions, labels)
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()

                print(
                    f'\rEpoch {epoch+1} [{batch_nr+1}/{len(training_data)}] - Loss {loss}',
                    end=''
                    )
            print()
            with torch.no_grad():
                correct_prediction = 0
                total_predictions = 0
                for _, (data, labels) in enumerate(validation_data):
                    predictions = network(data)
                    predicted = list(prediction.argmax() for prediction in predictions)
                    correct_prediction += numpy.equal(predicted, labels).sum().item()
                    total_predictions += len(predicted)