words_file_path = "./words.txt"


def is_abcderian(word):
    word_len = len(word)
    result = True
    for iterator in range(len(word) - 1):
        if word[iterator] <= word[iterator + 1]:
            iterator += 1
            continue
        else:
            result = False
            break
    return result


words_abcderian = 0

fin = open(words_file_path)

for line in fin:
    word = line.strip()
    if is_abcderian(word):
        print(word)
        words_abcderian += 1

print("Number of abcderian words are: ", words_abcderian)



