word_file_name = "./words.txt"

word_file = open(word_file_name)


def has_no_e(word):
    return word.find("e") == -1

total_words = 0
words_without_e = 0
for line in word_file:
    total_words += 1
    if has_no_e(line.strip()):
        words_without_e += 1
        print(line)

print("Percentage of words without e: ",(words_without_e/total_words * 100))

