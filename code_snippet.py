from enum import Enum
import re

string_re = re.compile(r"((?<![\\])['\"])((?:.(?!(?<![\\])\1))*.?)\1", re.MULTILINE)
string_replacement_basis = "09444a69322fe262§"
replaced_strings_re = re.compile(rf"(?<={string_replacement_basis})\d+", re.MULTILINE)
comments_re = re.compile(r'(\n*#.*)|(\n*//.*)|(\n*"""(.|\n)*""")|(/\*.*\*\/)', re.MULTILINE)
comments_format_re = re.compile(r'((\\n)*#)|((\\n)*//)|((\\n)*""")|((\\n)*/\*)|((\\n)*\*/)', re.MULTILINE)


class ProgrammingLanguage(Enum):
    PYTHON = 1
    JAVA = 2
    C = 3


class CodeSnippet:
    def __init__(self, language: ProgrammingLanguage, original_text: str):
        self.language = language

        self.code_strings = []
        self.code_comments = []

        self.code_original = original_text
        self.code_original_strings_no_comments = ''
        self.code_replaced_strings_no_comments = ''
        self.code_replaced_strings_with_comments = ''

        self.__compute_strings()

    def get_code(self, original_strings: bool, with_coms: bool) -> str:
        if original_strings and with_coms:
            return self.code_original
        elif original_strings:
            return self.code_original_strings_no_comments
        elif with_coms:
            return self.code_replaced_strings_with_comments
        else:
            return self.code_replaced_strings_no_comments

    def __compute_strings(self) -> None:
        replaced_string = self.code_original

        code_strings = string_re.findall(self.code_original)
        self.code_strings = []
        for string in code_strings:
            full_str = string[0] + string[1] + string[0]
            if full_str == '"""':
                continue
            replaced_string = replaced_string.replace(full_str, string_replacement_basis + str(len(self.code_strings)), 1)
            self.code_strings.append(full_str)

        comments = comments_re.findall(replaced_string)
        clean_comments = []
        for i, comment in enumerate(comments):
            comments[i] = ''.join(comments[i])
            clean_com = comments[i]
            for element in comments_format_re.findall(comments[i]):
                for subelement in element:
                    clean_com = clean_com.replace(subelement, '')

            clean_comments.append(clean_com)

        print(comments)
        print(clean_comments)

        # Saving computed values into object
        self.code_comments = comments
        self.clean_code_comments = clean_comments
        self.code_replaced_strings_with_comments = replaced_string
        self.code_replaced_strings_no_comments = replaced_string
        self.code_original_strings_no_comments = self.code_original


    @staticmethod
    def retrieve_strings(strings: list, code: str) -> str:
        to_replace = strings_id_re.findall(code)
        for index in to_replace:
            code = code.replace(string_replacement_basis + str(index), strings[int(index)])
        return code
