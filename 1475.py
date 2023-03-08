# 방번호 실버5 구현
from collections import Counter

n = input()
c = Counter(n)
list1 = sorted(c.most_common(), key = lambda x: (x[1], x[0]), reverse= True)

first_key, first_value = int((c.most_common())[0][0]), int((c.most_common())[0][1])
if len(c) >= 2:
    second_key, second_value = int(list1[1][0]), int(list1[1][1])
else:
    second_key, second_value = 0, 0
if first_key == 6 or first_key == 9:
    if second_key == 6 or second_key == 9:
        count = first_value + second_value
        print((count // 2) + 1 if count % 2 == 1 else count // 2)
    else:
        print((first_value//2) + 1 if first_value % 2 == 1 else first_value//2)
else:
    print(first_value)

#words = sorted(set([input() for _ in range (N)]), key = lambda x: (len(x), x))