def invert_dict(input_dict):
    inverse = {}
    for key in input_dict.keys():
        val = input_dict[key]
        inverse.setdefault(val, list()).append(key)
    return inverse


input = {'a': 1, 'b': 1, 'c': 2}
print(invert_dict(input))
