def reverse_lookup(input_dict, value):
    res_keys = []
    for key in input_dict.keys():
        if input_dict[key] == value:
            res_keys.append(key)
    return res_keys


input = {'a': 1, 'b': 1, 'c': 2}
print(reverse_lookup(input, 1))
print(reverse_lookup(input, 2))
