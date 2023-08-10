# 10610, 30, S4 메모리 초과
from itertools import permutations
n = input()
if '0' not in n:
    print(-1)
else:
    n = sorted(list(n), reverse=True)
    strings = list(permutations(n[:-1], len(n) - 1))
    for i in range (len(strings)):
        temp = int(''.join(strings[i]))
        if temp % 3 != 0 or len(str(temp)) != len(n) - 1:
            strings[i] = -1
        else:
            strings[i] = int(temp)
    print(-1 if max(strings) == -1 else str(max(strings)) + '0')