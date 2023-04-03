import csv
import numpy as np

def readNotes(path: str):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lenRow = 0
        for row in reader:
            lenRow = len(row)
            break
        listeNotes = [[] for l in range(lenRow-1)]
        listeFinale = (lenRow-1)*[-1]
        for row in reader:
            for i in range(1,lenRow):
                if row[i] != "":
                    listeNotes[i-1].append(int(row[i]))
    for i in range(lenRow-1):
        listeFinale[i] = np.mean(listeNotes[i])
    print(listeFinale)
    return listeFinale

readNotes('./resources/DatasetDorn/dataset/scores/java.csv')