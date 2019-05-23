mylist=[]
n=int(input("Enter size of the list 1:\n"))

for i in range(0,n):
    temp=int(input("Enter number to append:\n"))
    mylist.append(temp)
mylist2=[]
x=int(input("Enter size of the list 2:\n"))

for i in range(0,x):
    temp2=int(input("Enter number to append:\n"))
    mylist2.append(temp2)
c=[]
for m in mylist:
    if m in mylist2:
        c.append(m)
print(c)        
