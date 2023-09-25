X = int(input())
for i in range (4500): # 조건 X(1 ≤ X ≤ 10,000,000)의 근사값
    start, end = sum(range(i+1)), sum(range(i+2))
    if start < X <= end:
        if i % 2 == 0:
            bunza, bunmo = i + 1, 1
            
            for idx in range (start + 1, end + 1):
                if idx == X:
                    print(str(bunza) + "/" + str(bunmo))
                    break
                bunza, bunmo = bunza - 1, bunmo + 1
                
        elif i % 2 == 1:
            bunza, bunmo = 1, i + 1

            for idx in range (start + 1, end + 1):
                if idx == X:
                    print(str(bunza) + "/" + str(bunmo))
                    break
                bunza, bunmo = bunza + 1, bunmo - 1
        break