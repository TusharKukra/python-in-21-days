n = 5
# Upper part of the diamond
for i in range(1, n+1):
    print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*' if i > 1 else ' ' * (n - i) + '*')

# Lower part of the diamond
for i in range(n-1, 0, -1):
    print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*' if i > 1 else ' ' * (n - i) + '*')
