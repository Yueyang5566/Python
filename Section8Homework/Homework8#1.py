class Animal:       
    def __init__(self,name):
            self.name=name
            if (name=="elephant"):
                    self.info=["I have exceptional memory","I am the largest land-living mammal in the world","I have big ears and long teeth"]
            if (name=="tiger"):
                    self.info=["I am the biggest cat","I come in black and white or orange and black","I am the king of forest"]
            if (name=="bat"):
                    self.info=["I use echo-location","I can fly","I see well in dark"]
    def guess_who_am_i(self):
            flag=0
            print("I will give you 3 hints, guess what animal I am")
            while True:
                    print(self.info[flag])
                    answer=input("Who am I?:")
                    if (answer!=self.name and flag<2):
                            print("Nope, try again!")
                            flag=flag+1
                            
                    elif(answer!=self.name and flag==2):
                            print("I'm out of hints! The answer is:", self.name)
                            break
                    elif(answer==self.name):
                            print("You got it! I am "+self.name)
                            break
e = Animal("elephant")
t = Animal("tiger")
b = Animal("bat")
e.guess_who_am_i()
t.guess_who_am_i()
b.guess_who_am_i()
