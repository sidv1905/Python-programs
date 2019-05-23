t=int(input())
playeri,playerj=0,0
c,c1=0,0
while(t>0):
    Si,Ti = map(int, input().strip().split(' '))
    playeri=playeri+Si
    playerj=playerj+Ti
    if playeri>playerj and playeri-playerj>c:
        c=playeri-playerj

    elif playerj>playeri and playerj-playeri>c1:
        c1=playerj-playeri
    t=t-1;
if c>c1:
    print(1,c)
else:
    print(2,c1)
