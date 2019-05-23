S=input()
sf=''
k=int(input())
for i in S:
    if i.isupper():
        sf += chr(65+(ord(i)+k-65) % 26)
    elif i.islower():
        sf += chr(97+(ord(i)+k-97) % 26)
    elif i.isnumeric():
        sf += str((int(i) + k) % 10)
    else:
        sf += i
print(sf)
