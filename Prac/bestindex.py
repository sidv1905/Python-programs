
def miniMaxSum(arr):
    arr.sort()
    minimum=sum(arr[0:4])
    maximum=sum(arr[1:5])
    return minimum,maximum


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
