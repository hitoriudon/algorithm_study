n = int(input())
cow = input()   

answer = 0
for i in range (n-2): # 'C' 한정 전체 완전탐색인데, 어차피 'COW'가 되는 조건은 마지막에서 -2번째까지가 'C'가 되어야 함.
    for j in range (i+1, n-1):
        for k in range (j+1, n):
            if cow[i] == 'C' and cow[j] == 'O' and cow[k] == 'W':
                answer += 1
print(answer)