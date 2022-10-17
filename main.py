#!/usr/bin/env python
# dobra praktyka

import sys


def fetch_words(filepath):
    with open(filepath, 'r') as file:
        return [word for line in file for word in line.split()]


def print_items(items):
    for item in items:
        print(item)


def main(filepath):
    words = fetch_words(filepath)
    print_items(words)


# read_file('text.txt')
# print(__name__)  # zeby odróżnić __

if __name__ == '__main__':  # sprawdza, czy w globalnym contexcie, nie odpala przy imporcie tylko po kropce np., moge odpalać na 2 sposoby
    main(sys.argv[1])
    # read_file(sys.argv[1])  # przkeazywanie parametru po nazwie pliku
