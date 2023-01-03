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