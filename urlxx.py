# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 10:07:41 2015

@author: paolo
"""

import urllib

    
        
#key=raw_input("key=")    
key=["description","jobLocation"]
stringa=[]
i=0    
npage=5
sock=""
sock = urllib.urlopen("http://www.indeed.co.uk/Python-Programmer-jobs")
    
stringa.append(sock.readlines())

while i<10*npage:
    i+=10
    sock = urllib.urlopen("http://www.indeed.co.uk/jobs?q=Python+Programmer&start="+str(i))
    stringa.append(sock.readlines())
    

c=0
id=0
for k in range(npage):
    for el in stringa[c]:
        if id==1:
            print el
        id=0    
     
        for i in range(len(el)):
     
               
                if (el[i:i+len(key[0])]==key[0]):
                    
                    id=1
                if (el[i:i+len(key[1])]==key[1]):
                    
                    print el

    c+=1           
        
    print("PAGE NUMBER"+str(k*10))
    
  

 
