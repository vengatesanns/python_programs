dummy_list = ['a', 'b', 'c', 'b', 'e', 'd', 'e']

result_list = []
for item in dummy_list:
    if dummy_list.count(item) > 1 and item not in result_list:
        result_list.append(item)


print(result_list)
