# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 15:38:01 2015

@author: paolo
"""

from visual import *
import ase
import math



class atom():
	def __init__(self,tipology,vec):
		self.radius=0
		self.color=''
		self.pos=vec
		self.tipology=tipology


	def setradiuscolor(self,tipology):

		if tipology=='O':
			self.color=color.red
			self.radius=0.66
		if tipology=='H':
			self.radius=0.3
			self.color=color.white
		if tipology=='N':
			self.radius=0.7
			self.color=color.blue
		if tipology=='Cu':
			self.radius=1.28
			self.color=color.orange	
		if tipology=='C':
			self.radius=0.77
			self.color=color.green
		if tipology=='Ru':
			self.radius=1.33
			self.color=color.blue
		if tipology=='Co':
			self.radius=1.49
			self.color=color.red
		if tipology=='Au':
			self.radius=1.44
			self.color=color.yellow
		if tipology=='Ag':
			self.radius=1.44
			self.color=color.white

	

 
			
		
def convert_fil(namefile):
	from ase.io import read
 	from ase.io import write
	slab=read(namefile)
	write('x.xyz', slab)
	
	

def atomselect(ev):
	for el in listobj:
		
		distance=math.sqrt((float(ev.pos.x)-float(el.pos[0]))**2+(float(ev.pos.y)-float(el.pos[1]))**2+((float(ev.pos.z)-float(el.pos[2]))**2)) 	
		#print distance
		if distance<el.radius:
			el.color=color.red
 			print el.tipology
def readfiles():
	f1=open(name_file ,"r")
	dati=f1.readlines()
        stringa=dati[2].split("      ")
	c=0
        for el in dati:
		c+=1
		if c>2:
			#print el
			dati=el.split("     ")
			 
			#print dati[0], dati[1], dati[2] , dati[3]
			vec=[dati[1],dati[2],dati[3]]
					
			#print vec
						
			listobj.append(atom(dati[0],vec))
 	for el in listobj:
		el.setradiuscolor(el.tipology)

		
def mindist():
    distance=sys.maxint
    el1=0
    el2=0
    c=0
    c2=0
    for el in listobj:
        c+=1
        c2=0
        for elx in listobj:
            c2+=1
            if (math.sqrt((float(el.pos[0])-float(elx.pos[0]))**2+(float(el.pos[1])-float(elx.pos[1]))**2+(float(el.pos[2])-float(elx.pos[2]))**2)!=0) and (math.sqrt((float(el.pos[0])-float(elx.pos[0]))**2+(float(el.pos[1])-float(elx.pos[1]))**2+(float(el.pos[2])-float(elx.pos[2])**2)<distance)):
                distance=math.sqrt((float(el.pos[0])-float(elx.pos[0]))**2+(float(el.pos[1])-float(elx.pos[1]))**2+(float(el.pos[2])-float(elx.pos[2]))**2)
                el1=c
                el2=c2
    print distance
    print el1,el2
    
                
def select():
    k=-1
    while 1==1:
        rate(400)    
        if scene.kb.keys:
            s=scene.kb.getkey()
            print s
            if s=="f":
                print k
                if k>-1:
                    ball[k].color=colorold
                k+=1
                colorold=ball[k].color
                ball[k].color=color.magenta
                print ball[k].pos
            if s=="b":
                print k
                if k>-1:
                                        
                    ball[k].color=colorold
                    k-=1
                    colorold=ball[k].color
                    ball[k].color=color.magenta
                    print ball[k].pos
            if s=="e":
                break
                
                
                 
        if k==len(listobj)-1:
            break
        
                 
                 
def expand(ball):
    
    c=0
    listemp=[]
    listemp[:]=listobj[:]
    listx=[]
    vec=[]
    for el in listemp:
        print veccell
        vec=[float(el.pos[0])+float(veccell[0]),float(el.pos[1])+float(veccell[1]),float(el.pos[2])+float(veccell[2])]
        print vec
        listobj.append(atom(el.tipology,vec))
        listx.append(atom(el.tipology,vec))
 
        c+=1
     
    for el in listobj:
        el.setradiuscolor(el.tipology)
    for el in listx:
        el.setradiuscolor(el.tipology)
        
    print listx
    
    for el in listx:
        c+=1
        print el.tipology
        print el.pos[0]
        ball.append(sphere(pos=(float(el.pos[0]),float(el.pos[1]),float(el.pos[2])), radius=el.radius, color=el.color))
        
 
name_file=raw_input("Insert name of the file=")
convert_file=raw_input("Do you want to convert the file in xyz format?=")
#name_file='cartesian.xyz'

listobj=[]
if convert_file=='y':
	convert_fil(name_file)
	name_file='x.xyz'
ball=[]
readfiles()

c=-1
for el in listobj:
    c+=1
    print el.tipology
    print el.pos[0]
    ball.append(sphere(pos=(float(el.pos[0]),float(el.pos[1]),float(el.pos[2])), radius=el.radius, color=el.color))

while 1==1:

      rate(100)  

      if scene.kb.keys:
          
          s=scene.kb.getkey()  
          if s=="c":
              veccell=[0,0,0]  
              command=raw_input("insert command=")
              if command=="expand":
                  string=raw_input("insert vector1 of the cells")
                  veccell=string.split()
                  print veccell

                  expand(ball)
                  s=""
              if command=="minimaldistance":
                  mindist()
              if command=="select":
                  select()
              

 