def count_frequency(mylist):               #define the function
    i=0
    d={}                                   #create a empty 
    for i in range(len(mylist)):
        keyword=mylist[i]                  #keyword in the mylist
        value = mylist.count(keyword)      #value related to keyword
        i=i+1
        if (keyword not in d):
            d.update({keyword:value})      #add element to the dictionary
    return d
mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))
    





