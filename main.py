#!/usr/bin/env python
# dobra praktyka

'''Fetch and print words
Usage:
    python main.py <filepath>
    ./main.py <filepath>
    from main import main
    main(<filepath>)
'''

import sys


def fetch_words(filepath):
    '''
    fetch words from given filepath
    :param filepath: relative or absolute filepath
    :type filepath: str
    :return: word list from given filepath
    :rtype list[str]
    '''
    with open(filepath, 'r') as file:
        return [word for line in file for word in line.split()]


def print_items(items):
    '''
    print item from given iterable
    :param items: any iterable collection of data
    type items: iterable
    :return: None
    :rtype: None
    '''
    for item in items:
        print(item)


def main(filepath):
    '''
    Fetch and shows word from given filepath
    :param filepath: relative or absolute filepath
    :type filepath: str
    :return: None
    :rtype None
    '''
    words = fetch_words(filepath)
    print_items(words)


# read_file('text.txt')
# print(__name__)  # zeby odróżnić __

# sprawdza, czy w globalnym contexcie, nie odpala przy imporcie tylko po kropce np., moge odpalać na 2 sposoby
if __name__ == '__main__':
    main(sys.argv[1])  # Zero-index is module name

    # read_file(sys.argv[1])  # przkeazywanie parametru po nazwie pliku
