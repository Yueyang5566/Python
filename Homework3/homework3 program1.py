def bunnyEars2(n):                          #define the function
    if (n<=0):                              #if n<=0, return value 0
        return 0
    elif (n>=1):
        if (n%2!=0):                        #if n is odd, add 2
            return bunnyEars2(n-1)+2
        else:                               #if n is even, add 3
            return bunnyEars2(n-1)+3

print ("bunnyEars2(0):",bunnyEars2(0))
print ("bunnyEars2(1):",bunnyEars2(1))
print ("bunnyEars2(2):",bunnyEars2(2))
