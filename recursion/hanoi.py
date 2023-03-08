# 11729, 하노이 탑, S1

n = int(input())
msg = "{}번 원반을 {}에서 {}으로 이동했습니다."

def move(n, start, end):
    print(msg.format(n, start, end))

def hanoi(n, start, end, via):
    if n == 1:
        move(1, start, end)
        return
    else:
        hanoi(n-1, start, via, end)
        move(n, start, end)
        hanoi(n-1, via, end, start)

print(2**n - 1)

try:
    hanoi(n, "A", "C", "B")
except NameError as error:
    print("비상비상! %s 발생했어요!! 프로그램 종료할게요!" %error)