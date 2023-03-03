
import torch
import torch.nn as nn
import torch.optim as optim
import numpy
import copy


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
        
        self.batch_size = batch_size
        self.epochs = epochs
        self.loss_function = loss_function
        self.best_network = None
        self.best_accuracy = 0
    

    def runTraining(self, dataset, network: nn.Sequential, learning_rate: int):
        optimizer: torch.optim.Adam = torch.optim.Adam(network.parameters(), learning_rate)
        
        training_data = dataset.get_training_loader(batch_size=self.batch_size,shuffle = True)
        validation_data = dataset.get_validation_loader(batch_size=self.batch_size,shuffle = False)

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
                correct_prediction: int = 0
                total_predictions: int = 0

                for _, (data, labels) in enumerate(validation_data):
                    predictions = network(data)
                    predicted = list(prediction.argmax() for prediction in predictions)
                    correct_prediction += numpy.equal(predicted, labels).sum().item()
                    total_predictions += len(predicted)

                    accuracy = correct_prediction/total_predictions
                    print(f'\rThe accuracy of the model is {str(correct_prediction/total_predictions)[:4]}%.')
                print()

                if accuracy > self.best_accuracy:
                    print("Storing model")
                    self.best_network = copy.deepcopy(network.state_dict())
                    self.best_accuracy = accuracy

    def test_training(self, dataset, network: nn.Sequential):

        testing_data = dataset.get_testing_loader(batch_size=self.batch_size,shuffle = False)

        with torch.no_grad():
                correct_prediction: int = 0
                total_predictions: int = 0

                for _, (data, labels) in enumerate(testing_data):
                    predictions = network(data)
                    predicted = list(prediction.argmax() for prediction in predictions)
                    correct_prediction += numpy.equal(predicted, labels).sum().item()
                    total_predictions += len(predicted)

                    accuracy = correct_prediction/total_predictions
                    print(f'\rThe accuracy of the model is {str(accuracy)[:4]}%.')
                print()
