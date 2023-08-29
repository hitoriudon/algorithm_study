size, gold_value = map(int, input().split())
golds = [list(map(int, input().split())) for _ in range (size)]
max_gold_count = 0

dots = [[(0, 0)]]
max_k = 0
while max_k < size - 1: # 다 덮을 정도까지만 미리 다 만들어 놓기
    next_list = []
    for x, y in dots[-1]:
        next_list.append((x, y))
        next_list.append((x+1, y))
        next_list.append((x-1, y))
        next_list.append((x, y+1))
        next_list.append((x, y-1))
    next_list = set(next_list) # 겹치는 부분 set로 제외
    dots.append(next_list)
    max_k += 1

def is_range(x, y): 
    return x >= 0 and x < size and y >= 0 and y < size

for i in range (size): # 진짜 완전탐색
    for j in range (size): # 모든 인덱스 다 돌기
        for k in range (max_k + 1): # 최소 마름모부터 최대 마름모까지 모두
            cost, expected_gold = 0, 0 # cost 공식은 결국 마름모의 크기랑 동일
            for x, y in dots[k]: # 마름모 좌표 완전탐색
                nx, ny = i + x, j + y
                if is_range(nx, ny) and golds[nx][ny] == 1:
                    expected_gold += gold_value
                cost += 1 # 범위 밖이라고 하더라도 cost는 증가시켜야 함
            if (expected_gold - cost) >= 0: # 손해라고 하길래 자연수만 해당되는 줄 알았는데, 0도 포함이었음(테케로 확인)
                max_gold_count = max(max_gold_count, expected_gold // gold_value) # 최댓값 최신화

print(max_gold_count)