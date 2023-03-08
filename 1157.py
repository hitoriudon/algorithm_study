from collections import Counter
string = input().upper()

dic = dict(Counter(string))
maxnum = max(dic.values())
if list(dic.values()).count(maxnum) >= 2:
    print("?")
else:
    for k in dic:
        if dic[k] == maxnum:
            print(k)