d=int(input())
count=0
sum1=0
r,x=map(int , input().split())
area=44/7*r
capable=100*x
while d<0:
    while area<=capable:
        sum1=area+sum1
        if area<=capable:
            count+=1
        elif area==capable:
            count+=1
            break
    d=d-1
print(count)
