n = int(input())

member = {'A': 0, 'B': 0}
glory = [True, True]
change = 0

for _ in range (n):
    c, s = map(str, input().split())
    member[c] += int(s)
    
    # copy
    before_glory = [False, False]
    for i in range (2):
        before_glory[i] = glory[i]
    
    if member['A'] < member['B']:
        glory = [False, True]
        
    elif member['A'] > member['B']:
        glory = [True, False]

    elif member['A'] == member['B']:
        glory = [True, True]
    
    if glory != before_glory:
        change += 1
    
    print(member)
    print(change, glory)
print(change)