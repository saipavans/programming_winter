import string

def words_counter(file_list):
    result = []
    for file in file_list:
        file_reader = open(file)
        total_word_count = 0
        words_counter = {}

        for line in file_reader:
            words = line.split()
            for word in words:
                words_counter[word] = words_counter.get(word,0) + 1
                total_word_count += 1
        file_reader.close()

        result.append((words_counter, total_word_count))

    return result

if __name__ == '__main__':
    input_file_list = ["./resources/The_new_england_country.txt", "./resources/cape_cod.txt"]
    word_details_list = words_counter(input_file_list)
    highest_words = 0
    highest_words_book_index = 0
    for i in range(len(input_file_list)):
        if (word_details_list[i][1]) > highest_words:
            highest_words = (word_details_list[i][1])
            highest_words_book_index =  i
    print("Book with the highest words is '" + input_file_list[highest_words_book_index] + "' with " + str(highest_words) + " number of words")
