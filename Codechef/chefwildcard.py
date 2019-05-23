T=int(input())
while T>0:
    X=input()
    Y=input()
    c=0
    for i in range(len(X)):
        if(X[i]!=Y[i] and (X[i]!='?' and Y[i]!='?')):
            c=1
            break
    if c==0:
        print('Yes')
        
    else:
        print('No')
    T=T-1
