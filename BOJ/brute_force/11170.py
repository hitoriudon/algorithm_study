testcase = int(input())
for _ in range (testcase):
    answer = 0
    n, m = map(int, input().split())     
    for i in range (n, m + 1):
        answer += str(i).count('0')
    print(answer)