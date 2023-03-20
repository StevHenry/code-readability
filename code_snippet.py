from enum import Enum

class Langage(Enum):
    PYTHON = 1
    JAVA = 2
    C = 3


class Code_snippet:
    def __init__(self, langage: Langage, contenu: str, comments:str):
        self.langage = 0
        self.contenu = {} # contenu du code en occultant les commentaires
        self.comments = {} #commentaires (concanténés) pour calcul métrique Thomas

