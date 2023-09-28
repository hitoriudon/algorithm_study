n, m = map(int, input().split())
bombs = [int(input()) for _ in range (n)]

def check(start, value):
    for i in range (start + 1, len(bombs)):
        if value != bombs[i]:
            return i - 1 # 처음부터 안 같으면 그냥 그 자리 그대로 반환하도록
    return len(bombs) - 1

while True:
    flag = False
    for curr_idx, number in enumerate(bombs):
        if number == 0:
            continue
        end_idx = check(curr_idx, number)
        
        if end_idx - curr_idx + 1 >= m:
            flag = True
            # bombs[curr_idx: end_idx + 1] = 0 이렇게 쓰면 안 됨
            bombs[curr_idx: end_idx + 1] = [0] * (end_idx - curr_idx + 1)
        
    bombs = list(filter(lambda x: x > 0, bombs))
    
    if not flag:
        break
print(len(bombs))
for bomb in bombs:
    print(bomb)