from lev_ratio import *

data = open("./data/exampleText0.txt", "r")




for line in data.readlines():
    words = line.split(" ")
    for i in range(len(words)):
        x = lev_ratio_and_dist(words[i], "which", True)
        if x[0] <= 3:
            print(words[i])
