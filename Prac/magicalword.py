T=int(input())
while T>0:
    N=int(input())
    S=input()
    S=S.upper()
    sf=''
    def check_prime(a):
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    def find_next_prime(n):
        low = n - 1
        high = n + 1
        while True:
            if check_prime(low):
                return low
            elif check_prime(high):
                return high
            else:
                low -= 1
                high += 1
    for check in S:
        if check_prime(ord(check)):
            sf=sf+check
        else:
            nextone=find_next_prime(ord(check))
            nextone=chr(next)
            sf=sf+nextone
    print(sf)
