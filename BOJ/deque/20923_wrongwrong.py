# 숫자 할리갈리 게임, S1, 2트

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
do_deck, su_deck = deque(), deque()

for _ in range (n):
    tx, ty = map(int, input().split()) # temp
    do_deck.appendleft(tx)
    su_deck.appendleft(ty)
    
do_ground, su_ground = [], []
def do_win():
    if len(do_ground) > 0 and do_ground[-1] == 5:
        return True
    elif len(su_ground) > 0 and su_ground[-1] == 5:
        return True
    
    return False

def su_win():
    if len(do_ground) > 0 and len(su_ground) > 0 and do_ground[-1] + su_ground[-1] == 5:    
        return True
    
    return False

def after_suyeon_win():
    time = len(do_ground)
    for _ in range (time):
        su_deck.append(do_ground.pop())
    
    time = len(su_ground)
    for _ in range (time):
        su_deck.append(su_ground.pop())
    
def after_dodo_win():
    time = len(su_ground)
    for _ in range (time):
        do_deck.append(su_ground.pop())
    
    time = len(do_ground)
    for _ in range (time):
        do_deck.append(do_ground.pop())

do_turn = True
for _ in range (m):
    if do_turn:
        do_ground.append(do_deck.popleft()) # 덱에서 카드 뽑아서 그라운드에 내려놓기
        if len(do_deck) == 0:
            break
            
        if su_win():
            after_suyeon_win()
        elif do_win():
            after_dodo_win()
        
        do_turn = False
    
    elif not do_turn:
        su_ground.append(su_deck.popleft())
        if len(su_deck) == 0:
            break

        if su_win():
            after_suyeon_win()
        elif do_win():
            after_dodo_win()
        
        do_turn = True

if len(do_deck) > len(su_deck):
    print("do")
elif len(do_deck) < len(su_deck):
    print("su")
elif len(do_deck) == len(su_deck):
    print("dosu")    