T = int(input())
ans = []
for t in range (1, T+1):
    n = int(input())
    tree = list(map(int, input().split()))
    maxHeight = max(tree)
    answer = 0
    
    # (내가 짠 게 그리디인지 모르겠음...)
    # 접근) 
    # 짝수 날에 성장을 최대한 할 수 있는 게 이득이다.
    # 그렇다고 홀수 날을 쉬고 짝수 날에 성장을 하는 건 의미가 없다(하루 쉬어야 해서 최소 일수가 어차피 증가함)
    # 홀수 날엔 홀수 값을 가지는 나무를 성장시키고, 짝수 날에는 짝수 값을 가지는 나무를 성장시키는,
    # 균형을 잡는 게 이 문제를 푸는 포인트인 거 같다.
    
    # 짝수로 성장이 가능한 횟수가 even, 홀수 성장이 필요한 횟수가 odd이다.
    odd, even = 0, 0
    for i in range (n):
        heightDifference = maxHeight - tree[i]
        even += heightDifference // 2
        odd += heightDifference % 2
    
    # 균형 맞추기. 짝수 카운트와 홀수 카운트를 같게 만들기 위함이다(균형).
    # odd가 even보다 크거나 같아아 한다. 짝수는 쉴 수도 있는 경우가 있지만 홀수는 쉬는 경우가 없다.
    # 내가 무슨 말을 하는지 모르겠지만 홀수 2일은 짝수 1일로 대체될 수 있다. 그래서 짝수는 쉴 수 있는 경우가 있다.
    # 근데 홀수 1일은 어떤 경우에도 대체될 수 없다. 그래서 홀수는 쉬는 경우가 없다고 하는 것.
    # 그래서 even을 최대한으로 만들면서, odd보다는 작거나 같아야 한다.
    if even > odd:
        while abs(even - odd) > 1:
            even -= 1
            odd += 2
    if (odd > even):
        answer = odd * 2 - 1
    elif (even > odd):
        answer = even * 2
    else:
        answer = odd + even
        
    ans.append("#" + str(t) + " " + str(answer))

for a in ans:
    print(a)
    
    
    
    # while 이후 answer 계산할 때 틀렸던 가설
    # 근데 저렇게 while을 -1, +2하면 짝수 홀수가 같지 않고 홀수가 큰 경우가 당연히 생긴다.
    # 만약 even odd가 같으면 너무 좋은 상황이다. 홀짝홀짝홀짝홀짝 반복하면서 쭉 나아가면 되기 때문이다.
    # 그래서 밑의 max 코드는 짝 홀이 같은 경우엔 같은 값을 리턴할 것이다. 
    # 근데 odd가 크다면? odd가 even보다 커봤자 1 아니면 2다.
    # 1 크면 홀짝홀짝홀짝(=even * 2) 반복하고 홀 하면 끝난다.
    # odd가 even보다 2 크면? 홀수인 날 하루 쉬고 짝수인 날 물을 줘야 한다. 그래서 어차피 이틀이 소요된다.
    # 그럼 밑의 max 코드는 even + odd 값을 리턴할 것이다.
    # answer = max(even * 2, even + odd)