n = 5
for i in range(n):
    num = 1
    for j in range(1, n - i):
        print(' ', end="")
    for j in range(0, i+1):
        if j == 0 or j == i:
            print(num, end=" ")
        else:
            num = num * (i - j + 1) // (j)
            print(num, end=" ")
    print()
