name=input("Hi, what is your name?")
print("Hello "+name+"  let's play a game!")
print("Think of random number from 1 to 100, and I'll try to guess it!")
i=1
a=0
b=101
x=50
flag=True                                   
playgame="yes"                       #Set the playgame = "yes",to run the program!
while(flag==True):                                    
    if (playgame=="yes"):            #playgame = "yes", will run the program!                               
        while(flag==True):
            isequal=input("Is it "+str(x)+"?(yes/no):")
            if (isequal=="yes"):     #if number is the one, congratulation!
                print("Yeey! I got it in "+str(i)+" tries!")
                i=1                  #after the first game, set the number to original!
                x=50
                break
            elif (isequal=="no"):    #if number is not the one, find it by guess!
                islarger=input("Is the number larger than "+str(x)+"?(yes/no)")                                   
                if(islarger=="yes"): #if the one you think larger than number,do the following!
                    i=i+1
                    a=x
                    x=(a+b)//2               
                elif(islarger=="no"):#if the one you think less than number, do the following!
                    i=i+1
                    b=x
                    x=(a+b)//2              
    elif(playgame=="no"):            #playgame = "no", will jump out the loop!                                
        print("Bye-bye!")
        break
    playgame=input("Do you want to play more?(yes/no)")
