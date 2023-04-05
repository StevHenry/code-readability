import os
import csv
import numpy as np
from numpy import ndarray

import compute_metrics
from sklearn.utils import Bunch
from code_snippet import CodeSnippet, ProgrammingLanguage
from code_metric import ReadibilityClass, CodeMetric, IMPLEMENTED_METRICS


def _get_scores_from_file(path: str, lines_count_to_skip: int, columns_count_to_skip: int) -> list[float]:
    """
    :param path: path of the scores file
    :param lines_count_to_skip: Number of lines at the beggining of the file to skip
    :param columns_count_to_skip: Number of columns to skip when counting the values
    :return: a list of the mean score for each code snippet of the dataset
    """

    scores_per_column = []
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        rows = list(reader)
        column_scores = [list() for _ in range(len(rows[0]) - columns_count_to_skip)]

        for row in rows[lines_count_to_skip:]:
            for column in range(columns_count_to_skip, len(row)):
                if row[column] != "":
                    column_scores[column - columns_count_to_skip].append(float(row[column]))

        for score in column_scores:
            scores_per_column.append(float(np.mean(score)))
    return scores_per_column


def _convert_scores_to_classes(scores: list[float]) -> list[str]:
    """
    Converts a list of floats into a list of ReadabilityClass
    x<3: NOT_VERY_READABLE, 3<x<4: QUITE_READABLE, x>=4: FULLY_READABLE
    :param scores: Scores to convert into classes
    :return: a new list of class associated scores
    """
    class_scores = []
    for score in scores:
        if score < 3:
            class_scores.append(ReadibilityClass.NOT_VERY_READABLE.name)
        elif score < 4:
            class_scores.append(ReadibilityClass.QUITE_READABLE.name)
        else:
            class_scores.append(ReadibilityClass.FULLY_READABLE.name)
    return class_scores


def _get_snippets_from_folder(path: str, dataset_language: ProgrammingLanguage) -> list[CodeSnippet]:
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


def _get_dataset_list(is_classification: bool, metrics: list[CodeMetric]) -> tuple[ndarray, ndarray, ndarray]:
    """
    :param metrics: list of wanted metrics
    :param is_classification: Whether the dataset is for classification
    :return: a tuple of the metrics, the scores and the feature names
    """
    snippets = []
    snippets.extend(_get_snippets_from_folder('./resources/dataset/Dataset/Snippets', ProgrammingLanguage.JAVA))
    snippets.extend(_get_snippets_from_folder('./resources/DatasetBW/Snippets/java', ProgrammingLanguage.JAVA))
    snippets.extend(_get_snippets_from_folder('./resources/DatasetDorn/dataset/snippets/cuda', ProgrammingLanguage.C))
    snippets.extend(_get_snippets_from_folder('./resources/DatasetDorn/dataset/snippets/java', ProgrammingLanguage.JAVA))
    snippets.extend(_get_snippets_from_folder('./resources/DatasetDorn/dataset/snippets/python',
                                              ProgrammingLanguage.PYTHON))

    scores = []
    scores.extend(_get_scores_from_file('./resources/dataset/Dataset/scores.csv', 1, 1))
    scores.extend(_get_scores_from_file('./resources/DatasetBW/oracle.csv', 0, 2))
    scores.extend(_get_scores_from_file('./resources/DatasetDorn/dataset/scores/cuda.csv', 0, 1))
    scores.extend(_get_scores_from_file('./resources/DatasetDorn/dataset/scores/java.csv', 0, 1))
    scores.extend(_get_scores_from_file('./resources/DatasetDorn/dataset/scores/python.csv', 0, 1))
    classes = _convert_scores_to_classes(scores)

    snippets_data = [[compute_metrics.get_metric(metric, snippet) for metric in metrics] for snippet in snippets]

    feature_names = [metric.name for metric in metrics]
    return (np.array(snippets_data),
            np.array(classes if is_classification else scores),
            np.array(feature_names))


# Create a Bunch object
def get_regression_bunch(metrics: list[CodeMetric] = IMPLEMENTED_METRICS):
    """
    :param metrics: list of wanted metrics, None => All metrics
    :return: A Bunch object of the generated dataset for a regression model
    """
    data, targets, feature_names = _get_dataset_list(False, metrics)
    return Bunch(data=data, target=targets, feature_names=feature_names,
                 DESCR='Regression dataset with all the metrics')


def get_classification_bunch(metrics: list[CodeMetric] = IMPLEMENTED_METRICS):
    """
    :param metrics: list of wanted metrics, None => All metrics
    :return: A Bunch object of the generated dataset for a classification model
    """
    data, targets, feature_names = _get_dataset_list(True, metrics)
    return Bunch(data=data, target=targets, feature_names=feature_names,
                 DESCR='Classification dataset with all the metrics')
