import heapq

n = int(input())

vote = []
for i in range (1, n + 1):
    v = int(input())
    vote.append([(-1) * v, (-1) * i])
    
heapq.heapify(vote)

cnt = 0
while not vote[0][1] == -1:
    for i in range (n):
        v, pnum = vote[i]
        if pnum == -1:
            vote[i][0] -= 1
            vote[0][0] += 1
            cnt += 1
            break
    heapq.heapify(vote)

print(cnt)