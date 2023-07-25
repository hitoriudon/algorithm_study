def fib(n):
    global cnt1
    cnt1 += 1
    if n == 1 or n == 2:
        cnt1 -= 1
        return 1
    else:
        return fib(n-1) + fib(n-2)
def fibo(n):
    global cnt2
    arr = [1,1]
    for i in range (2, n):
        arr.append(arr[i-1]+arr[i-2])
        cnt2 += 1
    return arr[n-1]

n = int(input())
cnt1, cnt2 = 0, 0
fib(n)
fibo(n)
print(cnt1 + 1, cnt2)

# cnt1, cnt2를 어떻게 반영해야할지 어려웠음...