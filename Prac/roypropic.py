L=int(input())
N=int(input())
while N>0:
    W,H=map(int , input().split())
    if W<L or H<L:
        print('UPLOAD ANOTHER')
    elif W>L or H>L:
        print('CROP IT')
    elif W==L and H==L:
        print('ACCEPTED')
    N=N-1
