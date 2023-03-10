"""
Training module.
"""
import copy
import numpy
import torch
import torch.nn as nn
from src.data.data import DeltaData
import csv


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

    def run_training(self, dataset: DeltaData, network: nn.Sequential, learning_rate: float = 0.0001):
        """
        Method for training the specified model.
        """
        self.best_network = network.state_dict()
        loss_function = nn.CrossEntropyLoss()

        optimizer: torch.optim.Adam = torch.optim.Adam(network.parameters(), learning_rate)

        training_data = dataset.get_training_loader(batch_size=self.batch_size, shuffle=True)
        validation_data = dataset.get_validation_loader(batch_size=self.batch_size, shuffle=False)

        validation_accuracies = []
        training_accuracies = []
        validation_losses = []
        training_losses = []
        for epoch in range(self.epochs):

            batch_training_accuracies = []
            batch_validation_accuracies = []
            batch_training_losses = []
            batch_validation_losses = []

            correct_prediction: int = 0
            total_predictions: int = 0

            for batch_nr, (data, labels) in enumerate(training_data):
                predictions = network(data)
                loss = loss_function(predictions, labels)
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()

                predicted = list(prediction.argmax() for prediction in predictions)
                correct_prediction += numpy.equal(predicted, labels).sum().item()
                total_predictions += len(predicted)
                accuracy = correct_prediction / total_predictions * 100

                batch_training_accuracies.append(accuracy)
                batch_training_losses.append(loss.item())
                if (batch_nr % 10 == 0):
                    print(
                        f'\rEpoch {epoch + 1} [{batch_nr + 1}/{len(training_data)}] - Loss {loss}',
                        end=''
                    )
            print()
            correct_prediction: int = 0
            total_predictions: int = 0

            for batch_nr, (data, labels) in enumerate(validation_data):
                predictions = network(data)
                predicted = list(prediction.argmax() for prediction in predictions)
                correct_prediction += numpy.equal(predicted, labels).sum().item()
                total_predictions += len(predicted)

                accuracy = correct_prediction / total_predictions * 100
                loss = self.loss_function(predictions, labels)

                batch_validation_accuracies.append(accuracy)
                batch_validation_losses.append(loss.item())

                print(f'\rThe accuracy of the model is {accuracy}', end='')
            print()

            if accuracy > self.best_accuracy:
                print("Storing model")
                self.best_network = copy.deepcopy(network)
                self.best_accuracy = accuracy

            validation_accuracies.append(sum(batch_validation_accuracies) / len(batch_validation_accuracies))
            training_accuracies.append(sum(batch_training_accuracies) / len(batch_training_accuracies))

            validation_losses.append(sum(batch_validation_losses) / len(batch_validation_losses))
            training_losses.append(sum(batch_training_losses) / len(batch_training_losses))

        with open('src/data/Accuracy_and_loss.csv', 'w') as f:

            csv_writer = csv.writer(f)
            csv_writer.writerow(['validation_accuracy', 'training_accuracy', 'validation_loss', 'training_loss'])

            result = []
            for i in range(len(validation_accuracies)):
                result.append(
                    [validation_accuracies[i], training_accuracies[i], validation_losses[i], training_losses[i]])

            csv_writer.writerows(result)

        self.test_training(dataset=dataset, network=self.best_network)

        return self.best_network

    def test_training(self, dataset: DeltaData, network: nn.Sequential):
        """
        Method for running the test dataset on our model.
        """

        testing_data = dataset.get_testing_loader(batch_size=self.batch_size, shuffle=False)

        with torch.no_grad():
            correct_prediction: int = 0
            total_predictions: int = 0

            for _, (data, labels) in enumerate(testing_data):
                predictions = network(data)
                predicted = list(prediction.argmax() for prediction in predictions)
                correct_prediction += numpy.equal(predicted, labels).sum().item()
                total_predictions += len(predicted)

                accuracy = correct_prediction / total_predictions * 100
                print(f'\rThe accuracy of the model is {str(accuracy)[:4]}.', end="")
            print()
