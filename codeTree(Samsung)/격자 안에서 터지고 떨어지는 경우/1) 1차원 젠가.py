n = int(input())
jenga = [int(input()) for _ in range (n)]
outs = []
for _ in range (2):
    x, y = map(int, input().split())
    outs.append((x, y))

for x, y in outs:
    temp = []
    for i in range (1, len(jenga) + 1):
        if i < x or i > y:
            temp.append(jenga[i - 1])
    
    jenga = [temp[i] for i in range (len(temp))] # copy

print(len(jenga))
for num in jenga:
    print(num)