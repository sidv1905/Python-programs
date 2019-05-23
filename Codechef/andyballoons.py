n=int(input())
S=[]
x=y=z=0
while x>=0:
    while y>=0:
        while z>=0:
            if (x+y+z)==n:
                f=[x,y,z]
                for i in range(len(S)):
                    if f[0]!=S[i][0]:
                        if f[1]!=S[i][1]:
                            if f[2]!=S[i][2]:
                                S.append(f)
            z+=1
        y+=1
    x+=1
h=len(S)
print(h)
for i in range(h):
    print(S[i])
