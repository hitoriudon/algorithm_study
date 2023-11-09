n = int(input())
dots = [tuple(map(int, input().split())) for _ in range (n)]

def check(dot):
    line = [0 for _ in range (1001)] 
    num = 0
    for x1, x2 in dot:
        flag = True
        for i in range(x1, x2 + 1):
            if line[i] == 1:
                flag = False
                break
        if flag:
            for i in range (x1, x2 + 1):
                line[i] = 1
            num += 1
    return num

def f(cnt):
    global ans
    if cnt == n:
        ans = max(ans, check(arr))
        return
    
    # 전체 포문으로 모든 경우 (예를 들면 1,1,1 같이 겹치는 경우)를 볼 필요가 없음.
    arr.append(dots[cnt])
    f(cnt + 1)
    arr.pop()
    # 이렇게 추가만 해나가면 됨
    f(cnt + 1)
    
ans = 0
arr = []
f(0)
print(ans)