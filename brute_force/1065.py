# 1065, 한수, S4

# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

N = int(input())
num = 99
if N <= 99:
    print(N)
elif 100 <= N <= 110:
    print(num)
else:
    for n in range (111, N+1):
        # 자연수 n을 str로 바꿔준 다음 각 자리를 쪼개서 리스트로 만들고, 그 각 요소들을 map 함수를 이용해 int로 형변환해서 다시 리스트
        seq = list(map(int, list(str(n)))) 
        diff = [(seq[i+1] - seq[i]) for i in range (len(seq) - 1)] # 차이들의 배열
        if len(set(diff)) == 1: # diff의 모든 값이 같으면, 즉 차이가 모두 같으면, set의 길이는 1
            num += 1
    print(num)

# diff를 저렇게 안 해도 됐는데... 난 모든 수에 대한 코드고
# N <= 1000이라서 사실 걍 seq[2] - seq[1] == seq[1] - seq[0] 으로 하기만 하면 됐음
# 뭐 그래도 바로 통과했으니 괜찮