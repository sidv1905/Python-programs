t=int(input())
while t>0:
    count=0
    a=input()
    distinct=set(a)
    b=input()
    for x in range(len(distinct)):
        for y in range(len(b)):
            if a[x]==b[y]:
                count+=1
                break
    print((int(len(distinct))-count)+(int(len(b))-count))
    t=t-1
