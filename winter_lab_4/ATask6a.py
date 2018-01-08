def has_duplicates(input_list):
	return not(len(input_list) == len(set(input_list)))

list1 = [1,2,3,4,3]
list2 = [2,4,5,3]
list3 = ['a','b','cad']

print(has_duplicates(list1))
print(has_duplicates(list2))
print(has_duplicates(list3))