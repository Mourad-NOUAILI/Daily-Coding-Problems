




lists = [[10, 15, 30], [12, 15, 20, 31], [17, 20, 32]]
one_sorted_list = []
for i in range(len(lists)):
    one_sorted_list = sorted([ *one_sorted_list, *lists[i] ])
print(one_sorted_list)
