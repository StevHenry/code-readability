from compute_metrics import *
from dataset_generator import *


snippets = []
file = open("./resources/DatasetDorn/dataset/snippets/python/5.jsnp", 'r', encoding="utf-8")
snippets.append(CodeSnippet(language=ProgrammingLanguage.PYTHON, original_text=file.read()))
file = open("./resources/DatasetDorn/dataset/snippets/java/106.jsnp", 'r', encoding="utf-8")
snippets.append(CodeSnippet(language=ProgrammingLanguage.JAVA, original_text=file.read()))
file = open("./resources/DatasetDorn/dataset/snippets/cuda/0.jsnp", 'r', encoding="utf-8")
snippets.append(CodeSnippet(language=ProgrammingLanguage.C, original_text=file.read()))


for index, snippet in enumerate(snippets):
    metrics = get_all_metrics(snippet)
    print(f"------\nComputing metrics of snippet: index={index}, language={snippet.language}")
    for key in metrics:
        print(f'{key}: {metrics[key]}')


print(get_classification_bunch(metrics=[CodeMetric.LINE_LENGTH_MAX]))
print(get_classification_bunch())
