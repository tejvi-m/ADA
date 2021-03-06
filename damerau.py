import sys

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

def search(word, maxcost,  ratio_calc = False):
    currentrow = range(len(word)+1)
    results = []

    for letter in trie.children:
        search_again(trie.children[letter], letter, None, word, currentrow, None, results, maxcost, ratio_calc)

    return results

def search_again(node, letter, prev_letter, word, prevRow, pre_previous_row, results, maxcost, ratio_calc):

    columns = len(word) + 1
    currentRow = [prevRow[0] + 1]

    for column in range(1,columns):

        insertcost = currentRow[column - 1] + 1
        deletecost = prevRow[column] + 1

        if word[column - 1] != letter:
            if ratio_calc:
                replacecost = prevRow[column - 1] + 2
            else:
                replacecost = prevRow[column - 1] + 1
        else:
            replacecost = prevRow[column - 1]

        currentRow.append(min( insertcost, deletecost, replacecost))
        if prev_letter:
        	#print(pre_previous_row,"----",currentRow[column], pre_previous_row[column - 2])
        if prev_letter and column -1 > 0 and letter == word[column - 2] and prev_letter == word[column - 1] and word[column - 1] != letter:
        	currentRow[column] = min(currentRow[column], pre_previous_row[column - 2] + 1)

    if(currentRow[-1] <= maxcost and node.word != None):
        results.append((node.word, currentRow[-1]))

    if min(currentRow) <= maxcost:
    	prev_letter = letter
        for letter in node.children:
            search_again(node.children[letter], letter, prev_letter, word, currentRow, prevRow, results, maxcost, ratio_calc)
        #node = node.children[letter]
        #prevRow = currentRow

if __name__ == '__main__':
    target = sys.argv[1]
    max_cost = int(sys.argv[2])

    data = open("./data/my.txt", "r")
    for line in data.readlines():
        words = line.split(" ")
        for i in range(len(words)):
            trie.insert(words[i])

    results = search(target, max_cost, True)
    for res in results:
        print(res)

    print(NodeCount,"thats it i guess")
