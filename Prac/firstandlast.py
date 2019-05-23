n=int(input("Enter no of elements"))
arr=[]
for i in range(n):
    temp=int(input())
    arr.append(temp)
def sumarr(a,b):
    sum=a+b
    print(sum)
sumarr(arr[0],arr[-1])
