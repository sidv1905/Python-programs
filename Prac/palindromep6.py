string = str(input()).lower()
''' [a:b:c] where c denotes the backword direction nad  after c comes a then b'''
if string[::-1] == string:
    print('is palindrome')
else:
    print('is not palindrome')
