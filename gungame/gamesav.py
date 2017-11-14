import pygame
from pygame.locals import *
from sys import exit
import math
import time
import os


class scenary():

    def __init__(self):
        self.label=0
        self.typeobj=[]
        self.cordobj=[]
        self.dimobj=[]
        



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
            #print string
            while string!="":
                try:
                    string=f1.readline()
                    info=string.split(',')
                    scenario[len(scenario)-1].cordobj.append([float(info[0]),float(info[1])])
                   # print "ola"+str(info[2])
                    scenario[len(scenario)-1].typeobj.append(str(info[2])[0:len(info[2])-1])
                  #  print scenario[len(scenario)-1].typeobj
                    for el in scenario[len(scenario)-1].typeobj:
                        if el=='tree':
                            
                            scenario[len(scenario)-1].dimobj.append([wx,wy])
                except:
                    break
            
#    for el in scenario:
 #       print el.label
  #      print el.cordobj
   #     print el.typeobj
        
        
    

pygame.init()
scenario=[]
size=width, height =400,300
#speed=[1,1]
black=0,0,
wx=20
wy=20
screen=pygame.display.set_mode(size)
background=pygame.image.load("immagine.png").convert()
background = pygame.transform.scale(background, (width, height))
hero=pygame.image.load("hero.jpg").convert()
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
        
    t=0
    for k in range(len(shotherodirection)):
        if shotherodirection[k]=='r':
            shotherocoordinates[k][0]+=10
            print "value",shotherocoordinates[k][0]
 
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
 #               print "ci sono"
                cont=0
                #obj=[]
                for elem in el.typeobj:
  #                  print el.dimobj[cont]
   #                 print shotherodirection[k]
                    if shotherocoordinates[k][0]>el.cordobj[cont][0] and shotherocoordinates[k][0]<el.cordobj[cont][0]+el.dimobj[cont][0] and shotherocoordinates[k][1]>el.cordobj[cont][1] and shotherocoordinates[k][1]<el.cordobj[cont][1]+el.dimobj[cont][1]:
    #                    print "beccato"
                        shotherodirection[k]=''
                        shotherocoordinates[k]=[-1,-1]
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
            print "x"
            cont=-1
            for el in shotherocoordinates:
                cont+=1
                if el==[-1,-1]:
                   # print "ok"
                    shotherocoordinates[cont]=[x+wx/2,y+wy/2]
                    
                    shotherodirection[cont]=oldk
                    print shotherocoordinates[cont]
                    break
    xold=x
    yold=y
    if keys[K_a]:
        x-=5
        oldk='l'
        
#                key='l'
    if keys[K_d]:
        x+=5
        oldk='r'

    if keys[K_w]:
        y-=5
        oldk='up'

    if keys[K_s]:
        y+=5
        oldk='down'

 #               key='d'
    #print x                      
    pygame.display.flip()
    screen.blit(background,(0,0))
    herobullets=[]
    for el in scenario:
        if el.label==schema:
            cont=0
            obj=[]
            for elem in el.typeobj:
                #print elem
                if elem=='tree':
                    obj.append(pygame.image.load("sc"+str(n)+"/tree.png").convert())
  #                  print "-----------",el.dimobj[cont][0],el.dimobj[cont][1]
                    obj[cont]=pygame.transform.scale(obj[cont], (el.dimobj[cont][0],el.dimobj[cont][1]))
 #                   print el.cordobj[cont][0],el.cordobj[cont][1]
                    screen.blit(obj[cont],(float(el.cordobj[cont][0]),float(el.cordobj[cont][1])))
   #                 print elem
                    if x+wx>=float(el.cordobj[cont][0]) and x<=float(el.cordobj[cont][0])+el.dimobj[cont][0] and y+wy>=float(el.cordobj[cont][1]) and y<=float(el.cordobj[cont][1])+el.dimobj[cont][1]:
                        x=xold
                        y=yold
#                        print "x,y",x,y
                    cont+=1
    screen.blit(hero,(x,y))
    for k in range(len(shotherodirection)):
        herobullets.append(pygame.image.load("bullet.png").convert())
        herobullets[k]=pygame.transform.scale(herobullets[k], (2,2))
        bullet_rect =herobullets[k].get_rect()
 
        screen.blit(herobullets[k],(shotherocoordinates[k][0],shotherocoordinates[k][1]))

    pygame.display.update()
            
    time.sleep(0.1)
    

    
           
    
        
