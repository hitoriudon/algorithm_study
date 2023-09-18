score = sorted([(int(input()), i) for i in range (8)], reverse= True)

high_5 = sorted(score[:5], key = lambda x: (x[1]))

max_num = 0
for i in range (5):
    max_num += high_5[i][0]
    
print(max_num)
for i in range (5):
    idx = high_5[i][1] + 1
    print(idx, end=" ")