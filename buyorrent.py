# -*- coding: utf-8 -*-
"""
Created on Sat May 27 09:02:26 2017

@author: paolo
"""
import matplotlib.pyplot as plt
years=20.0
homecost=140000
loanpermonth=27000/(years*12)
sellhome=130000
rentcost=450
feecostrent=100
feecostlet=100
notaiocost=15000
crashcost=8000
month=0
nmonth=340
listvalues=[]
yearslist=[]

print loanpermonth
print (sellhome-homecost-notaiocost)
ok=0
for i in range(nmonth):
    renttot=rentcost*i+feecostrent*i
    tothomesell=(sellhome-homecost-notaiocost-crashcost)-loanpermonth*i-feecostlet*i
    listvalues.append(tothomesell+renttot)
    yearslist.append(i/12.0)
    
    if tothomesell+renttot>=0 and ok==0:
        print i
        print i/12.0
        ok=1
plt.plot(yearslist,listvalues)
    
plt.show()