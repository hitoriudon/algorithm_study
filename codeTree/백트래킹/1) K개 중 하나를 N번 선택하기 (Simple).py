k, n = map(int, input().split())
ans = []

def f(cnt):
    if cnt == n:
        for num in ans:
            print(num, end=" ")
        print()
        return
    
    for value in range (1, k + 1):
        ans.append(value)
        f(cnt + 1)
        ans.pop()
f(0)