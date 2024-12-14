import os
import unicodedata

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def normalizar_categoria(categoria):
    return ''.join((c for c in unicodedata.normalize('NFD', categoria) if unicodedata.category(c) != 'Mn')).lower().strip()


def normalizar_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')