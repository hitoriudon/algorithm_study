# 369, B3

n = int(input())
clap = 0

for i in range (1, n + 1):
    num = str(i)    
    for index in range (len(num)):
        if num[index] == '3' or num[index] == '6' or num[index] == '9': 
            clap += 1
            
print(clap)