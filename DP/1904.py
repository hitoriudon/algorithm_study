from itertools import permutations

list1 = ['00', '1', '1', '1', '1']

tmp = set(list(permutations(list1, 4)))
list2 = []
for i in tmp:
    i = ''.join(list(i))
    if '00' in i:
        list2.append(''.join(i))
print(list2)