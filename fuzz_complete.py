'''
import numpy as np
def lev_ratio_and_dist(s, t, lev_ratio = False):
    r = len(s)+1
    c = len(t)+1
    dist_mat = np.zeros((r,c),dtype = int)
    for i in range(1, r):
        for k in range(1,c):
            dist_mat[i][0] = i
            dist_mat[0][k] = k
            
    for row in range(1,r):
        for col in range(1,c):
            if s[row-1] == t[col-1]:
               cost = 0
            else:
                if(lev_ratio == True):
                    cost = 2
                else:
                    cost = 1
            dist_mat[row][col] = min(dist_mat[row-1][col]+1,
                                     dist_mat[row][col-1] +1,
                                     dist_mat[row-1][col-1]+cost)
    if lev_ratio == True:
        ratio = ((r+c-2) - dist_mat[row][col])/(r+c-2)
    else:
        ratio = -1

    return (dist_mat[row][col], ratio)
'''
import sys
target = sys.argv[1]
max_cost = int(sys.argv[2])



NodeCount = 0
class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

        global NodeCount
        NodeCount += 1

    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()

            node = node.children[letter]
        node.word = word

trie = TrieNode()

# relpace with file reading type of input if necessary
word = "Thejas"
trie.insert(word)
trie.insert("The")
trie.insert("Bhat")
trie.insert("Thej")
trie.insert("Bhatta")

def search(word, maxcost,  ratio_calc = False):
    currentrow = range(len(word)+1)

    results = []

    for letter in trie.children:
        search_again(trie.children[letter], letter, word, currentrow, results, maxcost, ratio_calc)

    return results

def search_again(node, letter, word, prevRow, results, maxcost, ratio_calc):

    columns = len(word) + 1
    currentRow = [ prevRow[0] + 1 ]

    for column in range(1,columns):

        insertcost = currentRow[column - 1] + 1
        deletecost = prevRow[column] + 1

        if word[column - 1] != letter:
            if ratio_calc:
                #print("following python lev package style")
                replacecost = prevRow[column - 1] + 2
            else:                
                replacecost = prevRow[column - 1] + 1
        else:
            replacecost = prevRow[column - 1]

        currentRow.append(min( insertcost, deletecost, replacecost))

    if(currentRow[-1] <= maxcost and node.word != None):
        results.append((node.word, currentRow[-1]))

    if min(currentRow) <= maxcost:
        for letter in node.children:
            search_again(node.children[letter], letter, word, currentRow, results, maxcost, ratio_calc)

            
results = search(target, max_cost, True)

for res in results:
    print(res)

print(NodeCount,"thats it i guess")    


    
