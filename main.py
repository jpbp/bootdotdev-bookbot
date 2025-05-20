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

from stats import (
    get_count_of_words_text,
    get_book_text,
    get_number_of_times_each_character,
    get_return_order_dic)

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    name_book = f"./{sys.argv[1]}"
    book = get_book_text(name_book)
    num_words = get_count_of_words_text(book)
    dic_count_words = get_number_of_times_each_character(book)
    
    print("=" *12,"BOOKBOT","=" *12)
    print("Analyzing book found at books/frankenstein.txt...")
    print("-" *12,"Word Count","-" *12)
    print(f"Found {num_words} total words")
    print("-" *10,"Character Count","-" *10)
    list_character = get_return_order_dic(dic_count_words)
    for dic_character in list_character:
        if (dic_character["char"].isalpha()):
            char = dic_character["char"]
            num = dic_character["num"]
            print(f"{char}: {num}")
    print("=" *10,"END ","=" *10)
main()