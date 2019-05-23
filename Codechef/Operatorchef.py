T=int(input())
while T>0:
    A,B=map(int,input().split())
    if A>B:
        print('>')
    elif A<B:
        print('<')
    elif A==B:
        print('=')
    T=T-1            
