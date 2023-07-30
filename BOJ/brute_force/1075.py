n = int(input())
f = int(input())

front = int(str(n)[:-2]) # 정수 n의 마지막 두 자리 전까지 문자열 타입으로 바꾸고 다시 정수형 타입으로 바꾸기
candidate = [] # 나누어 떨어지는 값들을 이 배열에 담아야 함. 최소값을 답으로 내야 하기 때문에!

for _ in range (100):
    last = int(str(n)[-2:]) # 정수 n의 마지막 두 자리를 문자열 타입으로 바꾸고 다시 정수형 타입으로 바꾸기
    if n % f == 0:
        candidate.append(last) # 후보에 추가하기
    
    last = (last + 1) % 100 # 맨 마지막 두 자리만 바꿔줘야 하기 때문!
    if len(str(last)) == 1: # last가 1이면 01로 바꿔주기
        last_string = "0" + str(last) # 십의 자리에 0 붙여주기
        # n = 23400이라면, front는 234, last_string은 00이다. 그래서 "234" + "00"을 더해준 "23400"을 int로 바꿔준 정수 값을 n으로 만들어주기.
        n = int(str(front) + last_string) 
    else:
        n = int(str(front) + str(last)) # 이것도 마찬가지.

answer = min(candidate) # 마지막 두 자리만 들어있는 값들 중 최소값이 answer에 들어갈 것.
print("0" + str(answer) if len(str(answer)) == 1 else answer) # answer가 일의 자리 수라면 "0" 붙여줘야 해서.