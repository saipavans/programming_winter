def rotate_word(s,n):
    result = ""
    lower_case_ascii_list = list(range(ord("a"), ord("z")+1))
    upper_case_ascii_list = list(range(ord("A"), ord("Z")+1))
    for letter in s:
        if ord(letter) in lower_case_ascii_list:
            lower_letter_index = ord(letter) - ord("a")
            lower_letter_index_new = (lower_letter_index + n) % len(lower_case_ascii_list)
            result += chr(lower_case_ascii_list[lower_letter_index_new])
        elif ord(letter) in upper_case_ascii_list:
            upper_letter_index = ord(letter) - ord("A")
            upper_letter_index_new = (upper_letter_index + n) % len(upper_case_ascii_list)
            result += chr(lower_case_ascii_list[lower_letter_index_new])
        else:
            print("Contains non alphabet character")
            return ""
    return result

print(rotate_word("abcd",-3))
print(rotate_word("abyz",1))



