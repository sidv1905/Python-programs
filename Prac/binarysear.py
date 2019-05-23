'''binary search'''
print(' enter a list in sorted order ')
n=int(input('No. of elements'))
arr=[]
for i in range(n):
    temp=int(input())
    arr.append(temp)
arr.sort()
search=int(input('enter element u want to search'))
start=1
end=n-1
while True:
    mid=(end-start)//2
    if search==arr[mid]:
        print('search element found at',mid)
        break
    elif search>arr[mid]:
        start=mid
    elif search<arr[mid]:
        end=mid
print('yuss')
