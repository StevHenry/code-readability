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
    code.FP = max_streak_period(code)
    return code.LN, code.LC, code.AvgLL, code.MaxLL, code.CL, code.BL, code.ID, code.PA, code.FP


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


def max_streak_period(code):
    period_regex = r'(((([^\. \n])+\(.*?\))|[^\. \n]+)(\.((([^\. \n])+\(.*?\))|[^\. \n]+))+)'
    max_streak = 0
    for chain in re.findall(period_regex, code.get_code(False, False)):
        print(chain[0].split('.'))
        max_streak = max(max_streak, len(chain[0].split('.')))
    return max_streak
