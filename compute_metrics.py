import sys
import re
import numpy as np
from code_snippet import CodeSnippet, ProgrammingLanguage
import keyword


if __name__ == '__main__':
    """ program parameters: files to compute """
    arguments = sys.argv
    if len(arguments) != 0:
        files = arguments
    else:
        files = ['./resources/DatasetDorn/dataset/snippets/python/0.jsnp']


def returnMetrics(code: CodeSnippet) -> tuple:
    code.LN = reg_number_of_lines(code)
    code.LC = reg_number_of_loops(code)
    code.LL = lines_length_mean(code)
    code.CL = comment_line_per_code_line(code)
    code.BL = blank_line_per_code_line(code)
    code.ID = proportion_good_indentations(code)
    code.IL = mean_identifier_length(code)
    code.PA = max_streak_opening_parentheses(code)
    code.FP = max_streak_period(code)
    return code.LN, code.LC, code.LL, code.CL, code.BL, code.ID, code.IL, code.PA, code.FP


def comments_readability(code: CodeSnippet):
    """
    Cette fonction prend en entrée une chaîne de caractères représentant du code Python
    et renvoie une chaîne de caractères contenant tous les commentaires présents dans le code, en les joignant avec des points pour délimiter des phrases.
    """
    lines = code.split('\n')  # Séparer le code en lignes
    comments = []  # Initialiser une liste pour stocker les commentaires
    for i in range(len(lines)):
        line = lines[i].rstrip()  # Supprimer les espaces en fin de ligne
        if '#' in line:  # Si le caractère '#' est présent sur la ligne
            start_index = line.index('#')  # Trouver l'index du premier caractère '#'
            if not line[:start_index].strip().startswith('"'):  # Si la ligne ne commence pas par une chaîne de caractères, c'est un commentaire en ligne
                comment = line[start_index+1:].strip()  # Récupérer le commentaire à partir du premier caractère '#'
                comments.append(comment)  # Ajouter le commentaire à la liste
        elif line.startswith('"""'):  # Si la ligne commence par '"""', c'est le début d'un commentaire en bloc
            j = i + 1
            while j < len(lines) and not lines[j].strip().endswith('"""'):  # Trouver la fin du commentaire en bloc
                j += 1
            if j < len(lines):  # Si on a trouvé la fin du commentaire en bloc
                comment = ' '.join([x.strip() for x in lines[i:j+1] if x.strip().startswith('#') or x.strip() != ''])  # Joindre toutes les lignes de commentaire en bloc avec un espace entre elles
                comment = comment.replace('"""', '').strip()  # Supprimer les triple quotes du début et de la fin du commentaire
                comments.append(comment)  # Ajouter le commentaire à la liste
    return '.'.join(comments)  # Joindre les commentaires en une seule chaîne de caractères, en les délimitant avec des points pour délimiter des phrases


def reg_number_of_lines(code : CodeSnippet):
    x = re.findall("\n", code.get_code(True, True))
    return len(x)


def reg_number_of_loops(code : CodeSnippet) :
    x = re.findall("for" , code.get_code(False, False))
    y = re.findall("while" , code.get_code(False, False))
    output = x+y
    return len(output)

def lines_length_mean(code : CodeSnippet):
    lines = code.get_code(True, True).split('\n')
    list_length = []
    for line in lines:
        if line.replace(" ","") != '': # verifie que la ligne n'est pas vide ou ne contient pas que des espaces car sinon cela fausse la moyenne
            list_length.append(len(line))
    return np.mean(list_length)

def comment_line_per_code_line(code : CodeSnippet):
    comments = code.code_comments
    code_no_comments = code.get_code(True, False).split('\n')
    return len(comments)/(len(comments)+len(code_no_comments))


# A voir si on laisse with_coms=True car ça augmente la valeur de len(lines) et donc diminue un peu la proportion de blank line
# Mais si on met with_coms=False il faut que Steven supprime les lignes vides qui sont laissées lorsqu'il supprime les commentaires
def blank_line_per_code_line(code : CodeSnippet):
    lines = code.get_code(True,True).split('\n')
    blank_line = []
    for line in lines:
        if line.replace(" ", "") == '':
            blank_line.append(line)
    return len(blank_line)/len(lines)

