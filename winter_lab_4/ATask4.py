def is_sorted(in_list):
    sorted = True
    for i in range(0,len(in_list)-1):
        if in_list[i] > in_list[i+1]:
            sorted = False
            break
    return sorted

print(is_sorted([1,2,2]))
print(is_sorted(['b','a']))
        