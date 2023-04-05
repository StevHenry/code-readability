import os
import csv
import numpy as np
import compute_metrics
from sklearn.utils import Bunch
from code_snippet import CodeSnippet, ProgrammingLanguage


def get_notes_from_file(path: str):
    """
    :param path: path of the scores file
    :return: a list of the mean score for each code snippet of the dataset
    """
    final_scores = []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        values_count_to_remove = 2 if './resources/DatasetBW/oracle.csv' else 1
        columns_count = 0
        for row in reader:
            if columns_count == 0:
                columns_count = len(row)
            row_scores = []
            for column in range(values_count_to_remove, columns_count):
                if row[column] != "":
                    row_scores.append(int(row[column]))
            final_scores.append(np.mean(row_scores).astype(float))
    return final_scores


def get_snippets_from_folder(path: str, dataset_language: ProgrammingLanguage) -> list[CodeSnippet]:
    """ 
    Instantiates code snippets object from all the files at the provided folder path
    :param path: dataset folder path 
    :param dataset_language: language of the snippets at the provided folder path
    :return: all the CodeSnippet objects
    """
    code_snippets = []
    files = os.listdir(path)
    sorted_files = sorted(files, key=lambda x: int(x.split('.')[0]))
    for file_name in sorted_files:
        with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
            code = CodeSnippet(dataset_language, file.read())
            code_snippets.append(code)
    return code_snippets


def compute_all_metrics():
    snippets = []
    snippets.extend(get_snippets_from_folder('./resources/dataset/Dataset/Snippets', ProgrammingLanguage.JAVA))
    snippets.extend(get_snippets_from_folder('./resources/DatasetBW/Snippets/java', ProgrammingLanguage.JAVA))
    snippets.extend(get_snippets_from_folder('./resources/DatasetDorn/dataset/snippets/cuda', ProgrammingLanguage.C))
    snippets.extend(get_snippets_from_folder('./resources/DatasetDorn/dataset/snippets/java', ProgrammingLanguage.JAVA))
    snippets.extend(get_snippets_from_folder('./resources/DatasetDorn/dataset/snippets/python',
                                             ProgrammingLanguage.PYTHON))
    for snippet in snippets:
        metrics = compute_metrics.get_all_metrics(snippet)



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
        elif note > 4:
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