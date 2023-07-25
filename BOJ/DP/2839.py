# 2839, 설탕 배달, S3

N = int(input())

bag_list = []

# 3kg와 5kg 봉지의 개수를 모두 고려한다.
for i in range(N // 3 + 1):
    for j in range(N // 5 + 1):
        # 3kg 봉지 i개와 5kg 봉지 j개를 사용할 때, N kg의 설탕을 만들 수 있다면
        if i * 3 + j * 5 == N:
            bag_list.append(i + j)

# 봉지 수가 없는 경우 -1을 출력한다.
if not bag_list:
    print(-1)
else:
    # 가능한 모든 경우의 봉지 수 중 최소값을 출력한다.
    print(min(bag_list))