"""
def proportion_good_indentations(code : CodeSnippet):

    if code.langage == ProgrammingLanguage.PYTHON:
        return 1
    if code.langage == ProgrammingLanguage.JAVA:
        # Compte le nombre de lignes avec une indentation correcte
        nb_lignes_correctes = 0
        for ligne in code.splitlines():
            indentation = len(ligne) - len(ligne.lstrip())
            if indentation % 4 == 0:
                nb_lignes_correctes += 1
        # Calcule la proportion de bonnes indentations
        proportion = nb_lignes_correctes / len(code.splitlines())

        return proportion
    if code.langage == ProgrammingLanguage.C:
        # Compte le nombre de lignes avec une indentation correcte
        nb_lignes_correctes = 0
        for ligne in code.splitlines():
            indentation = len(ligne) - len(ligne.lstrip())
            for i in (2,4,8):
                if indentation % i == 0:
                    nb_lignes_correctes += 1
                    break


        # Calcule la proportion de bonnes indentations
        proportion = nb_lignes_correctes / len(code.splitlines())

        return proportion
"""

def proportion_good_indentations(code : CodeSnippet):

    if code.language == ProgrammingLanguage.PYTHON:
        return 1 #indentation forcément parfaite en Python

    codelines = code.get_code(False, False)
    bracesCounter = 0
    indentCounter = 0
    wellIndentedLines = 0
    linesCounter = 0
    for i, car in enumerate(codelines.rstrip(codelines[-3:-1])):
        match car:
            case '{':
                bracesCounter += 1
            case '}':
                bracesCounter -= 1
            case '\n':
                while(codelines[i+1:i+2] == '\t'):
                    indentCounter += 1
                    i += 2
                if indentCounter == bracesCounter:
                    wellIndentedLines += 1
                linesCounter += 1
    return wellIndentedLines/linesCounter

def mean_identifier_length(code):
    # find all identifiers
    identifiers = re.findall(r'\b\w+\b', code.get_code(False, False).split('\n'))
    # Exclude reserved word in identifiers (for, while, print, etc)
    identifiers = [id for id in identifiers if id not in keyword.kwlist]
    avg_length = sum(len(id) for id in identifiers) / len(identifiers)
    print("La taille moyenne des identificateurs est de :", avg_length, "caractères.")
    return avg_length

def max_streak_opening_parentheses(code : CodeSnippet):
    count = 0
    max_count = 0
    for caractere in code.get_code(False, False):
        if caractere == "(":
            count += 1
        elif caractere == ")":
            if count > max_count:
                max_count = count
            count = 0
            continue
    return max_count


def max_streak_period(code):
    period_regex = r"(\w+(\(.*\))?)([\.]{1}\1?)+"
    list_mot = re.findall(period_regex, code)
    print(list_mot)


file = open("./resources/DatasetDorn/dataset/snippets/python/5.jsnp", 'r', encoding="utf-8")
snippet1 = file.read()


test_value_comments_readability = comments_readability(snippet1)
#print("value_comments_readability is : ", test_value_comments_readability)
"""
test_lines_length_mean = lines_length_mean(snippet1)
print("lines_length_mean is : ",test_lines_length_mean)

test_number_of_lines = reg_number_of_lines(snippet1)
print("number_of_lines is : ",test_number_of_lines)

test_number_of_loops = reg_number_of_loops(snippet1)
print("number_of_loops is : ",test_number_of_loops)

test_number_of_loops = reg_number_of_loops(snippet1)
print("number_of_loops is : ",test_number_of_loops)

test_comment_line_per_code_line = comment_line_per_code_line(snippet1)
print("comment_line_per_code_line is : ",test_comment_line_per_code_line)

test_comment_line_per_code_line = comment_line_per_code_line(snippet1)
print("comment_line_per_code_line is : ",test_comment_line_per_code_line)

test_max_streak_opening_parentheses = max_streak_opening_parentheses(snippet1)
print("max_streak_opening_parentheses is : ",test_max_streak_opening_parentheses)
"""

test_max_streak_period = max_streak_period(snippet1)
print("max_streak_period is : ",test_max_streak_period)

with open('./resources/dataset/Dataset/Snippets/1.jsnp', "r") as fichier:
    codeTest = CodeSnippet(ProgrammingLanguage.JAVA,"exemple de code \n etc")

returnMetrics(codeTest)
