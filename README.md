VGNG
====

Video Game Name Generator. Translated to python from the javascript used on
videogamena.me

Works with at least python 2.7 and 3.3. Not tested with anything else.


Usage
=====

Uses 'video_game_names.txt' as the default list to generate names from.

    $ ./vgng.py -h
    usage: vgng.py [-h] [-l LIST] [count]
    
    positional arguments:
      count                 Number of names to create
      
    optional arguments:
      -h, --help            show this help message and exit
      -l LIST, --list LIST  Word list to use for generating names.
    
    $ ./vgng.py
    <name>

    $ ./vgng 3
    <name>
    <name>
    <name>


Word List Syntax
================

Uses the same format as used on videogamena.me

The file is separated into three groups, separated by dashes.  Dupe protection is indicated with a '^' and are separated with '|'s


LICENSE
=======
Python code is licensed under the MIT license. See LICENSE

video_game_names.txt is shamelessly copied from videogamena.me/video_game_names.txt
See http://videogamena.me/about.html for details.
