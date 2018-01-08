def sort_by_length(words):
    t = {}
    for word in words:
        t.setdefault(len(word),set()).add(word)
    sorted_keys = list(t)
    sorted_keys.sort(reverse=True)

    res = []
    print(sorted_keys)
    for key in sorted_keys:
        res.append(t[key])

    return res

print(sort_by_length(["python","abc","ink","cab","encyclopedia"]))