string = input()

answer = 0
for i in range (len(string) - 1): # 전체 완전탐색
    if string[i] == string[i+1] == '(': # 동시 체크
        for j in range (i+2, len(string) - 1): # 이후 괄호 다음부터 개수 세기 시작
            if string[j] == string[j+1] == ')':
                answer += 1
print(answer)