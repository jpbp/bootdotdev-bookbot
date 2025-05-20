#!/usr/bin/env python3

'''Build a Bookbot in Python.

A ideia é criar um aplicativo de linha de comando real em Python 
que analisa dados em arquivos de texto, ou melhor, em romances 
inteiros como "Frankenstein", "Moby Dick" ou "Orgulho e Preconceito". 
Você será guiado pela configuração de um ambiente de desenvolvimento 
profissional usando Python, Git e Github. Este é o primeiro projeto Python 
perfeito para iniciantes.

Execução:
    python3 main.py
    ou
    ./main.py

'''
__version__ = "0.0.1"
__autor__ = "João Paulo"
__licence__ = "Unlicense"

from stats import get_count_of_words_text
from stats import get_book_text
       
def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_count_of_words_text(book)
    print(f"{num_words} words found in the document")
    
main()