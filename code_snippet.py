from enum import Enum
import re

STRING_RE = re.compile(r"((?<![\\])['\"])((?:.(?!(?<![\\])\1))*.?)\1", re.MULTILINE)
STRING_REPLACEMENT_BASIS = "09444a69322fe262§"
REPLACED_STRINGS_RE = re.compile(rf"(?<={STRING_REPLACEMENT_BASIS})\d+", re.MULTILINE)
COMMENTS_RE = re.compile(r'(#.*)|(//.*)|("""(.|\n)*""")|(/\*(.|\n(?!$))*\*/)', re.MULTILINE)
COMMENTS_FORMAT_RE = re.compile(r'#|(//)|(""")|(/\*\*?)|(\*/)', re.MULTILINE)
START_JUMP_LINES_RE = re.compile(r'^(\\n|\s)*', re.MULTILINE)
END_JUMP_LINES_RE = re.compile(r'(\\n|\s)*$', re.MULTILINE)


class ProgrammingLanguage(Enum):
    """
    Constants defining the programming language used in the code snippet
    """
    PYTHON = 1
    JAVA = 2
    C = 3


class CodeSnippet:
    """
    Object model for a code snippet, used to compute the metrics
    """
    def __init__(self, language: ProgrammingLanguage, original_text: str):
        """
        :param language: Programming language of the snippet (as an element of the ProgrammingLanguage enum)
        :param original_text: snippet saved as a string with line break characters
        """
        self.language = language

        # Variable that saves all the strings of the snippet ("aaa" or 'aaa')
        self.code_strings = []
        # Variable that saves all the comments of the snippet (//aaa or #aaa or /*aaa*/ or /**aaa*/ or """aaa""")
        self.code_comments = []

        # Original code extracted from the dataset
        self.code_original = original_text
        # Code with original strings and removed comments (Also removes the line if the comment is alone on its line)
        self.code_original_strings_no_comments = ''
        # Code with string replaced as 09444a69322fe262§INDEX_HERE to avoid computing metrics in the strings
        self.code_replaced_strings_no_comments = ''
        # Code with string replaced as 09444a69322fe262§INDEX_HERE and no comments (only executable code)
        self.code_replaced_strings_with_comments = ''

        self.__compute_strings()

    def get_code(self, original_strings: bool, with_coms: bool) -> str:
        """
        :param original_strings: Whether the code should be with non modified strings or replaced strings
                                The strings can be retrieves through the retrieve_strings method after computing
        :param with_coms: Whether the code should contain the comments
        :return: The code as a string with the specified parameters
        """
        if original_strings and with_coms:
            return self.code_original
        elif original_strings:
            return self.code_original_strings_no_comments
        elif with_coms:
            return self.code_replaced_strings_with_comments
        else:
            return self.code_replaced_strings_no_comments

    def __compute_strings(self) -> None:
        """
        Called only once in the constructor to compute the different versions of code
        :return: Nothing, saves the computed versions of the code directly in the object
        """
        replaced_string = self.code_original

        # Replaces the strings with undetectable values for the metrics computing
        code_strings = STRING_RE.findall(self.code_original)
        self.code_strings = []
        for string in code_strings:
            full_str = string[0] + string[1] + string[0]
            # If the string is """: skip
            if full_str == '"""':
                continue
            replaced_string = replaced_string.replace(full_str, STRING_REPLACEMENT_BASIS + str(len(self.code_strings)), 1)
            self.code_strings.append(full_str)

        # Finds all the comments from the code without strings
        comments = COMMENTS_RE.findall(replaced_string)
        clean_comments = []
        for i, comment in enumerate(comments):
            comments[i] = ''.join(comments[i])
            if comments[i].startswith('\n'):
                comments[i].replace('\n', '', 1)
            clean_com = comments[i]
            for element in COMMENTS_FORMAT_RE.findall(comments[i]):
                for sub_element in element:
                    clean_com = clean_com.replace(sub_element, '').replace('\n*', '\n')
                    clean_com = START_JUMP_LINES_RE.sub("", clean_com)
                    clean_com = END_JUMP_LINES_RE.sub("", clean_com)
            clean_comments.append(clean_com)

        # Saving computed values into object
        self.code_comments = comments
        self.clean_code_comments = clean_comments
        self.code_replaced_strings_with_comments = replaced_string
        self.code_replaced_strings_no_comments = replaced_string
        self.code_original_strings_no_comments = self.code_original

        for comment in comments:
            self.code_replaced_strings_no_comments = self.code_replaced_strings_no_comments.replace(comment, "")
            self.code_original_strings_no_comments = self.code_original_strings_no_comments.replace(comment, "")

    def retrieve_strings(self, working_string: str) -> str:
        """
        Replaces the strings with their initial values on the provided string
        :param working_string: string with replaced strings that needs the strings back
        :return: the new string
        """
        to_replace = REPLACED_STRINGS_RE.findall(working_string)
        for index in to_replace:
            working_string = working_string.replace(STRING_REPLACEMENT_BASIS + index, self.code_strings[int(index)])
        return working_string
