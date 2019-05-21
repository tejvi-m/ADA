import cmd
from lev_tries import *

data = open("./data/google-10000-english.txt", "r")
for line in data.readlines():
    word = line.strip()
    trie.insert(word)


class MyCmd(cmd.Cmd):
    def do_start(self, line):
        pass

    def complete_start(self, text, line, start_index, end_index):

        if text:
            results = search(text, 2, True)
            return [

                result[0][:] for result in results
            ]
            # text = text.replace(" ", "")
            # return text

        else:
            return "type something"


if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.cmdloop()
