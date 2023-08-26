n = int(input())
nums = [int(input()) for _ in range (n)]
max_num = 0

for i in range (n): # 전체 완전 탐색
    for j in range (i+1, n):
        for k in range (j+1, n):
            n1, n2, n3 = str(nums[i]), str(nums[j]), str(nums[k])
            n1, n2, n3 = (5 - len(n1)) * '0' + n1, (5 - len(n2)) * '0' + n2, (5 - len(n3)) * '0' + n3
            n1, n2, n3 = list(map(int, n1)), list(map(int, n2)), list(map(int, n3))
            
            temp = 0
            for l in range (5): 
                current_digit = n1[-(l+1)] + n2[-(l+1)] + n3[-(l+1)]
                if current_digit > 9: # carry 발생
                    temp = 0
                    break
                elif current_digit <= 9:
                    temp += current_digit * (10 ** l)
            max_num = max(max_num, temp)

print(max_num if max_num > 0 else -1)



# 6
# 522
# 6
# 84
# 7311
# 19
# 9999