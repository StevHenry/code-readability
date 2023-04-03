from enum import Enum
import re

string_re = re.compile(r"((?<![\\])['\"])((?:.(?!(?<![\\])\1))*.?)\1", re.MULTILINE)
string_replacement_basis = "09444a69322fe262§"
strings_id_re = re.compile(rf"(?<={ string_replacement_basis })\d+", re.MULTILINE)
comments_re = re.compile(r"(#.*$)|(//.*$)|(\"\"\".*\"\"\")|(\/\*.*\*\/)")


class ProgrammingLanguage(Enum):
    PYTHON = 1
    JAVA = 2
    C = 3


class CodeSnippet:
    def __init__(self, language: ProgrammingLanguage, original_text: str):
        self.langage = language
        # contenu total du code
        self.original_text = original_text
        # contenu du code en occultant les commentaires du code
        self.code_no_comments = ''
        # commentaire du code
        self.comments = ''

        self.code_strings = []
        self.code_strings_replaced = ''
        self.compute_replaced_string()

        self.code_no_strings_comments = ''

    def get_code(self, with_strings: bool, with_coms: bool) -> str:
        if with_strings and with_coms:
            return self.original_text
        elif with_strings:
            return self.code_no_comments
        elif with_coms:
            return self.code_no_string_with_com
        else:
            return self.code_no_string_no_com

    def compute_replaced_string(self) -> None:
        code_strings = string_re.findall(self.original_text)
        replaced_string = self.original_text
        i = 0
        # Replace the string number i by "string_replacement_basis + i"
        for string in code_strings:
            replaced_string = replaced_string.replace(string[1], string_replacement_basis + str(i), 1)
            i += 1
        # Minimize the code_strings list (removing unused values)
        for i in range(len(code_strings)):
            code_strings[i] = code_strings[i][1]
        self.code_strings = code_strings
        self.code_strings_replaced = replaced_string

    def remove_comments(self, code: str):
        code_comments = comments_re.findall(code)
        print(code_comments)
        without_coms = comments_re.sub("", code)
        comments = ''

        for comment in code_comments:
            comments += comment[0] + '\n'


    @staticmethod
    def retrieve_strings(strings: list, code: str) -> str:
        to_replace = strings_id_re.findall(code)
        for index in to_replace:
            code = code.replace(string_replacement_basis + str(index), strings[int(index)])
        return code
