file_path = "./words.txt"


def check_file(file_path, find_word):
    fin = open(file_path)
    word_table = {}
    for line in fin:
        word = line.strip()
        if word in word_table.keys():
            word_table[word] += 1
        else:
            word_table[word] = 1
    return (find_word in word_table.keys())


word1 = "aah"
word2 = "asfdafknasgnasdfkansfgkl"
print(check_file(file_path, word1))
print(check_file(file_path, word2))
