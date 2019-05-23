n=int(input("enter number of elements"))
arr=[]
for i in range(n):
    temp=int(input("enter elements"))
    arr.append(temp)
b=[]
for x in arr:
    if x not in b:
        b.append(x)

print(b)
