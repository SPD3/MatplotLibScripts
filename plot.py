import sys
import matplotlib.pyplot as plt
import csv
import numpy as np

valuesForEachColumn = []
labels = []
allValuesForFiles = []
names = []
allfiles = sys.argv[1:]
for file in allfiles:
    valuesForEachColumn = []
    fileName = str(file)
    name = fileName.split("/")
    name = name[len(name) - 1]
    with open(file) as csvfile:
        plots = csv.reader(csvfile, delimiter=',')

        count = 0
        for row in plots:
            numberOfColumns = 0
            for column in range(len(row)):
                numberOfColumns += 1
                
                if(count == 0):
                    if len(allfiles) != 1:
                        labels.append(name + "/" + row[column])
                    else:
                        labels.append(row[column])
                    valuesForEachColumn.append([])
                    continue

                valuesForEachColumn[column].append(float(row[column]))
                
            count += 1
    
    names.append(name)
    allValuesForFiles.append(valuesForEachColumn)

fig, subplots = plt.subplots(len(allValuesForFiles), sharex=True, sharey=True, figsize=(10,10))
fig.set_tight_layout(True)
labelsCount = 0
filesCount = 0
for fileValues in allValuesForFiles:
    times = fileValues[0]
    allSetsOfYValues = fileValues[1:]
    subplot = subplots[filesCount]
    filesCount += 1
    subplot.set_xlabel(labels[labelsCount])
    labelsCount += 1
    for setOfYValues in allSetsOfYValues:
        subplot.plot(times, setOfYValues, label=labels[labelsCount])
        labelsCount += 1
    subplot.legend(loc="upper right")

title = names[0]
if len(names) > 1:
    count = 1
    for name in names[1:]:
        count+= 1
        if(count == len(names)):
            title += ", and " + name
        else:
            title += ", " + name
plt.title(title)
plt.show()
