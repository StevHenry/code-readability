import sys
import re
import numpy as np
from code_snippet import CodeSnippet, ProgrammingLanguage

if __name__ == '__main__':
    """ program parameters: files to compute """
    arguments = sys.argv
    if len(arguments) != 0:
        files = arguments
    else:
        files = ['./resources/DatasetDorn/dataset/snippets/python/0.jsnp']


def returnMetrics(code: CodeSnippet) -> tuple:
    code.LN = reg_number_of_lines(code) #test OK
    code.LC = reg_number_of_loops(code) #test OK
    code.AvgLL = lines_length(code)[0] #test OK
    code.MaxLL = lines_length(code)[1]  #test OK
    code.CL = comment_line_per_code_line(code)
    code.BL = blank_line_per_code_line(code) #test OK
    code.ID = indentation_mean(code) #test ok
    code.PA = max_streak_opening_parentheses(code) #test OK
    #code.FP = max_streak_period(code)
    return code.LN, code.LC, code.AvgLL, code.MaxLL, code.CL, code.BL, code.ID, code.PA


def reg_number_of_lines(code: CodeSnippet):
    x = re.findall("\n", code.get_code(True, True))
    return len(x)


def reg_number_of_loops(code: CodeSnippet):
    forwhile_re = re.compile(r'(?<!\S)(for|while)', re.MULTILINE)
    return len(forwhile_re.findall(code.get_code(False, False)))


def lines_length(code: CodeSnippet):
    lines = code.get_code(True, True).split('\n')
    list_length = []
    for line in lines:
        if line.replace(" ", "") != '':  # vérifie que la ligne n'est pas vide ou ne contient pas que des espaces car sinon cela fausse la moyenne
            list_length.append(len(line))
    return np.mean(list_length), np.max(list_length)


def comment_line_per_code_line(code: CodeSnippet):
    comments_size = 0
    for com in code.code_comments:
        comments_size = comments_size + len(com.split('\n'))
    code_no_comments = code.get_code(True, False).split('\n')
    return comments_size / reg_number_of_lines(code)


def blank_line_per_code_line(code: CodeSnippet):
    lines = code.get_code(True, True).split('\n')
    blank_line = []
    for line in lines:
        if line.replace(" ", "") == '':
            blank_line.append(line)
    return len(blank_line) / len(lines)


def indentation_mean(code : CodeSnippet):
    if code.language == ProgrammingLanguage.PYTHON:
        return 2
    codelines = code.get_code(False,False)
    ctr = 0
    for car in (codelines):
        if car == '\t':
            ctr += 1
    return ctr / reg_number_of_lines(code)


def max_streak_opening_parentheses(code: CodeSnippet):
    count = 0
    max_count = 0
    for character in code.get_code(False, False):
        if character == "(":
            count += 1
        elif character == ")":
            if count > max_count:
                max_count = count
            count = 0
            continue
    return max_count

"""
def max_streak_period(code):
    period_regex = r"(\w+(\(.*\))?)([\.]{1}\1?)+"
    list_mot = re.findall(period_regex, code)
    print(list_mot)
"""


file = open("./resources/DatasetDorn/dataset/snippets/python/5.jsnp", 'r', encoding="utf-8")
snippetPython = file.read()
codeSnippetPython = CodeSnippet(language=ProgrammingLanguage.PYTHON, original_text=snippetPython)

file = open("./resources/DatasetDorn/dataset/snippets/java/102.jsnp", 'r', encoding="utf-8")
snippetJava = file.read()
codeSnippetJava = CodeSnippet(language=ProgrammingLanguage.JAVA, original_text=snippetJava)

file = open("./resources/DatasetDorn/dataset/snippets/cuda/0.jsnp", 'r', encoding="utf-8")
snippetCuda = file.read()
codeSnippetCuda = CodeSnippet(language=ProgrammingLanguage.C, original_text=snippetCuda)

