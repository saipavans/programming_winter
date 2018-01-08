def most_frequent(phrase):
    hist = {}
    for letter in phrase:
        hist[letter] = hist.get(letter, 0) + 1
    value_sorted_letters = sorted(hist, key=hist.get, reverse=True)
    for letter in value_sorted_letters:
        print(letter, hist[letter])


most_frequent("helloo")
