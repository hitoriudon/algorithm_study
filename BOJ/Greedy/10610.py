# 10610, 30, S4, 2트

# 3의 배수는 각 자리 합이 3의 배수여야 함.

num = input()
if '0' not in num:
    print(-1)
else:
    total = 0
    for n in num:
        total += int(n)
    if total % 3 == 0:
        print(''.join(sorted(num, reverse = True)))
    else:
        print(-1)