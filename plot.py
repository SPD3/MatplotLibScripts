import sys
import matplotlib.pyplot as plt
import csv
import numpy as np

valuesForEachColumn = []
labels = []

with open(sys.argv[1]) as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    count = 0
    for row in plots:
        numberOfColumns = 0
        for column in range(len(row)):
            numberOfColumns += 1
            
            if(count == 0):
                labels.append(row[column])
                valuesForEachColumn.append([])
                continue

            valuesForEachColumn[column].append(float(row[column]))
            
        count += 1

times = valuesForEachColumn[0]
allSetsOfYValues = valuesForEachColumn[1:]
count = 1

plt.figure(figsize=(16, 7.5), tight_layout=True)

for setOfYValues in allSetsOfYValues:
    plt.plot(times, setOfYValues, label=labels[count])
    count += 1

plt.xlabel(labels[0])
plt.legend()
plt.show()
