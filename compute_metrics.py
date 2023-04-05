import re
import numpy as np
from code_snippet import CodeSnippet, ProgrammingLanguage
from code_metric import CodeMetric, NOT_IMPLEMENTED_METRICS


def get_metric(metric: CodeMetric, snippet: CodeSnippet) -> int | float:
    """
    :param metric: Metric to compute (From the CodeMetric enum)
    :param snippet: Code snippet to compute
    :return: the computed queried metric for the provided code snippet
    """
    match metric:
        case CodeMetric.NUMBER_OF_LINES:
            return _metric_number_of_lines(snippet)
        case CodeMetric.NUMBER_OF_LOOPS:
            return _metric_number_of_loops(snippet)
        case CodeMetric.NESTED_LOOPS_AND_BRANCHES:
            raise NotImplementedError
        case CodeMetric.LINE_LENGTH_MEAN:
            return _metrics_lines_length(snippet)[0]
        case CodeMetric.LINE_LENGTH_MAX:
            return _metrics_lines_length(snippet)[1]
        case CodeMetric.COMMENTS_PER_CODE_LINE:
            return _metric_comment_line_per_code_line(snippet)
        case CodeMetric.LINES_BREAK_AFTER_STATEMENTS:
            raise NotImplementedError
        case CodeMetric.PROPORTION_OF_BLANK_LINES:
            return _metric_blank_line_per_code_line(snippet)
        case CodeMetric.PROPORTION_OF_GOOD_INDENTATION:
            return _metric_indentation_mean(snippet)
        case CodeMetric.IDENTIFIERS_LENGTH:
            raise NotImplementedError
        case CodeMetric.MAX_STREAK_OF_OPENING_PARENTHESIS:
            return _metric_max_streak_opening_parentheses(snippet)
        case CodeMetric.MAX_STREAK_OF_FOLLOWING_PERIODS:
            return _metric_max_streak_period(snippet)
        case CodeMetric.SPACES_AROUND_OPERATORS:
            raise NotImplementedError
        case _:
            raise NotImplementedError


def get_all_metrics(snippet: CodeSnippet) -> dict:
    """ Returns a dict<CodeMetric, value> for the provided code snippet """
    result = dict()
    implemented_metrics = [metric for metric in CodeMetric if metric not in NOT_IMPLEMENTED_METRICS]
    for metric in implemented_metrics:
        result[metric] = get_metric(metric, snippet)
    return result


def _metric_number_of_lines(code: CodeSnippet):
    """ Returns the value of CodeMetric.NUMBER_OF_LINES """
    return len(re.findall("\n", code.get_code(True, True)))


def _metric_number_of_loops(code: CodeSnippet):
    """ Returns the value of CodeMetric.NUMBER_OF_LOOPS """
    forwhile_re = re.compile(r'(?<!\S)(for|while)', re.MULTILINE)
    return len(forwhile_re.findall(code.get_code(False, False)))


def _metrics_lines_length(code: CodeSnippet) -> (float, float):
    """ Returns the value of CodeMetric.LINE_LENGTH_MEAN and CodeMetric.LINE_LENGTH_MAX """
    lines = code.get_code(True, True).split('\n')
    list_length = []
    for line in lines:
        # vérifie que la ligne n'est pas vide ou ne contient pas que des espaces car sinon cela fausse la moyenne
        if line.replace(" ", "") != '':
            list_length.append(len(line))
    return np.mean(list_length).astype(float), np.max(list_length).astype(float)


def _metric_comment_line_per_code_line(code: CodeSnippet):
    """ Returns the value of CodeMetric.COMMENTS_PER_CODE_LINE """
    comments_size = 0
    for com in code.code_comments:
        comments_size = comments_size + len(com.split('\n'))
    code_no_comments = code.get_code(True, False).split('\n')
    return comments_size / _metric_number_of_lines(code)


def _metric_blank_line_per_code_line(code: CodeSnippet):
    """ Returns the value of CodeMetric.PROPORTION_OF_BLANK_LINES """
    lines = code.get_code(True, True).split('\n')
    blank_line = []
    for line in lines:
        if line.replace(" ", "") == '':
            blank_line.append(line)
    return len(blank_line) / len(lines)


def _metric_indentation_mean(code: CodeSnippet):
    """ Returns the value of CodeMetric.PROPORTION_OF_GOOD_INDENTATION """
    if code.language == ProgrammingLanguage.PYTHON:
        return 2
    codelines = code.get_code(False, False)
    ctr = 0
    for car in (codelines):
        if car == '\t':
            ctr += 1
    return ctr / _metric_number_of_lines(code)


def _metric_max_streak_opening_parentheses(code: CodeSnippet):
    """ Returns the value of CodeMetric.MAX_STREAK_OF_OPENING_PARENTHESIS """
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


def _metric_max_streak_period(code):
    """ Returns the value of CodeMetric.MAX_STREAK_OF_FOLLOWING_PERIODS """
    period_regex = r'(((([^\. \n])+\(.*?\))|[^\. \n]+)(\.((([^\. \n])+\(.*?\))|[^\. \n]+))+)'
    max_streak = 0
    for chain in re.findall(period_regex, code.get_code(False, False)):
        max_streak = max(max_streak, len(chain[0].split('.')))
    return max_streak
