from collections import deque
import sys
input = sys.stdin.readline

tests = int(input())
for _ in range (tests):
    n_jobs, my_job = map(int, input().split())
    prior = list(map(int, input().split()))
    
    que = deque(list(enumerate(prior)))
    
    seq = 1 # 몇번째로 출력되었는지?    
    
    while len(que):
        # 우선 맥스 값 스캔
        top = 0
        for idx, pr in que:
            top = max(top, pr)
        
        if que[0][1] == top:
            if que[0][0] == my_job:
                break
            else:    
                que.popleft()
                seq += 1
        else:
            que.rotate(-1)
    print(seq)
            