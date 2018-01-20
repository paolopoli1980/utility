import pygame
from pygame.locals import *
from sys import exit
import math
import time
import os
import random

class scenary():

    def __init__(self):
        self.label=0
        self.typeobj=[]
        self.cordobj=[]
        self.dimobj=[]
        self.shotting=[]
        for i in range(10):
            self.shotting.append([[-1,-1] for j in range(10)])
        self.typeshotting=[]

        for i in range(10):
            self.typeshotting.append([[-1,-1] for j in range(10)])
        self.lifeenemy=[]


def charge_scenary(n):
    x=os.listdir('sc'+str(n))
    
    for files in x:
        print files
        file_extension=files.split(".")
        print file_extension[1]
        if file_extension[1]=="sch":
            scenario.append(scenary())
            scenario[len(scenario)-1].label=file_extension[0]
            f1=open("sc"+str(n)+"/"+str(files))
            string="x"
            while string!="":
                try:
                    string=f1.readline()
                    info=string.split(',')
                    scenario[len(scenario)-1].cordobj.append([float(info[0]),float(info[1])])
                    scenario[len(scenario)-1].typeobj.append(str(info[2])[0:len(info[2])-1])
                    cont=0
                    cont2=0
                    cc=0
                    
                    
  
                except:
                    break
            for el in scenario[len(scenario)-1].typeobj:
                cc+=1
                liscopy=[]
                liscopy=scenario[len(scenario)-1].cordobj[:]
                if el=='tree':
                    
                    scenario[len(scenario)-1].dimobj.append([wx,wy])
                if el=='e1':
                    scenario[len(scenario)-1].dimobj.append([wx,wy])
                    scenario[len(scenario)-1].lifeenemy.append(1)
                    print scenario[len(scenario)-1].lifeenemy 
                    for i in range(5):
                        val1=scenario[len(scenario)-1].cordobj[cont][0]
                        val2=scenario[len(scenario)-1].cordobj[cont][1]
                        
                        scenario[len(scenario)-1].shotting[cont2][i][0]=val1
                        scenario[len(scenario)-1].shotting[cont2][i][1]=val2
            
                        vers1=random.randint(-4,4)
                        vers2=random.randint(-4,4)
                        if vers1==0:
                            vers1=1
                        if vers2==0:
                            vers2=1
                            

                        scenario[len(scenario)-1].typeshotting[cont2][i]=[vers1,vers2]
                    cont2+=1     
                cont+=1        

    print cc                    
    for el in scenario:
        print el.typeobj
        print el.lifeenemy
        
    

pygame.init()
scenario=[]
size=width, height =640,480
#speed=[1,1]
black=0,0,
wx=20
wy=20
screen=pygame.display.set_mode(size)
background=pygame.image.load("immagine.png").convert()
background = pygame.transform.scale(background, (width, height))
hero=pygame.image.load("hero.png").convert()
hero = pygame.transform.scale(hero, (wx, wy))
x=0
y=0
#hero_rect = hero.get_rect()
#hero_rect.width=10
#hero_rect.height=10
shotherocoordinates=[]
shotherodirection=[]
herobullets=[]
endscen=0
n=1
charge_scenary(n)
schema='1111'
numb=0
obj=[]

