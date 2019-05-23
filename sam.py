from itertools import combinations
a=[]
for i in  range (5):
    temp=int(input())
    a.append(temp)

print(list(combinations(a,2)))
