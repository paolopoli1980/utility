# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:50:49 2015

@author: Alessandro Zanetti and Paolo Poli
"""
from __future__ import division
from vpython import * 
from datetime import datetime
from datetime import timedelta
import math



scene = canvas(title='Rotation',
     x=0, y=0, width=800, height=620,
     center=vec(10,10,0), background=vec(0,1,1)) 

#scene.autoscale=True
#scene.fillswindow=True
scene.autocenter=True
scene.range=25


class Diamond:
    def __init__(self):
        self.Pos= vec(0,0,0)
        self.Rot= vec(0,0,0)
        self.Model = cylinder(pos=vec(self.Pos), axis=vec(0,0,1), radius=0.5,color=color.magenta, opacity =0.5)
    
    def Update(self,gameTime):
        self.Model.pos=self.Pos
        
        

class Bullet:

    def __init__(self,pos,direction,velocity):
        self.Pos=pos
        self.Fire=sphere(pos=vec(self.Pos),radius=0.1,color=color.yellow)
        self.Direction=direction
        self.Velocity=velocity
        self.Cell=[0,0]

    def Update(self):
        self.Pos+=self.Direction*self.Velocity
        self.Fire.pos=self.Pos
        self.Cell=[math.trunc((self.Pos.x+cube.lato/2) / cube.lato),math.trunc((self.Pos.y+cube.lato/2) / cube.lato)]
        
    
            
        

class Player:
    
    def changeposfromcell(self,XY):
        self.PosX=XY[0]*cube.lato+cube.lato/2
        self.PosY=XY[1]*cube.lato+cube.lato/2
        self.getCell()        

        self.modelPlayer = pyramid(pos=vec(self.PosX,self.PosY,self.PosZ), size=vec(1,1,1),axis=vec(0.1,0,0),color=self.Colore)
        
        
    def __init__(self,tastileft,tastiright,tastiup,tastidown,fire,bonusVel,invis,colore):
        self.PosX = 0
        self.PosY = 0
        self.PosZ = 0
        self.RotX = 0
        self.RotY = 0
        self.RotZ = 0
        self.Velocity = 0.05
        self.vx=0
        self.vy=0
        self.vz=0    
        self.Left=tastileft
        self.Right=tastiright
        self.Up=tastiup
        self.Down=tastidown
        self.Fire=fire
        self.BonusVel=bonusVel
        self.Invis= invis
        self.Colore=colore
        self.Cell=[]
        self.newcella=[]
        self.Bullets=[]        
        self.direction=vec(1,0,0)
        self.Lives =3
        
        self.DeltaFire = timedelta(seconds = 0.5)
        self.DataLastFire = datetime.now()
                 
        self.CountBonusVelocity = 3           
        self.PercBonusVelocity = 0
        self.DeltaTimeVelocity = timedelta(seconds = 2)
        self.DataLastBonusVelocity = datetime.now()
        self.DataCancelBonusVelocity= datetime.now()
        self.DeltaTimeCancelBonusVelocity= timedelta(seconds = 3)
        

        self.CountBonusInvis = 3          
        self.DeltaTimeInvis = timedelta(seconds = 3)
        self.DataLastInvis = datetime.now()
        self.DataCancelInvis= datetime.now()        
        self.DeltaTimeCancelInvis= timedelta(seconds = 3)
        
        self.CanFire=True        
        
        self.getCell()        
        self.modelPlayer = pyramid(pos=vec(self.PosX,self.PosY,self.PosZ), size=vec(1,1,1),axis=vec(0.1,0,0),color=self.Colore)
        self.ShipLabel = label(pos= vec(self.modelPlayer.pos), text= str(self.Lives)) 
        #self.Rotazione = Vector3(0,0,0)        
        
    def Update(self,key,walls,gameTime):
        
        self.RotZ=0    
        self.ShipLabel.pos = self.modelPlayer.pos
        self.ShipLabel.text = str(self.Lives)
                    
        dataCancVel=self.DataLastBonusVelocity+self.DeltaTimeCancelBonusVelocity
        if (gameTime > dataCancVel):
            self.PercBonusVelocity =0
        dataCancInvis=self.DataLastInvis+self.DeltaTimeCancelInvis
        if (gameTime > dataCancInvis):
            self.modelPlayer.opacity = 1
            self.ShipLabel.visible=1
            self.CanFire=True
            
        for elem in key:
            if elem==self.Fire:               
                diffdate= datetime.today() - self.DataLastFire
                if ((diffdate > self.DeltaFire) and (self.CanFire==True) ):                
                    self.Bullets.append(Bullet(pos=vec(self.PosX,self.PosY,self.PosZ),direction=vec(self.direction),velocity=0.2))
                    self.DataLastFire= datetime.today()
                    break
            if elem == self.Invis:
                diffdate= datetime.today() - self.DataLastInvis
                if ((diffdate > self.DeltaTimeInvis) and (self.CountBonusInvis >0)): 
                    self.modelPlayer.opacity=0.1
                    self.CanFire=False
                    self.ShipLabel.visible=0
                    self.CountBonusInvis -=1
                    self.DataLastInvis = datetime.today()
                break
            if elem == self.BonusVel:
                diffdate= datetime.today() - self.DataLastBonusVelocity
                if ((diffdate > self.DeltaTimeVelocity) and (self.CountBonusVelocity >0)): 
                    self.PercBonusVelocity = 0.06
                    self.CountBonusVelocity -=1
                    self.DataLastBonusVelocity = datetime.today()
                break    
            if elem==self.Down:
                self.RotY =0.75*2*math.pi
                if self.premoving(walls) == True:
                    self.moving()
                    self.direction=vec(0,-1,0)
                                        
                break
     
            if elem==self.Up:
                self.RotY = 0.25*2*math.pi
                if self.premoving(walls) == True:
                    self.moving()
                    self.direction=vec(0,1,0)                    

                break
         
            if elem==self.Left:
                self.RotY = 0.5*2*math.pi
                if self.premoving(walls) == True:
                    self.moving()
                    self.direction=vec(-1,0,0)                    

                break
     
            if elem==self.Right:
                self.RotY = 0
                if self.premoving(walls) == True:
                    self.moving()
                    self.direction=vec(1,0,0)                    

                break


    def premoving(self,muri):
        prePosX= self.PosX + self.vx * (self.Velocity + self.PercBonusVelocity)
        prePosY= self.PosY + self.vy * (self.Velocity + self.PercBonusVelocity)
        prePosZ= self.PosZ + self.vz * (self.Velocity + self.PercBonusVelocity)
        self.vx=math.cos(self.RotZ)*math.cos(self.RotY)*1
        self.vy=math.cos(self.RotZ)*math.sin(self.RotY)*1
        self.vz=0
  
        self.modelPlayer.axis=vector(self.vx,self.vy,self.vz)

        self.newcella=self.getCellfromposition(prePosX,prePosY)
        #print (self.newcella)
         
        check=0        
        
        for elx in muri:
             if ((self.newcella[0]==elx.Cell[0]) and (self.newcella[1]==elx.Cell[1])):
                 check=1
                 break
        if check == 0:
            
            return True
        #print (check)
        return False
                 

    def moving(self):
        #print (str(self.Cell) + str("*"))
        self.PosX += self.vx* (self.Velocity + self.PercBonusVelocity)
        self.PosY += self.vy* (self.Velocity + self.PercBonusVelocity)
        self.PosZ += self.vz* (self.Velocity + self.PercBonusVelocity)
 
            ##print self.vx
            
        self.vx=math.cos(self.RotZ)*math.cos(self.RotY)*1
        self.vy=math.cos(self.RotZ)*math.sin(self.RotY)*1
        self.vz=0
  
        self.modelPlayer.axis=vec(self.vx,self.vy,self.vz)
        
        self.modelPlayer.pos=vec(self.PosX,self.PosY,self.PosZ)
        
        self.getCell()
        #if key=='c':
    def getCellfromposition(self,x,y):
        Cella=[math.trunc((x+cube.lato/2) / cube.lato),math.trunc((y+cube.lato/2) / cube.lato)]
        return Cella
        
    def getCell(self):
        self.Cell=[math.trunc((self.PosX+cube.lato/2) / cube.lato),math.trunc((self.PosY+cube.lato/2) / cube.lato)]
 
        return  self.Cell
             
    def crash(self,obj):
        self.cu=obj
        check=0
        if len(self.newcella)>0:
              
            for elx in self.cu:
                if ((self.newcella[0]==elx.Cell[0]) and (self.newcella[1]==elx.Cell[1])):
                    check=1 
                    break
            if check==0:
                self.moving()
                
class cube:
     
     lato=0
     
     #def __init__(self,lenght,large,tickness,x,y,z):
     def __init__(self,x,y,z):
         #self.Lenght=lato#lenght
        # self.Large=lato#large
         #self.Tickness=lato#tickness
         self.X=x
         self.Y=y
         self.Z=z
         self.Cell = [0,0]
     
         
         
         
     
cube.lato = 2
         
 
player1=Player('left','right','up','down','.','-','l',color.red)
player2=Player('a','d','w','s','1','2','3',color.green)
#xy=[1,1]
#player1.changeposfromcell(xy)
#xy=[2,2]
#player2.changeposfromcell(xy)
listaPlayers=[]
listaPlayers.append(player1)
listaPlayers.append(player2)
 
lista=[]
f1=open("map.txt","r")

filetxt=f1.readlines()
listvalue=[]
lenght=len(filetxt)
large=len(filetxt[0])

mapWidth= large * cube.lato
mapHeight = lenght * cube.lato

matrixgame=[[0 for j in range(lenght)]for i in range(large)] 
row=0
column=0
wall=[]
#lato=2 
    
for el in filetxt:
    for let in el:
        if let!="\n":
            matrixgame[row][column]=let
            if let == "1":
                cubo=cube(row*cube.lato,column*cube.lato,0)
                cubo.Cell=[row,column]
                wall.append(cubo)
            if let =="A":
                player1.changeposfromcell([row,column])
            if let =="B":
                player2.changeposfromcell([row,column])   
        column+=1
    column=0    
    row+=1
    
 
plane=box (pos = vec(cube.lato*lenght/2-cube.lato/2,cube.lato*large/2-cube.lato/2,-cube.lato/2), length=cube.lato*lenght, height=cube.lato*large, width=0.1,color=vec(0,0,255))    
for cubo in wall:
    Cubo=box (pos = vec(cubo.X,cubo.Y,0), length=cube.lato, height=cube.lato, width=cube.lato,color=vec(100,100,0))
 
diamante= Diamond()
diamante.Pos= vector(5,5,0)

def handleKeyUp( evt ):
    
    cont=-1
    for el in lista:
        cont+=1
        if el==evt.key:
            del lista[cont]
  
     
def handleKeyDown( evt ):
 
    ok=1
    for el in lista:
        if el==evt.key:
            ok=0
    if ok==1:
        lista.append(evt.key)
#    #print lista

scene.bind('keydown', handleKeyDown)
scene.bind('keyup', handleKeyUp)            


 
GameTime=datetime.today()

while 1==1:    
    rate(100)
    GameTime= datetime.today()    
    
    diamante.Update(GameTime)

    for play in listaPlayers:
        play.Update(lista,wall,GameTime)
        ##print lista
        for el in play.Bullets:
            el.Update()
    #player1.Update(lista,wall)
    #player2.Update(lista,wall)
    
    #for el in player1.Bullets:
    #    el.Update()
    
    for el in player1.Bullets:
        pl = vector(player2.PosX,player2.PosY,player2.PosZ)
        ris = mag(pl - el.Pos)        
        if (ris<=0.8):        
            del player1.Bullets[player1.Bullets.index(el)] 
            el.Fire.visible=0
            player2.Lives-=1
            
                
                
            #del listaPlayers[listaPlayers.index(player2)]
           # #print "distrutti"            
            #player2.visible=0
            
    
    for el in player2.Bullets:
        pl = vector(player1.PosX,player1.PosY,player1.PosZ)
        ris = mag(pl - el.Pos)        
        if (ris<=0.8):        
            del player2.Bullets[player2.Bullets.index(el)] 
            el.Fire.visible=0
            player1.Lives-=1


    for elex in wall:
        for el in player1.Bullets:
            if (elex.Cell[0]==el.Cell[0]) and (elex.Cell[1]==el.Cell[1]):
                del player1.Bullets[player1.Bullets.index(el)] 
                el.Fire.visible=0
                
    for elex in wall:
        for el in player2.Bullets:
            if (elex.Cell[0]==el.Cell[0]) and (elex.Cell[1]==el.Cell[1]):
                del player2.Bullets[player2.Bullets.index(el)] 
                el.Fire.visible=0
            
        
    
        #    #print player1.Bullets
    #player1.crash(wall)
    
    #player2.crash(wall)        
     
#    #print player1.Cell 
#    sfera.pos=(player1.PosX,player1.PosY,player1.PosZ)
    
          
    
    
 
 

    

