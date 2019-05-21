# Approximate string matching using Levenshtein and Damerau Levenshtein distance with fuzzy search tries

A Design and Analysis of Algorithms course assignment

Levenshtein distance measures the minimum number of edits to get from one word to another (insertion, deletion and substitution of characters)

Damerau Levenshtein also includes transposition of characters to measure the distance.

The usage of search tries lets us build the edit matrix in a faster way by traversing through the list of the words from the corpus in the best possible order (i.e., by collapsing all the words with a common prefix into one path).

For a more detailed explanation on search tries - [This post by Steve Hanov](http://stevehanov.ca/blog/?id=114) (which also served as a reference to us)

The time function used here takes into account the time to taken to start the python interpreter as well(so for smaller datasets, time the functions individually).

The UI is a very rudimentary terminal UI. type in ```start``` after the ```(cmd)``` prompt and type in words and press ```tab``` to see a list of suggested words. The word is autocorrected/completed only if there is only one possible word that satisifies the edit distance constraint. run ```ui_lev.py``` for the ui for levenshtein distance and ```ui_dl.py``` for damerau-levenshtein distance.
