n = 5
for i in range(n, 0, -1):
    print(' ' * (n - i) + ''.join(str(x) for x in range(1, i+1)))
