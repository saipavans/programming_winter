def has_three_pairs(word):
    triple_occurence_counter = 0
    i = 0
    while i < (len(word) - 1) and triple_occurence_counter<3:
        if word[i] == word[i + 1]:
            triple_occurence_counter += 1
            i += 2  # incrementing by 2, to avoid mistaking three 'aaa' as two time 'aa'
        else:
            i += 1
            triple_occurence_counter = 0  ## break of pattern
    return (triple_occurence_counter == 3)

def has_two_pairs(word):
    double_occurence_counter = 0
    i = 0
    while i < (len(word) - 1) and double_occurence_counter<2:
        if word[i] == word[i + 1]:
            double_occurence_counter += 1
            i += 2  # incrementing by 2, to avoid mistaking three 'aaa' as two time 'aa'
        else:
            i += 1
            double_occurence_counter = 0  ## break of pattern
    return (double_occurence_counter == 2)


if __name__ == '__main__':
    words_file_name = "./words.txt"
    words_file = open(words_file_name)
    print("Words with three consecutive double letters")
    for line in words_file:
        if has_three_pairs(line):
            print(line)
    print("Words with two consecutive double letters")
    for line in words_file:
        print(line)
        if has_two_pairs(line):
            print(line)