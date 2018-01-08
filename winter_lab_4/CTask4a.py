
def group_anagrams(word_list):
    """
    :param word_list: list containing words
    :return:  dictionary with [(letter(sorted), occurence), ...] as key and list of words as values
    """
    anagram_dict = {}

    for word in word_list:
        letter_count = {}
        anagram_dict_key = ()

        for letter in word:
            letter_count[letter] = letter_count.get(letter,0) + 1

        letter_keys = list(letter_count)
        letter_keys.sort()
        for letter in letter_keys:
            anagram_dict_key += ((letter,letter_count[letter]))
        anagram_dict.setdefault(anagram_dict_key,[]).append(word)

    return  anagram_dict

if __name__ == '__main__':
    word_file_path = "./words.txt"
    word_file_obj = open(word_file_path)
    word_list = []

    for line in word_file_obj:
        word_list.append(line.strip())

    anagrams = group_anagrams(word_list)
    for key in anagrams:
        if len(anagrams[key]) > 1:
            print(anagrams[key])
