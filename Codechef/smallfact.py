t=int(input())
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
arr=[]
factarr=[]
i=0
while i<t:
    temp=int(input())
    arr.append(temp)
    factarr.append(factorial(arr[i]))
    i+=1
for fact in factarr:
    print(fact)
