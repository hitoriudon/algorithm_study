# 문제 똑바로 좀 읽자 1 이상 4 이하의 자연수래잖아...

def is_range(idx):
    return idx < n

def check():
    restart_idx = 0
    for idx in range (n):
        if idx < restart_idx:
            continue
        
        value = arr[idx]
        progress = 0
        for j in range (value):
            if is_range(idx + j) and arr[idx] == arr[idx + j]:
                progress += 1
        if value != progress:
            return False
        
        restart_idx = idx + value
    
    return True

def f(cnt):
    global ans
    if cnt == n:
        if check():
            ans += 1
        return
    
    for i in range (1, 5): # ㅅㅂ 여기만 바꾸면 됐네
        arr.append(i)
        f(cnt + 1)
        arr.pop()
        
n = int(input())
ans = 0
arr = []

f(0)
print(ans)


# 똑바로 안 읽고 모든 수에 대해서 다 했음

# def is_range(idx):
#     return idx < n

# def check():
#     restart_idx = 0
#     for idx in range (n):
#         if idx < restart_idx:
#             continue
        
#         value = arr[idx]
#         progress = 0
#         for j in range (value):
#             if is_range(idx + j) and arr[idx] == arr[idx + j]:
#                 progress += 1
#         if value != progress:
#             return False
        
#         restart_idx = idx + value
    
#     return True

# def f(cnt):
#     global ans
#     if cnt == n:
#         if check():
#             ans += 1
#             print(arr, ans)
#         return
    
#     for i in range (1, n + 1):
#         arr.append(i)
#         f(cnt + 1)
#         arr.pop()
        
# n = int(input())
# ans = 0
# arr = []

# f(0)
# print(ans)