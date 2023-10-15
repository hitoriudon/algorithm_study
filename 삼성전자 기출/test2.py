# grid = [
#     [
#         [1, 2], [3, 4], [5, 6]
#     ],
#     [
#         [0], [7, 8], [0, 0]
#     ],
#     [
#         [7, 8], [2, 0], [3, 3]
#     ]   
# ]
# for line in grid:
#     print(line)

# print()
# grid = list(zip(*grid[::-1]))
# for line in grid:
#     print(line)

def is_range(x, y):
    return x >= 0 and x < 5 and y >= 0 and y < 5

grid = [[1,2,3,4,5], 
        [4,5,6,7,8], 
        [7,8,9,0,1], 
        [2,3,4,5,6], 
        [3,4,5,6,7]
]
for length in range (1, 5):
    for x in range (5):
        for y in range (5):
            rx, ry = x + length, y + length
            if is_range(rx, ry):
                temp =[]
                for i in range (x, rx + 1):
                    temp2=[]
                    for j in range (y, ry + 1):
                        temp2.append(grid[i][j])
                    temp.append(temp2)
                for line in temp:
                    print(line)
                print()