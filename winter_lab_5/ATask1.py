import string

def compress_file(file):
    """
    Removes whitespace and punctuation characters from the file
    :return: string with compressed file contents
    """
    file_reader = open(file)
    compressed_file_content = ""

    for line in file_reader:
        words = line.split()
        for word in words:
            for character_to_be_removed in string.punctuation + string.whitespace:
                word = word.replace(character_to_be_removed,"")
            compressed_file_content += word + "\n"

    return compressed_file_content

if __name__ == '__main__':
    input_file = "../resources/book1.txt"
    print(compress_file(input_file))



