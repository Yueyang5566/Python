from random import randrange
print("INTEGER DIVISIONS (input 'quit' to end the learning game!)")
d=1
while True:
    if(d=="quit"):
        break
    try:
        a=randrange(12)
        b=randrange(1,4)
        print(a,"/",b)  
        c=(a//b)     # a division by b  =  c
        d=input("=")
        d=int(d)
        if (d==c):
            print("CORRECT!")
        elif (d!=c):
            print("INCORRECT!")
    except ValueError:
        print("Please enter Integers Only!")
    #except ZeroDivisionError:
    #    print("Error, division by zero!")
