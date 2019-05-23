a=list(map(int , input().split()))
b=list(map(int , input().split()))
counta=0
countb=0
for i in range(3):
    if a[i]>b[i]:
        counta+=1
    elif a[i]<b[i]:
        countb+=1
print(counta,' ',countb)
