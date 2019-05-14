from lev_ratio import *
import sys


data = open("./data/google-10000-english.txt", "r")
target = sys.argv[1]
dist = int(sys.argv[2])
suppress = int(sys.argv[3])

possibleWords = []
for line in data.readlines():
    words = line.split(" ")
    for i in range(len(words)):
        x = lev_ratio_and_dist(words[i], "which", False)
        if x[0] <= 3:
            possibleWords.append(x[0])

        if not suppress:
            print(possibleWords)
