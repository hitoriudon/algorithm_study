from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
cards = Counter([int(input()) for _ in range (n)])

max_count = max(cards.values())
max_list = []
for card in cards.keys():
    if cards[card] == max_count:
        max_list.append(card)
print(sorted(max_list)[0])