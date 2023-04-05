import readCSV
from compute_metrics import *
import os
from code_snippet import CodeSnippet, ProgrammingLanguage
from readCSV import *
from sklearn.utils import Bunch


def data_features():
    listeNotesFeatures = []
    #premier dataset
    fichiers = os.listdir('./resources/dataset/Dataset/Snippets')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/dataset/Dataset/Snippets/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r", encoding='utf-8') as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.JAVA,codeContent)
            listeNotesFeatures.append(returnMetrics(code))

    #deuxième dataset (BW)
    fichiers = os.listdir('./resources/DatasetBW/Snippets/java')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/DatasetBW/Snippets/java/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r", encoding='utf-8') as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.JAVA,codeContent)
            listeNotesFeatures.append(returnMetrics(code))

    # troisième dataset cuda (Dorn)
    fichiers = os.listdir('./resources/DatasetDorn/dataset/snippets/cuda')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/DatasetDorn/dataset/snippets/cuda/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r", encoding='utf-8') as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.C, codeContent)
            listeNotesFeatures.append(returnMetrics(code))

    # troisième dataset java (Dorn)
    fichiers = os.listdir('./resources/DatasetDorn/dataset/snippets/java')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/DatasetDorn/dataset/snippets/java/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r", encoding='utf-8') as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.JAVA, codeContent)
            listeNotesFeatures.append(returnMetrics(code))

    # troisième dataset python (Dorn)
    fichiers = os.listdir('./resources/DatasetDorn/dataset/snippets/python')
    fichiers_tries = sorted(fichiers, key=lambda x: int(x.split('.')[0]))
    for fileName in fichiers_tries:
        path = './resources/DatasetDorn/dataset/snippets/python/' + fileName
        # Ouvrir le fichier en mode lecture
        with open(path, "r", encoding='utf-8') as fichier:
            # Lire tout le contenu du fichier
            codeContent = fichier.read()
            # Afficher le contenu du fichier
            code = CodeSnippet(ProgrammingLanguage.PYTHON, codeContent)
            listeNotesFeatures.append(returnMetrics(code))
    return listeNotesFeatures

#print(f"liste des notes des métriques : {data_features()}")
#print(f"la taille de la liste des notes des métriques : {len(data_features())}")
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
#print("la taille de la liste des notes est", len(data_notes()))

def data_notes_classification():
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
    for i, note in enumerate(notes):
        if note < 3:
            notes[i]="très peu lisible"
        elif note < 4:
            notes[i]= "plutôt lisible"
        elif note >= 4:
            notes[i] = "très lisible"
    return notes

"""
test répartition classification :

notes=data_notes_classification()
i = 0
j=0
k=0
for note in notes:
    if note < 3:
        i+=1
    elif note < 4:
        j+=1
    elif note > 4:
        k+=1
print(i)
print(j)
print(k)
"""


def name_feature():
    names = ["number of lines", "number of Loops", "Lines length mean", "Lines length max",
             "comments line per code line", "Proportion of Blank Lines", "Identifiers length (characters)",
             "Max streak of opening parentheses before a closing one", "Max streak periods"]
    return names

#print("le nom des features sont : ",name_feature())



# Create numpy arrays for data, target, and feature_names
data = np.array(data_features())
target = np.array(data_notes())
feature_names = np.array(name_feature())

target_classification = data_notes_classification()
# Create a Bunch object
def create_bunch():
    return Bunch(data=data, target=target, feature_names=feature_names, DESCR='My data')


def create_bunch_classification():
    return Bunch(data=data, target=target_classification, feature_names=feature_names, DESCR='My data classification')


if __name__ == '__main__':
    print(create_bunch())