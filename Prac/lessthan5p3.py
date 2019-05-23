mylist=[]
n=int(input("Enter size of the list:\n"))

for i in range(0,n):
    temp=int(input("Enter number to append:\n"))
    mylist.append(temp)
newlist=[]
for less in mylist:
    if less<5:
        newlist.append(less)
print(newlist)        
