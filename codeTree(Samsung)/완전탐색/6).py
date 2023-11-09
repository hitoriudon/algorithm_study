binary = input()

if '0' not in binary:
    print(int(binary, 2) - 1)
else:
    idx = 0
    binary = list(binary)
    while True:
        if binary[idx] == '1':
            idx += 1
        else:
            binary[idx] = '1'
            binary = ''.join(binary)
            print(int(binary, 2))
            break