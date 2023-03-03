import csv
import matplotlib.pyplot as plt


with open('src/data/Accuracy_and_loss.csv', 'r') as csvfile:

    data = csv.DictReader(csvfile)

    validation_losses = []
    training_losses = []

    for row in data:
        validation_losses.append(float(row['validation_loss']))
        training_losses.append(float(row['training_loss']))


plt.plot(validation_losses, label='Validation loss')
plt.plot(training_losses, label='Training loss')


plt.legend()
plt.show()