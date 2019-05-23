import random
while(True):
    a=random.randint(1,9)
    user_input=input("Guess the number : ")
    count+=1
    user_input=int(user_input)
    a=int(a)
    if user_input>a:
        print("higher")
    elif user_input<a:
        print("lower")
    elif user_input==a:
        print("EQUAL")
        countr+=1
    print("it was",a)
