n = int(input("N: "))
k = int(input("MINIMUM: "))
m = int(input("MAXIMUM: "))
arr = []

# n개 중 최대 m개를 뽑는 백트래킹 조합
print("\n******************************")
print(str(n) + "개 중 최대 " + str(m) + "개를 뽑는 백트래킹 조합")
def f1(level, begin):
    if level == m:
        print(arr)
        return
    for i in range (begin, n):
        arr.append(i)
        f1(level + 1, i + 1)
        arr.pop()
    f1(level + 1, begin + 1)
f1(0,0)

# n개 중 최소 k개를 뽑는 백트래킹 조합
print("\n******************************")
print(str(n) + "개 중 최소 " + str(k) + "개를 뽑는 백트래킹 조합")
def f2(level, begin):
    if level == n:
        if len(arr) >= k:
            print(arr)
        return
    arr.append(begin)
    f2(level + 1, begin + 1)
    arr.pop()
    
    f2(level + 1, begin + 1)
f2(0,0)

# n개 중 최소 k개, 최대 m개 뽑는 조합
print("\n******************************")
print(str(n)+ "개 중 최소 " + str(k) + "개, 최대 " + str(m) + "개 뽑는 조합")
def f3(level, begin):
    if level == n:
        if m >= len(arr) >= k:
            print(arr)
        return
    arr.append(begin)
    f3(level + 1, begin + 1)
    arr.pop()
    f3(level + 1, begin + 1)
f3(0,0)

