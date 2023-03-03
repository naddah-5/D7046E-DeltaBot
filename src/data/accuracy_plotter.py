import csv
import matplotlib.pyplot as plt


with open('src/data/Accuracy_and_loss.csv', 'r') as csvfile:

    data = csv.DictReader(csvfile)

    validation_accuracies = []
    training_accuracies = []

    for row in data:
        validation_accuracies.append(float(row['validation_accuracy']))
        training_accuracies.append(float(row['training_accuracy']))


plt.plot(validation_accuracies, label='Validation Accuracy')
plt.plot(training_accuracies, label='Training Accuracy')


plt.legend()
plt.show()