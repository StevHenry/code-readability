import sys

from code_snippet import CodeSnippet

if __name__ == '__main__':
    """ program parameters: files to compute """
    arguments = sys.argv
    if len(arguments) != 0:
        files = arguments
    else:
        files = ['./resources/DatasetDorn/dataset/snippets/python/0.jsnp']



def reg_number_of_comments(code: CodeSnippet):
    pass


def comments_readability(code):
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
