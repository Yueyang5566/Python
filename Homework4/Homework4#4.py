import pickle
import shelve
f1=open("pickle.txt", "bw")

Origin={}
Origin["Name"]=("Yueyang")
Origin["Age"]=("23")
Origin["Country"]=("China")
pickle.dump(Origin, f1)
f1.close()


f2=open("pickle.txt", "br")
print(f2.read())
f2.close()


s1=shelve.open("myquotes2")
s1["Origin"]={"Name":"Yueyang","Age":23, "Country":"China"}
print(s1["Origin"])
s1.close()
