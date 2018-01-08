def is_anagram(word1, word2):
    word1_letter_count = {}
    word2_letter_count = {}
    anagram = True

    for letter in word1:
        word1_letter_count[letter] = word1_letter_count.get(letter,0) + 1

    for letter in word2:
            word2_letter_count[letter] = word2_letter_count.get(letter, 0) + 1

    for key in word1_letter_count.keys():
        if word1_letter_count[key] != word2_letter_count[key]:
            anagram = False

    return anagram


if __name__ == '__main__':
    print(is_anagram("eatt","ttea"))
    print(is_anagram("eatt","eati"))