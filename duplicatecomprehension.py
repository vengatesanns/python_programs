some_list = ['a', 'b', 'a', 'c', 'd', 'r', 'd']

duplicates = set([item for item in some_list if some_list.count(
    item) > 1])

print(duplicates)