while endscen==0:
    
 #    pygame.display.update()
                    
            
    #background cicle
    #shot cicle
    #monster cicle
    if x>=width:
        numb=int(schema)
        numb=numb+1000
        x=0
        schema=str(numb)
    if x<0:
        numb=int(schema)
        numb=numb-1000
        x=width-1
        schema=str(numb)

    if y>=height:
        numb=int(schema)
        numb=numb+100
        y=0
        schema=str(numb)
        print schema
    if y<0:
        numb=int(schema)
        numb=numb-100
        y=height-1
        schema=str(numb)
        print schema
        
        
    t=0
    for k in range(len(shotherodirection)):
        if shotherodirection[k]=='r':
            shotherocoordinates[k][0]+=10
 
        if shotherodirection[k]=='l':
            shotherocoordinates[k][0]-=10
        if shotherodirection[k]=='up':
            shotherocoordinates[k][1]-=10
        if shotherodirection[k]=='down':
            shotherocoordinates[k][1]+=10
        if shotherocoordinates[k][0]<1 or shotherocoordinates[k][0]>width-1:
            shotherodirection[k]=''
            shotherocoordinates[k]=[-1,-1]
            
        if shotherocoordinates[k][1]<1 or shotherocoordinates[k][1]>height-1:
            shotherodirection[k]=''
            shotherocoordinates[k]=[-1,-1]

    for k in range(len(shotherodirection)):
        
        for el in scenario:
            if el.label==schema:
                cont=0
                cont2=-1
                for elem in el.typeobj:
                    if elem=="e1":
                        cont2+=1
                    if shotherocoordinates[k][0]>el.cordobj[cont][0] and shotherocoordinates[k][0]<el.cordobj[cont][0]+el.dimobj[cont][0] and shotherocoordinates[k][1]>el.cordobj[cont][1] and shotherocoordinates[k][1]<el.cordobj[cont][1]+el.dimobj[cont][1]:
                        shotherodirection[k]=''
                        shotherocoordinates[k]=[-1,-1]
                        if elem=="e1":#sbagliato
                            el.lifeenemy[cont2]-=1
                            #cont2+=1
             #               print el.lifeenemy
                            
                    cont+=1     
                        
                        
            
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        pygame.quit()
    if keys[K_m]:
        if len(shotherodirection)<5:
            shotherocoordinates.append([x+wx/2,y+wy/2])
            shotherodirection.append(oldk)
        if len(shotherodirection)==5:
            cont=-1
            for el in shotherocoordinates:
                cont+=1
                if el==[-1,-1]:
                    shotherocoordinates[cont]=[x+wx/2,y+wy/2]
                    
                    shotherodirection[cont]=oldk
                    break
    xold=x
    yold=y
    if keys[K_a]:
        x-=5
        oldk='l'
        
    if keys[K_d]:
        x+=5
        oldk='r'

    if keys[K_w]:
        y-=5
        oldk='up'

    if keys[K_s]:
        y+=5
        oldk='down'

    pygame.display.flip()
    screen.blit(background,(0,0))
    herobullets=[]
    enemybullets=[]
    cont3=-1
    for el in scenario:
        if el.label==schema:
            cont=-1
            obj=[]
            cont3=-1
            for elem in el.typeobj:
                if elem=='tree':
                    cont+=1
                if elem=='tree':
                    obj.append(pygame.image.load("sc"+str(n)+"/tree.png").convert())
                    obj[cont]=pygame.transform.scale(obj[cont], (el.dimobj[cont][0],el.dimobj[cont][1]))
                    screen.blit(obj[cont],(float(el.cordobj[cont][0]),float(el.cordobj[cont][1])))
                    if x+wx>=float(el.cordobj[cont][0]) and x<=float(el.cordobj[cont][0])+el.dimobj[cont][0] and y+wy>=float(el.cordobj[cont][1]) and y<=float(el.cordobj[cont][1])+el.dimobj[cont][1]:
                        x=xold
                        y=yold
                if elem=='e1':
                    cont3+=1
                    cont+=1
                    obj.append(pygame.image.load("sc"+str(n)+"/e1.png").convert())


                if elem=='e1' and el.lifeenemy[cont3]>0:
                    obj[cont]=pygame.transform.scale(obj[cont], (el.dimobj[cont][0],el.dimobj[cont][1]))
                    screen.blit(obj[cont],(float(el.cordobj[cont][0]),float(el.cordobj[cont][1])))
                    if x+wx>=float(el.cordobj[cont][0]) and x<=float(el.cordobj[cont][0])+el.dimobj[cont][0] and y+wy>=float(el.cordobj[cont][1]) and y<=float(el.cordobj[cont][1])+el.dimobj[cont][1]:
                        x=xold
                        y=yold
                elif elem=='e1' and el.lifeenemy[cont3]<=0:
                    el.cordobj[cont][0]=-1
                    el.cordobj[cont][1]=-1
                    
                

            cont2=-1
            cont3=-1
            cont4=-1
            for elem in el.typeobj:
                cont3+=1
                if elem=="e1":
                    cont4+=1
                    cont2+=1
                    
                if elem=="e1" and el.lifeenemy[cont4]>0:
                   
#                   if el.lifeenemy[cont2]>0:
                   
                   for t in range(5):
                       if el.shotting[cont2][t][0]>0 and el.shotting[cont2][t][0]<width and el.shotting[cont2][t][1]>0 and el.shotting[cont2][t][1]<height:
                             el.shotting[cont2][t][0]+=el.typeshotting[cont2][t][0]
                             el.shotting[cont2][t][1]+=el.typeshotting[cont2][t][1]
                             
     #                           el.cordobj[cont3][0]-=1
                             enemybullets.append(pygame.image.load("bullete1.png").convert())
                             enemybullets[len(enemybullets)-1]=pygame.transform.scale(enemybullets[len(enemybullets)-1], (2,2))
                                #bullet_rect =herobullets[k].get_rect()
                         
                             screen.blit(enemybullets[len(enemybullets)-1],(el.shotting[cont2][t][0],el.shotting[cont2][t][1]))
                       else:
                           el.shotting[cont2][t][0]=el.cordobj[cont3][0]
                           el.shotting[cont2][t][1]=el.cordobj[cont3][1]
                           
                   #cont2+=1
                   
    #cont+=1                     

    screen.blit(hero,(x,y))
    for k in range(len(shotherodirection)):
        herobullets.append(pygame.image.load("bullet.png").convert())
        herobullets[k]=pygame.transform.scale(herobullets[k], (2,2))
        bullet_rect =herobullets[k].get_rect()
 
        screen.blit(herobullets[k],(shotherocoordinates[k][0],shotherocoordinates[k][1]))
                             
    pygame.display.update()
            
    time.sleep(0.1)
    

    
           
    
        
