# 1439, 뒤집기, S5

s = input()

s1 = s.split('0')
s2 = s.split('1')

cnt1, cnt2 = 0, 0

for s in s1:
    if len(s) > 0:
        cnt1 += 1

for s in s2:
    if len(s) > 0:
        cnt2 += 1

print(cnt1 if cnt1 < cnt2 else cnt2)