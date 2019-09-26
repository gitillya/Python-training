from os import strerror, path


def lineDone(line):
    temp_list = list(line.replace(' ', '').replace('\t', '').replace('\n', '').lower())
    for char in temp_list:
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1


def printResult(list):
    for element in list:
        print(element, "->", list[element])


def printResultToFile(list):
    for element in list:
        print(element, "->", list[element])


character_frequency = {}
file_name = input("Please enter file's name: ")
try:
    cnt = 0
    s = open(file_name, "rt")
    line = s.readline()
    lineDone(line)
    while line:
        line = s.readline()
        lineDone(line)
        cnt += 1
    s.close()
    # print("\n\nCharacters in file:", cnt)
    character_frequency = dict(sorted(character_frequency.items(), reverse = True, key=lambda i: i[1]))

    # firts_name = 'first.hist'
    firts_name = path.splitext(file_name)[0] + '.hist'
    fo = open(firts_name, 'wt')
    for element in character_frequency:
        temp = "" + str(element) + " -> " + str(character_frequency[element]) + "\n"
        fo.write(temp)
    fo.close()

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

printResult(character_frequency)
