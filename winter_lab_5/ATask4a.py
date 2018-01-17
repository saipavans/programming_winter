import string

word_file = "../resources/words.txt"
book_file = "../resources/book1.txt"

word_list = []
fin1 = open(word_file)
for line in fin1:
    word_list.append(line.strip())

fin2 = open(book_file)
book_words = []
for line in fin2:
    mod_line = line.strip().lower().translate(str.maketrans('', '', string.punctuation))
    book_words.extend(mod_line.split())

book_word_unique = set(book_words)
for word in book_word_unique:
    if word not in word_list:
        print(word)