# test_value_comments_readability = comments_readability(snippet1)
# print("value_comments_readability is : ", test_value_comments_readability)
"""
test_number_of_lines = reg_number_of_lines(codeSnippet1)
print("number_of_lines is : ", test_number_of_lines)


test_number_of_loops_python = reg_number_of_loops(codeSnippetPython)
print("number_of_loops for python snippet is : ",test_number_of_loops_python)

test_number_of_loops_cuda = reg_number_of_loops(codeSnippetCuda)
print("number_of_loops for cuda snippet is : ",test_number_of_loops_cuda)

test_number_of_loops_java = reg_number_of_loops(codeSnippetJava)
print("number_of_loops for java snippet is : ",test_number_of_loops_java)


test_lines_length_mean_Py = lines_length(codeSnippetPython)[0]
print("lines_length_mean Python is : ",test_lines_length_mean_Py)

test_lines_length_mean_java = lines_length(codeSnippetJava)[0]
print("lines_length_mean Java is : ",test_lines_length_mean_java)

test_lines_length_mean_Cuda = lines_length(codeSnippetCuda)[0]
print("lines_length_mean Cuda is : ",test_lines_length_mean_Cuda)


test_lines_length_max_Py = lines_length(codeSnippetPython)[1]
print("lines_length_max Python is : ",test_lines_length_max_Py)

test_lines_length_max_java = lines_length(codeSnippetJava)[1]
print("lines_length_max Java is : ",test_lines_length_max_java)

test_lines_length_max_Cuda = lines_length(codeSnippetCuda)[1]
print("lines_length_max Cuda is : ",test_lines_length_max_Cuda)
"""

"""
test_comment_line_per_code_line_Py = comment_line_per_code_line(codeSnippetPython)
print("comment_line_per_code_line_Py is : ",test_comment_line_per_code_line_Py)
"""

test_comment_line_per_code_line_java = comment_line_per_code_line(codeSnippetJava)
print("comment_line_per_code_line Java is : ",test_comment_line_per_code_line_java)

"""
test_comment_line_per_code_line_cuda = comment_line_per_code_line(codeSnippetCuda)
print("comment_line_per_code_line_cuda is : ",test_comment_line_per_code_line_cuda)


test_blank_line_per_code_line_Py = blank_line_per_code_line(codeSnippetPython)
print("blank_line_per_code_line_Py is : ",test_blank_line_per_code_line_Py)

test_blank_line_per_code_line_java = blank_line_per_code_line(codeSnippetJava)
print("blank_line_per_code_line Java is : ",test_blank_line_per_code_line_java)

test_blank_line_per_code_line_cuda = blank_line_per_code_line(codeSnippetCuda)
print("comment_line_per_code_line_cuda is : ",test_blank_line_per_code_line_cuda)


test_indentation_Py = indentation_mean(codeSnippetPython)
print("indentation_Py is : ", test_indentation_Py)

test_indentation_Java = indentation_mean(codeSnippetJava)
print("indentation_Java is : ", test_indentation_Java)

test_indentation_Cuda = indentation_mean(codeSnippetCuda)
print("indentation_Cuda is : ", test_indentation_Cuda)


test_max_streak_opening_parentheses_py = max_streak_opening_parentheses(codeSnippetPython)
print("max_streak_opening_parentheses_py is : ",test_max_streak_opening_parentheses_py)

test_max_streak_opening_parentheses_java = max_streak_opening_parentheses(codeSnippetJava)
print("max_streak_opening_parentheses_java is : ",test_max_streak_opening_parentheses_java)

test_max_streak_opening_parentheses_cuda = max_streak_opening_parentheses(codeSnippetCuda)
print("max_streak_opening_parentheses_cuda is : ",test_max_streak_opening_parentheses_cuda)


test_max_streak_period = max_streak_period(snippet1)
print("max_streak_period is : ",test_max_streak_period)

with open('./resources/dataset/Dataset/Snippets/1.jsnp', "r") as fichier:
    codeTest = CodeSnippet(ProgrammingLanguage.JAVA,"exemple de code \n etc")

returnMetrics(codeTest)
"""