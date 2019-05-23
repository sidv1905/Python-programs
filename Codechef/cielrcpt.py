T=int(input())

while T>0:
    p=int(input())
    for i in range(1,12):
        closer=(2**i-1)
        if closer==p:
            print(1)
        if closer<p:
