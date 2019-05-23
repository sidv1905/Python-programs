a=[]
size=int(input())
for i in range(size):
    temp=int(input("enter element"))
    a.append(temp)
for x in range(size):
    if a[x]>5:
        del a[x]
        size=size-1
print(a)
