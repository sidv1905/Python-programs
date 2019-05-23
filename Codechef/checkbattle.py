T=int(input())
while T>0:
    N=input()
    N=N.lower()
    if N=='b':
        print('BattleShip')
    elif N=='c':
        print('Cruiser')
    elif N=='d':
        print('Destroyer')
    elif N=='f':
        print('Frigate')
    T=T-1
