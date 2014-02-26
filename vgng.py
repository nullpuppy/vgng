#!/usr/bin/env python
#
# Translation of videogamena.me javascript to python
#
# http://videogamena.me/vgng.js
# http://videogamena.me/video_game_names.txt
#
# (C) 2014 Dustin Knie <dustin@nulldomain.com>

import argparse
import os
import random
from math import floor, trunc


_word_list_file = 'video_game_names.txt'
_word_list = []


def _build_list(word_list=_word_list_file):
    try:
        f = open(word_list, 'r')

        words = []
        for line in f:
            line = line.strip('\n')
            if line == "----":
                _word_list.append(words)
                words = []
            else:
                words.append(line)
        _word_list.append(words)

    except IOError as e:
        print("Error opening {}: {}".format(word_list, e))
        exit(1)


def _get_word(word_list, words=[], bad_match_list=[], allow_similar_matches=False):
    bad_word = True
    while bad_word:
        word = word_list[trunc(floor(random.random() * len(word_list)))]
        if '^' in word:
            if not allow_similar_matches:
                bad_match_list += word.split('^')[1].split('|')
            word = word.split('^')[0]

        if word in words or word in bad_match_list:
            continue

        bad_word = False

    words.append(word)
    return (words, bad_match_list)


def generate_game_name(allow_similar_matches=False):
    words = []
    bad_match_list = []
    for word_list in _word_list:
        (words, bad_match_list) = _get_word(word_list,
            words=words,
            bad_match_list=bad_match_list,
            allow_similar_matches=allow_similar_matches)

    return ' '.join(words)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('count', type=int, nargs='?', help='Number of names to create')
    parser.add_argument('-l', '--list', action='store', help='Word list to use for generating names.')

    args = parser.parse_args()

    _build_list(word_list=args.list if args.list else _word_list_file)
    for i in range(args.count if args.count else 1):
        print(generate_game_name())

