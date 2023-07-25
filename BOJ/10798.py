# runtime, indexerror
words = []
max_len = 0
'''for _ in range (5):
    string = input()
    if len(string) >= max_len:
        max_len = len(string)
    elif len(string) < max_len:
        string += "@" * (max_len - len(string))
    words.append(string)'''

for _ in range (5):
    string = input()
    string += "@" * (15 - len(string))
    words.append(string)
    
for j in range (15):
    for i in range (5):
        if words[i][j] != '@':
            print(words[i][j], end="")