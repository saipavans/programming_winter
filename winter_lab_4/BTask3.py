def print_hist(input_map):
    key_list = list(input_map.keys())
    key_list.sort()
    for key in key_list:
        print(key, input_map[key])


input_hist = {'John': 90, 'Doe': 95, 'Jane': 100}
print_hist(input_hist)
