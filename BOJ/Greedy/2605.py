n = int(input())
sequence = list(map(int, input().split()))
answer = []

for i in range (n):
    if sequence[i] == 0:
        answer.insert(0, str(i+1))
    else:
        answer.insert(sequence[i], str(i+1))
print(' '.join(reversed(answer)))