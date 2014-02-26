VGNG
====

Video Game Name Generator. Translated to python from the javascript used on
videogamena.me

Works with at least python 2.7 and 3.3. Not tested with anything else.


How to use
==========

Uses 'video_game_names.txt' as the default list to generate names from.

./vgng
    - Will output 1 random name.

./vgng N
    - Will output N number of names.

./vgng -l <FILENAME> OR ./vgng --list <FILENAME>
    - Will use FILENAME as the wordlist.

./vgng -l <FILENAME> N
    - Uses FILENAME as wordlist, outputs N names.


Word List Syntax
================

Uses the same format as used on videogamena.me

The file is separated into three groups, separated by dashes.  Dupe protection is indicated with a '^' and are separated with '|'s


LICENSE
=======
Python code is licensed under the MIT license. See LICENSE

video_game_names.txt is shamelessly copied from videogamena.me/video_game_names.txt
See http://videogamena.me/about.html for details.
