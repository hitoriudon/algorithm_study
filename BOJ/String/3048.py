# 3048, 개미, S4
n1, n2 = map(int, input().split())
ant1 = list(input())
ant1.reverse()
ant2 = list(input())
time = int(input())

ant = ant1 + ant2
for _ in range (time):
    for i in range (len(ant) - 1):
        if (ant[i] in ant1) and (ant[i+1] in ant2):
            ant[i], ant[i+1] = ant[i+1], ant[i]
            if ant[i+1] == ant1[-1]:
                break

print(''.join(ant))