

readFile = open("./data/wiki-100k.txt", "r")
symbols = [',', '.', ';', '\'', '"']
newFile = open("./data/cleaned.txt", "w")
for line in readFile.readlines():
    if line.startswith("#"):
        continue
    for symbol in symbols:
        if symbol in line:
            continue
    newFile.write(line)
