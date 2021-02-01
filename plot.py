import sys
import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.widgets import Button


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
                    labels.append(row[column])
                    valuesForEachColumn.append([])
                    continue

                valuesForEachColumn[column].append(float(row[column]))
                
            count += 1
    
    names.append(name)
    allValuesForFiles.append(valuesForEachColumn)

def plotAllDataSeparately():
    plt.clf()
    subplotRows = (int) (len(allValuesForFiles) ** 0.5)
    subPlotColumns = (int) (len(allValuesForFiles) / subplotRows)
    if(subplotRows * subPlotColumns < len(allValuesForFiles)):
        subPlotColumns += 1

    fig, subplots = plt.subplots(subplotRows, subPlotColumns, figsize=(16, 7.5))
    fig.set_tight_layout(True)
    labelsCount = 0
    filesCount = 0
    column = 0
    row = 0
    for fileValues in allValuesForFiles:
        times = fileValues[0]
        allSetsOfYValues = fileValues[1:]
        if(subplotRows == 1 and subPlotColumns == 1):
            subplot = subplots
        elif(subplotRows == 1): 
            subplot = subplots[column]
        else:
            subplot = subplots[row, column]
        row += 1
        if(row >= subplotRows):
            row = 0
            column += 1
        subplot.title.set_text(names[filesCount])
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

    fig.canvas.set_window_title(title)

def plotAllDataTogether():
    


global separatePlots 
separatePlots = True

def toggleMultiPlots():
    if(separatePlots):
        plotAllDataTogether()
        separatePlots = False
    else:
        plotAllDataSeparately()
        separatePlots = True
axcut = plt.axes([0.925, 0.0, 0.075, 0.03])
overlayPlotsButton = Button(axcut, "OverlayToggle")
overlayPlotsButton.on_clicked(toggleMultiPlots())



plt.show()
