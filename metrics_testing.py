from compute_metrics import *

snippets = []
file = open("./resources/DatasetDorn/dataset/snippets/python/5.jsnp", 'r', encoding="utf-8")
snippets.append(CodeSnippet(language=ProgrammingLanguage.PYTHON, original_text=file.read()))
file = open("./resources/DatasetDorn/dataset/snippets/java/106.jsnp", 'r', encoding="utf-8")
snippets.append(CodeSnippet(language=ProgrammingLanguage.JAVA, original_text=file.read()))
file = open("./resources/DatasetDorn/dataset/snippets/cuda/0.jsnp", 'r', encoding="utf-8")
snippets.append(CodeSnippet(language=ProgrammingLanguage.C, original_text=file.read()))


for index, snippet in enumerate(snippets):
    print(f"------\nComputing metrics of snippet: index={index}, language={snippet.language}")
    print("number_of_loops: ", reg_number_of_loops(snippet))
    line_length = lines_length(snippet)
    print("Line length mean: ", line_length[0])
    print("Line length max: ", line_length[1])
    print("Comment lines per code lines: ", comment_line_per_code_line(snippet))
    print("Blank lines per code lines : ", blank_line_per_code_line(snippet))
    print("Indentation rate: ", indentation_mean(snippet))
    print("max_streak_opening_parentheses_py is : ", max_streak_opening_parentheses(snippet))
    print("max_streak_period is : ", max_streak_period(snippet))

