# 11729, νλΈμ΄ ν, S1

n = int(input())

def hanoi(n, start, end, via):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n-1, start, via, end)
        print(start, end)
        hanoi(n-1, via, end, start)

print(2**n - 1)
hanoi(n, 1, 3, 2)