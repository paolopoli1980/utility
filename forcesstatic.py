from ase.io import *
from ase.io import write
import math
from pylab import *
a=read('OUTCAR')
f1=open('OUTCAR','r')
f2=open('CONTCAR','r')

stringa="*"
st=''
memstr=[]
memfreeatoms=[]
def readconstrained():
    startreadingline=9
    stringa="*"
    for j in range(startreadingline):
        f2.readline()
        
    for i in range(len(a.numbers)-1) :

        stringa=f2.readline()
        line=stringa.split()
       # print line[3]
        if (line[3]=='T' and line[4]=='T' and line[5]=='T'):
            memfreeatoms.append(i+1)
            
def reading():
    
    f1.readline()
    for i in range(len(a.numbers)) :
        st=f1.readline()
        memstr.append(st[0:len(st)-1])
        
    
maxlist=[]	
metric=0
maxlistx=[]
maxlisty=[]
maxlistz=[]

readconstrained()
print memfreeatoms
while stringa!="":
    stringa=f1.readline()
	#print stringa[1:6]
    memstr=[]
    maxim=0
    mx=0
    my=0
    mz=0
    
    
    if stringa[1:5]=='POSI':
         reading()
         cont=0
         for el in memstr:
             cont+=1
             
             keystr=el.split()
             metric=math.sqrt(float(keystr[3])**2+float(keystr[4])**2+float(keystr[5])**2)
             ok=0
             for elem in memfreeatoms:
                 
                 if elem==cont:
                     ok=1
             if ((metric>maxim) and (ok==1)):
                 maxim=metric
                 mx=float(keystr[3])                                        
                 my=float(keystr[4])                                        
                 mz=float(keystr[5])                                        
                     
             #print keystr[3]
         maxlist.append(maxim)    
         maxlistx.append(mx)    
         maxlisty.append(my)    
         maxlistz.append(mz)    
         
    #     pass
print maxlist
plot(maxlist)
plot(maxlistx)
plot(maxlisty)
plot(maxlistz)

show()
f1.close()
