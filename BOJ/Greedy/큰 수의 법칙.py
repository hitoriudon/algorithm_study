n, m, k = map(int, input().split())
inputs = list(map(int, input().split()))
numbers = []
for i in inputs:
    numbers.append([i, 0])
total = 0
first, second = sorted(numbers, reverse=True)[0], sorted(numbers, reverse=True)[1]

for _ in range (m):
    if first[1] < k:
        total += first[0]
        first[1] += 1
    else:
        total += second[0]
        first[1] = 0
print(total)