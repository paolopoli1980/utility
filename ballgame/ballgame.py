from __future__ import division
from visual import * 
from datetime import datetime
from datetime import timedelta
import math 

 

class player:

    def __init__(self,vector,direction):
        self.pos=vector
        self.direction=direction
riga=[]
life_list=[1,1,1,1,1,1,1]
listposx=[-3,-3,-3,-3,-3,-3,-2]
listposy=[3,3,3,7,4,3,3]
npar=[100,100,100,100,100,100,100]

def costruisci_schema(nschema,lenght,large):
    global maxx
    global maxy
    global stringa
    global riga
    maxx=0
    maxy=0
    f1=open("muri"+str(nschema)+".txt","r")
    cont=-1
    stringa="xx"
    while stringa!='*\n':
        cont+=1
        cont2=-1
        stringa=f1.readline()
        for el in stringa:
            cont2+=1
            if el=="1":
                wall[cont][cont2]=1
                muro.append(box(pos=(cont+cellx/2,cont2+celly/2,0), length=cellx, height=celly, width=1,color=color.blue))
                if cont>maxx:
                    maxx=cont
                if cont2>maxy:
                    maxy=cont2
 
    stringa=f1.readline()
    
    riga=stringa[0:len(stringa)-1].split(",")
    
    f1.close()
   
 
    
    

scene = display(title='The ball game',
     x=0, y=0, width=600, height=600,
     center=(0,0,0), background=(0,0,0))
muro=[]
obj=[]        
p1=player((-3,3,0),(1,0,0)) 

obj.append(pyramid(pos=p1.pos, size=(1,1,0),axis=p1.direction))
win=1
nschema=0
while win>0:
        
 
    for el in muro:
        el.visible=false
         
         

    muro=[]    
    large=20
    lenght=20
    cellx=1   #obbligatoriamente 1
    celly=1
    
    nschema+=1
    push='off'
 
        
    win=1
    print push
    wall=[[0 for j in range(lenght)]for i in range(large)] 
    print wall
    costruisci_schema(nschema,lenght,large)

    for k in range(npar[nschema-1]):
        if win==2:
            break

        win=0    
        ok=1
        ball=sphere(pos=(-3,3,0),radius=0.1,color=color.red)
        ball2=sphere(pos=(float(riga[0]),float(riga[1]),float(riga[2])),radius=0.1,color=color.yellow)
        x=listposx[nschema-1]
        y=listposy[nschema-1]
        assex=1
        assey=0
        teta=0
        vx=0
        vy=0
        ball.pos=p1.pos
        ball.pos.x+=1
        t=0
        dt=0.01
        push=""
        t2=0
        conta2=0
        xx=0
        yy=0
        
        while ok==1:
                 
                 
            rate(1000)
            p1.direction=(assex,assey,0)        
            p1.pos=(x,y,0)
            obj[0].pos=p1.pos
            obj[0].axis=p1.direction

            if push=='on':
                print 'on'
                ball.pos.x=ball.pos.x+vx*dt
                ball.pos.y=ball.pos.y+vy*dt
                if mag(ball.pos-ball2.pos)<0.2:
                    print "hai vinto"
                    win=2
                    ball2.color=color.black
                    ball.visible=false
                    break
            indexx=int(ball.pos.x)
            indexy=int(ball.pos.y)

            if ball.pos.x>0 and ball.pos.y>0:
                print "alt"
                             
                if (wall[indexx][indexy]==1):
                    #print "merda"
                    mindist=10000
                    for i in range(large):
                        for j in range(lenght):
                            dist=math.sqrt((ball.pos.x-i)**2+(ball.pos.y-j)**2)
                            if dist<mindist:
                                mindist=dist
                                xx=i
                                yy=j
                            dist=math.sqrt((ball.pos.x-(i+1))**2+(ball.pos.y-j)**2)
                            if dist<mindist:
                                mindist=dist
                                xx=i+1
                                yy=j
                            dist=math.sqrt((ball.pos.x-i)**2+(ball.pos.y-(j+1))**2)
                            if dist<mindist:
                                mindist=dist
                                xx=i
                                yy=j+1
        
                            dist=math.sqrt((ball.pos.x-(i+1))**2+(ball.pos.y-(j+1))**2)
                            if dist<mindist:
                                mindist=dist
                                xx=i+1
                                yy=j+1
                                
        
                    if abs(ball.pos.x-xx)>=abs(ball.pos.y-yy) and (vy!=0):
                        vy=-vy
                        t=0
                        
                    else:
                        vx=-vx
                        t=0
                        
            
 
            key='x'
            if push!='on':

                if scene.kb.keys:
                    key = scene.kb.getkey()
                
  
                    if (key=='up') and (key!='c'):
                        teta+=0.05
                        assex=math.cos(teta)
                        assey=math.sin(teta)
                    
                    if (key=='down') and (key!='c'):
                        teta-=0.05
                        assex=math.cos(teta)
                        assey=math.sin(teta)
                    if key=='c' and push!='on':
                        vx=ball.pos.x - p1.pos[0]
                        vy=ball.pos.y - p1.pos[1]
                        #print vx
                        t=0
                        push="on"
                    key='x'              
                
                
        
          
            if push!='on':
                ball.pos=p1.pos        
                ball.pos.x+=assex
                ball.pos.y+=assey
          
            if ball.pos.x>maxx+1.1 or ball.pos.y>maxy+1.1 or ball.pos.x<-4 or ball.pos.y<0:
                ball.visible=false    
     
                ok=0
                     
            
 