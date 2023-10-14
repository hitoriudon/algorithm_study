# arr = []
# eat = []

# def f(level, begin):

#     if level == 3:
#         if len(arr) == 3:
#             print(arr)
            
#         return
#     for i in range (begin + 1, 5):
#         arr.append(i)
#         f(level + 1, begin)
#         arr.pop()
#     f(level + 1, begin + 1)

# for _ in range (2):
#     f(0, 0)

# from copy import deepcopy
# grid = [1,2,3,0,0,0]
# copy_grid = deepcopy(grid)
# grid = [0,0,0,2,3,4]
# print(grid, copy_grid)
# copy_grid = deepcopy(grid)
# print(grid,copy_grid)

dx = [0, -1, 0, 0]
dy = [0, 0, 0, 1] 
# 상 하 우
set1 = list(set(zip(dx, dy)))

