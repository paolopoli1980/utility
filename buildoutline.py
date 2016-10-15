# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 20:35:52 2015

@author: paolo
"""
import pygame
from pygame.locals import *
from sys import exit
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255) 

g=0
GRAY = (g,g,g)

renderingStep = 0.0001


class curve:
    def __init__(self):
        self.listx=[]
        self.listy=[]
        self.curvepointx=[]
        self.curvepointy=[]
        self.size=2
        self.index=0
        self.selfinsbefrend=0
 
 
    def binomialCoeff(self,n, k):
        result = 1
        for i in range(1, k+1):
            result = result * (n-i+1) / i
        return result
    
    def draw_curve(self,npoints,inc):
        t=-inc
        self.curvepointx=[]
        self.curvepointy=[]
        while t<=1:
            t+=inc
            x=0
            y=0
            #print (1-t)**0
            #print self.binomialCoeff(npoints,npoints)
            for j in range(npoints):
                x=x+self.binomialCoeff((npoints-1),j)*self.listx[j]*(1-t)**((npoints-1)-j)*t**j
                y=y+self.binomialCoeff((npoints-1),j)*self.listy[j]*(1-t)**((npoints-1)-j)*t**j
                    
            self.curvepointx.append(x)
            self.curvepointy.append(y)
                
                
            
                
        
def draw_stick_figure(screen, x, y):
    pygame.draw.circle(screen, BLACK, [x, y],5)
     #pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
     

 
pygame.init()
size = [512, 512]
screen = pygame.display.set_mode(size)
surfaceRender = pygame.Surface(screen.get_size() , pygame.SRCALPHA)
surfaceGrayRender = pygame.Surface(screen.get_size() , pygame.SRCALPHA)

myfont = pygame.font.SysFont("monospace", 12)




 
 
pygame.display.set_caption("My Game")
 
done = False
configuration="" 
clock = pygame.time.Clock()
#listobj=[curve()]
listobj=[]
inc=0.05 
keym=0
pygame.mouse.set_visible(0)
numberofcurve=0
cont=-1
keyr=0

while not done:

    for event in pygame.event.get():
      
        if event.type == pygame.QUIT:
            done = True
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        if event.type == KEYDOWN:
 
           tasti_premuti = pygame.key.get_pressed()        

            
           if event.key == K_PAGEUP:
               if (g < 255):
                   g+=5
                   GRAY = (g,g,g)

           if event.key == K_PAGEDOWN:
               if (g >= 5):
                   g-=5
                   GRAY = (g,g,g)

           if event.key == K_KP_MULTIPLY:
               if (renderingStep <= 0.001):
                   renderingStep += 0.0001
                   
           if event.key == K_KP_DIVIDE:
               if (renderingStep >= 0.0002):
                   renderingStep -= 0.0001
           

           if event.key == K_z:
               inc/=2.0
           if event.key == K_x:
               inc*=2.0

           if (event.key == K_r) and (keyr==0):
               keyr=1 
               for el in listobj:
                   el.selfinsbefrend=len(el.curvepointx)
                   
                   #el.draw_curve(len(el.listx),0.0001)                                              
                   el.draw_curve(len(el.listx),renderingStep)                                              
                
           if event.key == K_s:
              
               for elxx in listobj:
                   k=0
                   keyc=0
                   keym=0
                   keyq=0
                   for elt in elxx.curvepointx:
                       #print math.sqrt((x-elt)**2+(y-elxx.curvepointy[k])**2)
                       if math.sqrt((x-elt)**2+(y-elxx.curvepointy[k])**2)<12:
                           elxx.size+=1
                           break 
                       k+=1
           if event.key == K_a:
              
               for elxx in listobj:
                   k=0
                   keyc=0
                   keym=0
                   keyq=0
                   for elt in elxx.curvepointx:
                       #print math.sqrt((x-elt)**2+(y-elxx.curvepointy[k])**2)
                       if (math.sqrt((x-elt)**2+(y-elxx.curvepointy[k])**2)<12) and (elxx.size>0):
                           elxx.size-=1
                           break 
                       k+=1               
           if event.key== K_q:
               
               minimum=100000
               keym=0
               keyc=0
               keyq=1 
               xx=x
               yy=y
               for elxx in listobj:
                   kk=-1
                   for lx in elxx.listx:
                       kk+=1
                       if math.sqrt((x-lx)**2+(y-elxx.listy[kk])**2)<minimum:
                           minimum=math.sqrt((x-lx)**2+(y-elxx.listy[kk])**2)
                           xx=lx
                           yy=elxx.listy[kk]
                           
               listobj[cont].listx.append(xx)
               listobj[cont].listy.append(yy)
               print listobj[cont].listx
                   
           if event.key == K_m:
               p=0
               
               for elxx in listobj:
                   k=0
                   keyc=0
                   keyq=0
                   for elt in elxx.listx:
                       #print math.sqrt((x-elt)**2+(y-elxx.curvepointy[k])**2)
                       if math.sqrt((x-elt)**2+(y-elxx.listy[k])**2)<12:
                           print elxx.index
                           p=elxx.index
                           p2=k
                           keym=1
                           
 

                           break
                       k+=1
                    
                 

           if event.key == K_f:
               f1=open('points.txt','w')
               
               for elxx in listobj:
                   k=0
                   for elt in elxx.curvepointx:
                       f1.write(str(elxx.curvepointx[k])+"\n")
                       f1.write(str(elxx.curvepointy[k])+"\n")
                       k+=1
               f1.write("*\n")        
               f1.close()        
           if event.key == K_d:
 
               for elxx in listobj:
                   k=0
                   keyc=0
                   keym=0
                   keyq=0
                   for elt in elxx.curvepointx:
                       print math.sqrt((x-elt)**2+(y-elxx.curvepointy[k])**2)
                       if math.sqrt((x-elt)**2+(y-elxx.curvepointy[k])**2)<12:
                           elxx.curvepointx=[]
                           elxx.curvepointy=[]
                           elxx.listx=[]
                           elxx.listy=[]
                           #curveDeleted = elxx
                           #listobj.remove(curveDeleted)
                           #cont-=1
                           break
                       k+=1
              
               
               

           if event.key == K_e:
               for el in listobj:
                   print el.listx
                   print el.listy
                   

           if event.key == K_c:
               cont+=1  
               segno=0
               if cont>0:
                   if len(listobj[cont-1].listx)==0:    
                       cont-=1
                       segno=1
               if segno==0:        
                   listobj.append(curve())
               print "curve!!"
               configuration="curve"
               keyc=1
               keyq=0
               keym=0
               if cont>0:
                   listobj[cont-1].draw_curve(len(listobj[cont-1].listx),inc)
                   listobj[cont-1].index=cont-1


        if event.type==pygame.MOUSEMOTION and keym==1:
               if cont>0:
                   print "p"+str(p)
                   listobj[p].curvepointx=[]
                   listobj[p].curvepointy=[]
 
                   listobj[p].listx[p2]=x
                   listobj[p].listy[p2]=y
 
                   
                   listobj[p].draw_curve(len(listobj[p].listx),inc)
                    
            
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
             
             keym=0
             if configuration=="curve":
                 if keyc==1 or keyq==1:
                     listobj[cont].listx.append(x)
                     listobj[cont].listy.append(y)
 
                 
                 print x,y
                 
             
        screen.fill(WHITE)

        label = myfont.render("Mum curves: " + str(len(listobj)), 1, BLACK)
        incValue = myfont.render("Inc value: " + str(inc), 1, BLACK)
        grayValue = myfont.render("Gray value: " + str(g), 1, BLACK)
        rendStepValue = myfont.render("Rendering step value: " + str(renderingStep), 1, BLACK)
        screen.blit(label, (10, 400))
        screen.blit(incValue, (10, 420))
        screen.blit(grayValue, (10, 440))
        screen.blit(rendStepValue, (10, 460))
     
        c=-1
        for el in listobj:
            c+=1
            c2=0
            for elx in listobj[c].listx:
                #pygame.draw.ellipse(screen, BLACK, [1 + listobj[c].listx[c2], listobj[c].listy[c2], 10, 10], 0)
                pygame.draw.circle(screen, BLACK, [listobj[c].listx[c2], listobj[c].listy[c2]],5)
                    
                c2+=1
            c2=0    
            for elx in listobj[c].curvepointx:
                    
               # pygame.draw.ellipse(screen, BLUE, [1 + listobj[c].curvepointx[c2], listobj[c].curvepointy[c2]+2,listobj[c].size , listobj[c].size/2], 0)
                if c2>0:
                    #pygame.draw.aaline()        
                    if keyr==0:    
                        #pygame.draw.line(screen, GRAY, (listobj[c].curvepointx[c2-1]+5,listobj[c].curvepointy[c2-1]+5), (listobj[c].curvepointx[c2]+5,listobj[c].curvepointy[c2]+5),int(listobj[c].size))
                        pygame.draw.line(screen, GRAY, (listobj[c].curvepointx[c2-1],listobj[c].curvepointy[c2-1]), (listobj[c].curvepointx[c2],listobj[c].curvepointy[c2]),int(listobj[c].size))
                    if keyr==1:    
                        #pygame.draw.line(surfaceRender, (0, 255, 0), (listobj[c].curvepointx[c2-1]+5,listobj[c].curvepointy[c2-1]+5), (listobj[c].curvepointx[c2]+5,listobj[c].curvepointy[c2]+5),int(listobj[c].size))
                        #pygame.draw.line(surfaceGrayRender, GRAY, (listobj[c].curvepointx[c2-1]+5,listobj[c].curvepointy[c2-1]+5), (listobj[c].curvepointx[c2]+5,listobj[c].curvepointy[c2]+5),int(listobj[c].size))                       

                        #pygame.draw.circle(surfaceRender, (0, 255, 0), (int(listobj[c].curvepointx[c2-1]+5),int(listobj[c].curvepointy[c2-1]+5)),int(listobj[c].size/2))
                        #pygame.draw.circle(surfaceGrayRender, GRAY,(int(listobj[c].curvepointx[c2-1]+5),int(listobj[c].curvepointy[c2-1]+5)),int(listobj[c].size/2))    
                        
                        pygame.draw.circle(surfaceRender, (0, 255, 0), (int(listobj[c].curvepointx[c2-1]),int(listobj[c].curvepointy[c2-1])),int(listobj[c].size/2))
                        pygame.draw.circle(surfaceGrayRender, GRAY,(int(listobj[c].curvepointx[c2-1]),int(listobj[c].curvepointy[c2-1])),int(listobj[c].size/2))                       

                c2+=1   
                             
        if keyr==1:            
            pygame.image.save(surfaceRender,'roadsTexture.png')
            pygame.image.save(surfaceGrayRender,'roadsHeight.png')
            keyr=0
            
            
            for el in listobj:
                listax=[el.curvepointx[0]]
                listay=[el.curvepointy[0]]

                for t in range(len(el.curvepointx)):
                    if t%100==0:
                        listax.append(el.curvepointx[t])
                        listay.append(el.curvepointy[t])
                el.curvepointx=[]
                el.curvepointy=[]
                el.curvepointx[:]=listax[:]
                el.curvepointy[:]=listay[:]
                
                 
                
        draw_stick_figure(screen, x, y)
 
        pygame.display.flip()
        clock.tick(100)
 
pygame.quit()