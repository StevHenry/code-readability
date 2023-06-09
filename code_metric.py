from enum import Enum


class CodeMetric(Enum):
    """
    Defines all the metrics potentially usable
    """
    NUMBER_OF_LINES = 0
    NB = 0
    NUMBER_OF_LOOPS = 1
    LC = 1
    NESTED_LOOPS_AND_BRANCHES = 2
    NL = 2
    LINE_LENGTH_MEAN = 3
    LL = 3
    COMMENTS_PER_CODE_LINE = 4
    CL = 4
    LINES_BREAK_AFTER_STATEMENTS = 5
    LBS = 5
    PROPORTION_OF_BLANK_LINES = 6
    BL = 6
    PROPORTION_OF_GOOD_INDENTATION = 7
    ID = 7
    IDENTIFIERS_LENGTH = 8
    IL = 8
    MAX_STREAK_OF_OPENING_PARENTHESIS = 9
    PA = 9
    MAX_STREAK_OF_FOLLOWING_PERIODS = 10
    FP = 10
    SPACES_AROUND_OPERATORS = 11
    SP = 11
    LINE_LENGTH_MAX = 12
    LM = 12


NOT_IMPLEMENTED_METRICS = (CodeMetric.NESTED_LOOPS_AND_BRANCHES, CodeMetric.NL,
                           CodeMetric.LINES_BREAK_AFTER_STATEMENTS, CodeMetric.LBS,
                           CodeMetric.IDENTIFIERS_LENGTH, CodeMetric.IL,
                           CodeMetric.SPACES_AROUND_OPERATORS, CodeMetric.SP)

IMPLEMENTED_METRICS = [metric for metric in CodeMetric if metric not in NOT_IMPLEMENTED_METRICS]


class ReadibilityClass(Enum):
    NOT_VERY_READABLE = 0
    QUITE_READABLE = 1
    FULLY_READABLE = 2