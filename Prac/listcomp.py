mylist=[]
n=int(input("size of list"))
for i in range(0,n):
    temp=int(input("enter list values"))
    mylist.append(temp)

print(mylist)

mylist2=[]
mylist2.append(list(even for even in mylist if even%2==0))
print(mylist2)
