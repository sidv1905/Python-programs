'''cows and bulls'''
import random
x=random.randint(1000,9999)
cow=0
bull=0
x=str(x)
print(x)
n=0
while n!=x:
    n=input()
    for i in range(len(n)):
        if x[i]==n[i]:
            bull+=1
        elif x[i]!=n[i]:
                cow+=1
    print(cow,' are cows', bull, 'are bulls')
    cow=0
    bull=0
print(int(n),'Success same number found')
