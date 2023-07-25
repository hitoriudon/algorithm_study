# 20923, 숫자 할리갈리 게임, S1

def dodo_win():
    for card in reversed(suyeon_ground):
            dodo_cards.append(card)
    suyeon_ground.clear()
    for card in reversed(dodo_ground):
        dodo_cards.append(card)
    dodo_ground.clear()
    
def suyeon_win():
    for card in reversed(dodo_ground):
        suyeon_cards.append(card)
    dodo_ground.clear()
    for card in reversed(suyeon_ground):
        suyeon_cards.append(card)
    suyeon_ground.clear()

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dodo_cards, suyeon_cards = deque([]), deque([])
for _ in range (N):
    do, su = map(int, input().split())
    dodo_cards.appendleft(do)
    suyeon_cards.appendleft(su)

dodo_ground, suyeon_ground = [], []
flag = True
if N == 1:
    M, flag = 0, False
    print("su")
for t in range (M//2):
    dodo_ground.append(dodo_cards.popleft())
    if len(dodo_cards) == 0 and len(suyeon_cards) == 1 and t < M - 1 and len(dodo_ground) * len(suyeon_ground) == 0: #
        print("dosuu")
        flag = False
        exit()
    elif len(dodo_cards) == 0 and len(suyeon_cards) != 0 and t < M - 1:
        print("su")
        flag = False
        exit()
    if dodo_ground[-1] == 5:
        dodo_win()    
    elif len(dodo_ground) != 0 and len(suyeon_ground) != 0:
        if dodo_ground[-1] + suyeon_ground[-1] == 5:
            suyeon_win()
    
    suyeon_ground.append(suyeon_cards.popleft())
    if len(suyeon_cards) == 0 and len(dodo_cards) == 1 and t < M - 1 and len(dodo_ground) * len(suyeon_ground) == 0:
        print("dosuu")
        flag = False
        exit()
    elif len(suyeon_cards) == 0 and len(dodo_cards) != 0 and t < M - 1:
        print("do")
        flag = False
        exit()
    if suyeon_ground[-1] == 5:
        dodo_win()    
    elif len(dodo_ground) != 0 and len(suyeon_ground) != 0:
        if dodo_ground[-1] + suyeon_ground[-1] == 5:
            suyeon_win()

do = len(dodo_cards)
su = len(suyeon_cards)

if flag:
    print("dosu" if do == su else ("do" if do > su else "su"))