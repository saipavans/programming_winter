### palindrome.py ###

def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


######## C Task 2 -1 ##########

print("testing middle with two letters ", middle("pq"))
print("testing middle with one letter", middle("p"))
print("testing middle with empty string", middle(""))


######## C Task 2 -2  #############
def is_palindrome(word):
    result = True
    if len(word) > 2:
        if first(word) == last(word):
            is_palindrome(middle(word))
        else:
            result = False
    return (result)


print("Is the word redivider palindrome?", is_palindrome("redivider"))
print("Is the word redividend palindrome?", is_palindrome("redividend"))



