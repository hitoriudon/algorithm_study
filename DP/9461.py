t = int(input())
p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
idx_cnt = 5

for _ in range (90):
    p.append(p[-1] + p[idx_cnt])
    idx_cnt += 1

for _ in range (t):
    n = int(input())
    print(p[n-1])
    
# 뭔 다이나믹 프로그래밍이야 수학이구만