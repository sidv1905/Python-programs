T=int(input())
while T>0:
    l=int(input())
    N=input()
    N=N.upper()
    if 'Y' in N:
        print('NOT INDIAN')
    elif 'I' in N:
        print('INDIAN')
    else:
        print('NOT SURE')
    T=T-1
