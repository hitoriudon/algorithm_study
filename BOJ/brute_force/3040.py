# 3040, 백설 공주와 일곱 난장이, B2, import 사용 금지

dwarf = []
total = 0
for _ in range (9):
    dwarf.append(int(input()))
    total += dwarf[-1]
    
fake_index = [0, 0]
for i in range (9):
    for j in range (i + 1, 9):
        if total - (dwarf[i] + dwarf[j]) == 100:
            fake_index = [i, j]

for index in range (9):
    if index not in fake_index:
        print(dwarf[index])