def histogram(input):
    result = {}
    for letter in input:
        result[letter] = result.get(letter, 0) + 1
    return result


print(histogram('ababcd'))
