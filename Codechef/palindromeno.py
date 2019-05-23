T=int(input())
while T>0:
    N=input()
    if N==N[::-1]:
        print('wins')
    else:
        print('losses')
    T=T-1      
