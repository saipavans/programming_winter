word_file_name = "./words.txt"

word_file = open(word_file_name)
for line in word_file:
    if len(line.strip()) > 20:
        print(line)
