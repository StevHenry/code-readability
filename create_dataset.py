import readCSV

from compute_metrics import *
import os
from code_snippet import CodeSnippet, ProgrammingLanguage
from readCSV import *


def data_features():
    listCodeFeatures = []
    #premier dataset
    fichiers = os.listdir('./resources/dataset/Dataset/Snippets')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/dataset/Dataset/Snippets/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r") as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.JAVA,codeContent)
            listCodeFeatures.append(returnMetrics(code))

    #deuxième dataset (BW)
    fichiers = os.listdir('./resources/DatasetBW/Snippets/java')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/DatasetBW/Snippets/java/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r") as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.JAVA,codeContent)
            listCodeFeatures.append(returnMetrics(code))

    # troisième dataset cuda (Dorn)
    fichiers = os.listdir('./resources/DatasetDorn/dataset/snippets/cuda')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/DatasetDorn/dataset/snippets/cuda/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r") as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.C, codeContent)
            listCodeFeatures.append(returnMetrics(code))

    # troisième dataset java (Dorn)
    fichiers = os.listdir('./resources/DatasetDorn/dataset/snippets/java')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/DatasetDorn/dataset/snippets/java/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r") as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.JAVA, codeContent)
            listCodeFeatures.append(returnMetrics(code))

    # troisième dataset python (Dorn)
    fichiers = os.listdir('./resources/DatasetDorn/dataset/snippets/python')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/DatasetDorn/dataset/snippets/python/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r") as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.PYTHON, codeContent)
            listCodeFeatures.append(returnMetrics(code))

def data_notes():
    notes = []
    for note in readCSV.readNotes('./resources/dataset/Dataset/scores.csv'):
        notes.append(note)
    for note in readCSV.readNotes('./resources/DatasetBW/oracle.csv'):
        notes.append(note)
    for note in readCSV.readNotes('./resources/DatasetDorn/dataset/scores/cuda.csv'):
        notes.append(note)
    for note in readCSV.readNotes('./resources/DatasetDorn/dataset/scores/java.csv'):
        notes.append(note)
    for note in readCSV.readNotes('./resources/DatasetDorn/dataset/scores/python.csv'):
        notes.append(note)
    return notes


#print("les notes sont", data_notes())
#print("la taille de la liste des notes sont", len(data_notes()))



def name_feature():
    names = ["number of lines", "number of Loops", "Lines length mean", "Comment lines per code line ",
             "Proportion of Blank Lines", "Proportion of good indentation", "Identifiers length (characters)",
             "Max streak of opening parentheses before a closing one", "Max streak of following periods"]
    return names

#print(name_feature())