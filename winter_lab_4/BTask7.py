def has_duplicates(in_list):
    res = {}
    for item in in_list:
        res[item] = res.get(item, 0) + 1
        if res[item] > 1:
            return True
    return False


print(has_duplicates([1, 2, 1]))
print(has_duplicates([1, 2, 3]))
