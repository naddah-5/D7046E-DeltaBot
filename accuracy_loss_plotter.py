import csv
import matplotlib.pyplot as plt

def plot_data():
    with open('src/data/Accuracy_and_loss.csv', 'r') as csvfile:

        data = csv.DictReader(csvfile)

        validation_accuracies = []
        training_accuracies = []

        validation_losses = []
        training_losses = []

        for row in data:
            validation_accuracies.append(float(row['validation_accuracy']))
            training_accuracies.append(float(row['training_accuracy']))

            validation_losses.append(float(row['validation_loss']))
            training_losses.append(float(row['training_loss']))


    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.plot(validation_accuracies, label='Validation Accuracy')
    ax1.plot(training_accuracies, label='Training Accuracy')

    ax2.plot(validation_losses, label='Validation loss')
    ax2.plot(training_losses, label='Training loss')

    ax1.legend()
    ax2.legend()
    plt.show()


if __name__=='__main__':
    plot_data()