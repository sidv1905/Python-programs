x=int(input("Enter a number "))
mylist=[]
n=int(x)
for i in range(1,n):
    if x%i==0:
        mylist.append(i)
print(mylist)
