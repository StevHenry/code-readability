import csv
import numpy as np

def readNotes(path: str):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        lenRow = 122
        listeNotes = []

        for row in reader:
            for i in range(1, 122):
                matInt = [][122]
            if row[i] != "" :
                matInt[i].append(int(row[i]))

    print(listeNotes)
readNotes('./resources/DatasetDorn/dataset/scores/java.csv')