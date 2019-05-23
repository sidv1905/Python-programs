n=int(input())
for i in range(n):
    for i in range(n):
        print('  --- ', sep=' ', end='', flush=True)
    print('\n')
    for i in range(n+1):
        print(' | ', sep='  ', end='  ', flush=True)
    print('\n')
    for i in range(n):
        print('  --- ', sep=' ', end='', flush=True)
