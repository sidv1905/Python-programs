#reverse of an number
N=int(input('enter'))
mylist=[]
for i in range(0,N):
	n=input()
	mylist.append(temp)
for reverse in mylist:
	rev=0
	while(n>0):
    		dig=n%10
    		rev=rev*10+dig
    		n=n/10
	print(rev)
