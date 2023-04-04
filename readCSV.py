import csv
import numpy as np

def readNotes(path: str):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lenRow = 0
        for row in reader:
            lenRow = len(row)
            break
        if path == './resources/DatasetBW/oracle.csv':
            listeNotes = [[] for l in range(lenRow-2)]
            listeFinale = (lenRow-2)*[-1]
            for row in reader:
                for i in range(2,lenRow):
                    if row[i] != "":
                        listeNotes[i-2].append(int(row[i]))
            for i in range(lenRow-2):
                listeFinale[i] = np.mean(listeNotes[i])
        else:
            listeNotes = [[] for l in range(lenRow - 1)]
            listeFinale = (lenRow - 1) * [-1]
            for row in reader:
                for i in range(1, lenRow):
                    if row[i] != "":
                        listeNotes[i - 1].append(int(row[i]))
            for i in range(lenRow - 1):
                listeFinale[i] = np.mean(listeNotes[i])

    return listeFinale

"""
print((readNotes('./resources/dataset/Dataset/scores.csv')))

print((readNotes('./resources/DatasetBW/oracle.csv')))

print((readNotes('./resources/DatasetDorn/dataset/scores/cuda.csv')))
print((readNotes('./resources/DatasetDorn/dataset/scores/java.csv')))
print((readNotes('./resources/DatasetDorn/dataset/scores/python.csv')))
"""

