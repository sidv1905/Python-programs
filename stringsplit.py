T=int(input())
while T>0:
    S=input()
    newstring=''
    newchar=''
    newno=''
    validLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    validno='0123456789'
    for char in S:
         if char in validLetters:
             newstring+=char
         elif char in validno:
             newno+=char
         else:
             newchar+=char
    print(newstring)
    print(newno)
    print(newchar)
    T=T-1
