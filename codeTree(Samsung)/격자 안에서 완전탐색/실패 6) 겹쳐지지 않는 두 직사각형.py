# board = [
#     [1,2,3,4],
#     [12,13,14,15],
#     [113,114,115,116],
#     [1114,1115,1116,1117]
# ]
# for i in range (4):
#     for j in range (4):
#         temp = []
#         for k in range (i + 1):
#             temp.append(board[k][:j+1])
#         print(temp)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range (n)]

max_sum = (-1000) * n * m

for i in range (n): # r
    for j in range (m): # c
        for k in range (i, n): # r
            for l in range (j, m): # c
                first = []
                for o in range (k+1):
                    first.append(graph[o][:l+1])
                # print(first)
                end_x, end_y = len(first) - 1, len(first[0]) - 1
                for a in range (n):
                    for b in range (m):
                        if (i != a and j != b) and (end_x < a or end_y < b): # 안 겹친다!
                            for c in range (a, n):
                                for d in range (b, m):
                                    second = []
                                    for e in range (c + 1):
                                        second.append(graph[c][:d+1])
                                        print(a,b,c,d)
                                    print(first, second)
                
                
                
                
# 4 5
# +6 +5 +4 -3 +1
# +3 -4 -4 14 +1
# +6 +1 -3 15 -5
# +3 -5 +1 16 +3