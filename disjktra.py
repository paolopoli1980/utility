# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:50:04 2013

@author: Paolo
"""
#VERSIONE GIUSTA

#This is an implementation of the Disjktra alghoritm

import numpy as np
from random import randint


nnodi=6    #set the number of the nodes

matrixdist = np.zeros(shape=(nnodi,nnodi))    
matrixpot= np.zeros(shape=(nnodi,nnodi))
identificator=np.zeros(shape=(nnodi,1))


k=1000000000000
casual=0
mj=0
mt=0

#you can create a random graphs using this subrouitine

def randompath(matrixdist,matrixpot,nnodi):
	for i in range(nnodi):
		for j in range(i+1,nnodi):
			casual=randint(1,9)
			connect=randint(0,1)
			if (connect==1):
				matrixdist[i][j]=casual
				matrixdist[j][i]=casual
				matrixpot[i][j]=k
				matrixpot[j][i]=k



#you set the nodes connections

#matrixdist=[[0,2,0,0,8,0,0],[2,0,6,2,0,0,0],[0,6,0,0,0,0,5],[0,2,0,0,2,9,0],[8,0,0,2,0,3,0],[0,0,0,9,3,0,1],[0,0,5,0,0,1,0]]
#matrixpot=[[0,k,0,0,k,0,0],[k,0,k,k,0,0,0],[0,k,0,0,0,0,k],[0,k,0,0,k,k,0],[k,0,0,k,0,k,0],[0,0,0,k,k,0,k],[0,0,k,0,0,k,0]]
#matrixdist=[[0,7,9,0,14,0],[7,0,10,15,0,0],[9,10,0,11,2,0],[0,15,11,0,0,6],[14,0,2,0,0,9],[0,0,0,6,9,0]]
#matrixpot=[[0,k,k,0,k,0],[k,0,k,k,0,0],[k,k,0,k,k,0],[0,k,k,0,0,k],[k,0,k,0,0,k],[0,0,0,k,k,0]]
#matrixdist=[[0,1,2,0,6,0],[1,0,0,1,3,0],[2,0,0,2,0,0],[0,1,2,0,1,0],[6,3,0,1,0,1],[0,0,0,0,1,0]]
#matrixpot=[[0,k,k,0,k,0],[k,0,0,k,k,0],[k,0,0,k,0,0],[0,k,k,0,k,0],[k,k,0,k,0,k],[0,0,0,0,k,0]]
matrixdist=[[0,4,2,0,0,0],[4,0,1,5,0,0],[2,1,0,8,10,0],[0,5,8,0,2,6],[0,0,10,2,0,3],[0,0,0,6,3,0]]
matrixpot=[[0,k,k,0,0,0],[k,0,k,k,0,0],[k,k,0,k,k,0],[0,k,k,0,k,k],[0,0,k,k,0,k],[0,0,0,k,k,0]]

matrixdist=[[0,8,2,5,0,0,0,0],[8,0,0,2,0,13,0,0],[2,0,0,2,5,0,0,0],[5,2,2,0,1,6,3,0],[0,0,5,1,0,0,1,0],[0,13,0,6,0,0,2,3],[0,0,0,3,1,2,0,6],[0,0,0,0,0,3,6,0]]
matrixpot= [[0,k,k,k,0,0,0,0],[k,0,0,k,0,k,0,0],[k,0,0,k,k,0,0,0],[k,k,k,0,k,k,k,0],[0,0,k,k,0,0,k,0],[0,k,0,k,0,0,k,k],[0,0,0,k,k,k,0,k],[0,0,0,0,0,k,k,0]]

#matrixdist=[[0,6,3,18,0,0,0],[6,0,0,11,5,0,0],[3,0,0,20,0,10,0],[18,11,20,0,13,1,17],[0,5,0,13,0,0,9],[0,0,10,1,0,0,14],[0,0,0,17,9,14,0]]
#matrixpot= [[0,k,k,k,0,0,0],[k,0,0,k,k,0,0],[k,0,0,k,0,k,0],[k,k,k,0,k,k,k],[0,k,0,k,0,0,k],[0,0,k,k,0,0,k],[0,0,0,k,k,k,0]]

#matrixdist=[[0,3,5,6,0,0,0],[3,0,0,2,0,0,0],[5,0,0,2,6,3,7],[6,2,2,0,0,9,0],[0,0,6,0,0,5,2],[0,0,3,9,5,0,1],[0,0,7,0,2,1,0]]
#matrixpot= [[0,k,k,k,0,0,0],[k,0,0,k,0,0,0],[k,0,0,k,k,k,k],[k,k,k,0,0,k,0],[0,0,k,0,0,k,k],[0,0,k,k,k,0,k],[0,0,k,0,k,k,0]]

#matrixdist=[[0,4,3,0,7,0,0],[4,0,6,5,0,0,0],[3,6,0,11,8,0,0],[0,5,11,0,3,10,2],[7,0,8,3,0,5,0],[0,0,0,10,5,0,3],[0,0,0,2,0,3,0]]
#matrixpot= [[0,k,k,0,k,0,0],[k,0,k,k,0,0,0],[k,k,0,k,k,0,0],[0,k,k,0,k,k,k],[k,0,k,k,0,k,0],[0,0,0,k,k,0,k],[0,0,0,k,0,k,0]]

matrixdist=[[0,10,25,0,0,0],[10,0,35,20,15,0],[25,35,0,0,35,0],[0,20,0,0,40,30],[0,15,35,40,0,20],[0,0,0,30,20,0]]
matrixpot= [[0,k,k,0,0,0],[k,0,k,k,k,0],[k,k,0,0,k,0],[0,k,0,0,k,k],[0,k,k,k,0,k],[0,0,0,k,k,0]]

matrixdist=[[0,1,2,0,0,0],[1,0,1,1,2,0],[2,1,0,0,1,0],[0,1,0,0,1,1],[0,1,2,1,0,1],[0,0,0,1,1,0]]
matrixpot= [[0,k,k,0,0,0],[k,0,k,k,k,0],[k,k,0,0,k,0],[0,k,0,0,k,k],[0,k,k,k,0,k],[0,0,0,k,k,0]]
#randompath(matrixdist,matrixpot,nnodi)
print matrixdist
nodoinit=0
listmem=[]
listseg=[]
identificator[nodoinit][0]=1
somma=0
memnodo=0
print(matrixpot[2][1])
ok='true'
while ok=='true':
    ok='false'
    for i in range(nnodi):
 
        if ((matrixpot[i][nodoinit]>0) and (identificator[i][0]<1) and (matrixpot[i][nodoinit]>matrixdist[i][nodoinit]+somma)):
            matrixpot[i][nodoinit]=matrixdist[i][nodoinit]+somma
            matrixpot[nodoinit][i]=matrixdist[nodoinit][i]+somma

 
            print '%s and %s and %s and %s and %s' %(nodoinit,i,somma,mj,mt)
        minn=k
	memnodo=nodoinit            
    for j in range(nnodi):
        for t in range(nnodi):
             if (matrixpot[j][t]==k):
                 ok='true'
	    
	     			
             if (((matrixpot[j][t]<=minn) ) and (matrixpot[j][t]>0) and (identificator[t][0]<1)):
                 minn=matrixpot[j][t]
                 nodoinit=t  
                 somma=minn
		 mj=j
		 mt=t

    if (matrixdist[memnodo][nodoinit]!=0):
	listseg.append('-')
    else:
	listseg.append('x')	
    identificator[nodoinit][0]=1
 	
    print matrixpot	 
    print "\n"	
    	
    listmem.append(nodoinit+1);	
    
    print(matrixpot)    
 
	
print listmem
print listseg
listmem=[nnodi]
jmem=nnodi-1
imem=0
while (jmem!=0): 
	min=1000
	 
	jmemold=jmem
	print(jmem)
	print(matrixpot[jmem])
	for j in range(nnodi):
		if ((matrixpot[jmem][j]<=min) and (matrixpot[jmem][j]>0) and (j!=jmemold) ):
			min=matrixpot[jmem][j]
			imem=j
 
	jmem=imem
	listmem.append(jmem+1)
print listmem
	

		
#print matrixpot[2][3]