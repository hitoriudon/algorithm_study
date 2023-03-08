# 10872, 팩토리얼, B5

# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 첫째 줄에 N!을 출력한다.

d = [0] * 20
def f(x):
    if x == 0 or x == 1:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = x * f(x-1)
    return d[x]
n = int(input())
print(f(n))