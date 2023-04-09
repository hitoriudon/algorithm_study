n, m = map(int, input().split())
cards = []
for _ in range (n):
    cards.append(list(map(int, input().split())))

answer = 0
for card in cards:
    chosen_card = min(card)
    if answer < chosen_card:
        answer = chosen_card
        
print(answer)