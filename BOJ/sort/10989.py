# 10989, 수 정렬하기 3, B1

# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys

N = int(sys.stdin.readline())
counts = [0]*10000
for _ in range (N):
    n = int(sys.stdin.readline())
    counts[n-1] = counts[n-1] + 1
for i in range (10000):
    if counts[i] != 0: 
        for j in range (counts[i]): print(i+1)        
        #print((str(i)+"\n")*(counts[i]-1) + str(i))