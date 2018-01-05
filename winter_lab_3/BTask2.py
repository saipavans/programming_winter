def change_word(word):
    if len(word) > 3:
        word = word + "ly" if word[-3:] == "ing" else word + "ing"
    return word

print(change_word("studying"))
print(change_word("python"))
print(change_word("now"))