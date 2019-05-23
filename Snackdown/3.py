T=int(input())
combinations = []
def makeNumber(number, digits, path = []):
    if digits == 1:                   # base case when only 1 digit to play with
        if number not in path:        # to stop duplications
            path += [number]        
            path.sort()
            if number < 10 and path not in combinations:
                combinations.append(path)

    else:
        nums = list(range(1, min(number - digits + 2, 10)))
        nums = list(set(nums).difference(path))

        for i in nums:
            makeNumber(number - i, digits - 1, path + [i])



while T>0:
    latestarr=[]
    N,K=map(int , input().split())
    if N==1 or K>=N:
        print(-1)
        continue
    product=1
    combinations=makeNumber(N,K)
    print(combinations)
    for check in combinations:
        for check1 in check:
            thisone=(check1*check1)-check1
            product=product*thisone
        latestarr.append(product)
        product=1
    m = 1000000007
    print (max(latestarr)%m)
    T-=1
