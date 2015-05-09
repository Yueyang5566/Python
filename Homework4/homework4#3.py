from datetime import datetime

import shelve

s=shelve.open("myquotes")
dt1 = datetime.now()
s["flower"]=(0,2,3)
print (s["flower"])
dt2 = datetime.now()
print(dt2.microsecond-dt1.microsecond)


d={}
dt3 = datetime.now()
d["flower"]=(0,2,3)
print (d["flower"])
dt4 = datetime.now()
print(dt4.microsecond-dt3.microsecond)
