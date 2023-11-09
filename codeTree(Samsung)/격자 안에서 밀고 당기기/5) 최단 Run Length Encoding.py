from collections import deque

alphabet = deque(input())

min_num = 50 # 임의 숫자

for cnt in range (len(alphabet)):
    chars = []
    alphabet.rotate(1) # right shift
    recent = alphabet[0]
    chars.append([recent, 1])
    
    for i in range (1, len(alphabet)):
        current = alphabet[i]
        if current == recent:
            chars[-1][1] += 1
        elif current != recent:
            recent = current
            chars.append([recent, 1])
    
    chars = list(map(lambda x: [x[0], str(x[1])], chars))
    answer = ''
    
    for c, n in chars:
        answer += (c + n)
    
    min_num = min(min_num, len(answer))

print(min_num)