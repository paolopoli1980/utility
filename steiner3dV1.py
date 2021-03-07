import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

class point:
    def __init__(self,x,y,z,pointype):

        self.x=x
        self.y=y
        self.z=z
        self.pointype=pointype
        
    
        
def extremescalculation():
    xmax=(max(el.x for el in points))
    xmin=(min(el.x for el in points))
    ymax=(max(el.y for el in points))
    ymin=(min(el.y for el in points))
    zmax=(max(el.z for el in points))
    zmin=(min(el.z for el in points))
    return [[xmax,ymax,zmax],[xmin,ymin,zmin]]
  


                          
def gridconstructor(distx,disty,distz):
    ix=distx/(grid[0]+1)
    iy=disty/(grid[1]+1)
    iz=distz/(grid[2]+1)
    for k in range(grid[2]):
        for j in range(grid[1]):
            for i in range(grid[0]):
                gridvector.append([pmin[0]+ix*(i+1),pmin[1]+iy*(j+1),pmin[2]+iz*(k+1)])

    
    

def minspanningcalc(dimpoints,listindexcouple):
    

    global somma    
    
    distances=[]
   
    distancesindex=[]
    #print(dimpoints)
    for i in range(dimpoints):
        
        for j in range(dimpoints):
            
            connectionmatrix[i][j]=np.sqrt((points[i].x-points[j].x)**2+(points[i].y-points[j].y)**2+(points[i].z-points[j].z)**2)
            
    minval=100000000000
    listmemindex=[0]
    somma=0
    listminval=[]
    
    #print (connectionmatrix)
   
   
    
    while len(listmemindex)<dimpoints:
        minval=1000000000
        switch='off'
        for el in listmemindex:
            #print (el)
            for j in range(dimpoints):
                #print(minval)
                check=True
                for elem in listmemindex:
                    #print ('elem',elem)
                    if elem==j:
                           
                        check=False               
                if (connectionmatrix[el][j]>0) and check==True:
                    if minval>connectionmatrix[el][j]:
                        switch='on'
                        #print ('minval',minval)   
                        minval=connectionmatrix[el][j]
                        memindex=j
                        indexcouple=(el,j)
                        
       
        if switch=='on':
            listmemindex.append(memindex)
            listindexcouple.append(indexcouple)
            
            
            somma+=minval
            listminval.append(minval)
            

            


def steinerongrid(nsteinerpoints,listindexcouple):
    global memsomma
    mempoints=[]
    npointsongrid=grid[0]*grid[1]*grid[2]
    niter=np.math.factorial(npointsongrid)/(np.math.factorial(nsteinerpoints)*np.math.factorial(npointsongrid-nsteinerpoints))
    niter=int(niter)
    virtualpos=[0 for i in range(len(gridvector))]
    print (niter)
    mempoints=[[0 for i in range(3)] for i in range(len(points))]
        
    for i in range(nsteinerpoints):
        virtualpos[i]=1

    count=nsteinerpoints-1
    memsomma=10000000000000000000
    memtrack=virtualpos.copy()
    while 1==1:
        contcheck=0

        
        listindexcouple=[]

        contpointer=len(points)-nsteinerpoints
        for j in range(len(virtualpos)):
            if virtualpos[j]==1:
            
                
                points[contpointer].x=gridvector[j][0]
                points[contpointer].y=gridvector[j][1]
                points[contpointer].z=gridvector[j][2]
                contpointer+=1
        listindexcouple=[]            
        dimpoints=len(points)    
       
        minspanningcalc(dimpoints,listindexcouple)

      
        if memsomma>somma:
           print(memsomma) 
           memsomma=somma
           memtrack=virtualpos.copy()
           memlistcouple=listindexcouple.copy()
          
           print ('memlistiinfuction',memlistcouple)
           print (memtrack)
           i=0    
           for el in points:
               print ('points in procedure',el.x,el.y,el.z)
               mempoints[i]=[el.x,el.y,el.z] 
               i+=1
                     
        for i in range(len(virtualpos)-nsteinerpoints,len(virtualpos)):
            if virtualpos[i]==1:
                contcheck+=1
        if contcheck==nsteinerpoints:
            break            
                
        while virtualpos[-1]==0:
            virtualpos[count]=0
            if count<len(virtualpos)-1:
                virtualpos[count+1]=1
                count+=1
                listindexcouple=[]
                
                contpointer=len(points)-nsteinerpoints
                for j in range(len(virtualpos)):
                    if virtualpos[j]==1:
                    
                        
                        points[contpointer].x=gridvector[j][0]
                        points[contpointer].y=gridvector[j][1]
                        points[contpointer].z=gridvector[j][2]
                        contpointer+=1  
                    


 
                minspanningcalc(dimpoints,listindexcouple)
            dimpoints=len(points)    
                                        

           
            if memsomma>somma:
               print(memsomma) 
               memsomma=somma
               memtrack=virtualpos.copy()
               memlistcouple=listindexcouple.copy()
              
                   
               print ('memlistinfunction',memlistcouple)
               print (memtrack)
               i=0 
               for el in points:
                   print ('points in procedure',el.x,el.y,el.z)
                   
                   mempoints[i]=[el.x,el.y,el.z] 
                   i+=1     

               
        if nsteinerpoints>1:       
           
            count=len(virtualpos)-1
            contone=0
            
            while virtualpos[count]!=0:
                
                contone+=1
                count-=1
            while virtualpos[count]!=1:
                count-=1
            virtualpos[count]=0
            virtualpos[count+1]=1
            memposone=[]
            for j in range(contone):
                virtualpos[j+count+2]=1
                memposone.append(j+count+2)
                zero=True
                for el in memposone:
                    if el==len(virtualpos)-1-j:
                        zero=False
                if zero==True:
                    virtualpos[len(virtualpos)-1-j]=0
                memcount=j+count+2
            count=memcount    
           
    print (memsomma)
    print (listindexcouple)
    i=0
    for el in points:
        el.x=mempoints[i][0]
        el.y=mempoints[i][1]
        el.z=mempoints[i][2]
        i+=1
        
                    
    return memlistcouple
        

def plotspanningtree(listindexcouple):
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")
    x=[]
    y=[]
    z=[]
    for el in points:
        x.append(el.x)
        y.append(el.y)
        z.append(el.z)
    ax.scatter3D(x, y, z, color = "green")
    v1=[x[0],y[0],z[0]]
    v2=[x[1],y[1],z[1]]
    #print (v1,v2)
    xs=[]
    ys=[]
    zs=[]
    xe=[]
    ye=[]
    ze=[]
    for el in listindexcouple:
        xs.append(points[el[0]].x)
        ys.append(points[el[0]].y)
        zs.append(points[el[0]].z)
        xe.append(points[el[1]].x)
        ye.append(points[el[1]].y)
        ze.append(points[el[1]].z)
                  
    for i in range(len(listindexcouple)):    
        ax.plot([xs[i],xe[i]],[ys[i],ye[i]],[zs[i],ze[i]])
    plt.title("simple 3D scatter plot")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    
    plt.show()

#points=[point(6,4,2,'city'),point(5,7,1,'city'),point(2,3,3,'city'),point(1,4,3,'city'),point(5,1,2,'city'),point(1.5,5.25,2.4,'city'),point(3,5.25,2.4,'city'),point(4.5,5.25,2.4,'city')]
#points=[point(3,2,1,'city'),point(5,1,1,'city'),point(2,3,3,'city'),point(1,2,1,'city'),point(2,1,2,'city'),point(1.5, 5.25, 2.4,'city'), point(3.5, 4.25, 1.4,'city'), point(1.25, 3.9375, 2.4,'city'), point(2.5, 3.9375, 2.4,'city'), point(3.75, 3.9375, 2.4,'city')]
points=[point(0,0,0,'city'),point(2,0,0,'city'),point(4,0,0,'city'),point(0,2,0,'city'),point(2,2,0,'city'),point(4,2,0,'city')]
#points=[point(0,2,0,'city'),point(0,0,0,'city'),point(3,2,2,'city'),point(4,0,2,'city')]
#listaccia=[0, 0, 0], [2, 0, 0], [4, 0, 0], [0, 2, 0], [2, 2, 0], [4, 2, 0], [1.7142857142857142, 0.5714285714285714, 0.0], [0.5714285714285714, 0.8571428571428571, 0.0], [3.4285714285714284, 1.1428571428571428, 0.0], [2.2857142857142856, 1.4285714285714284, 0.0]
grid=[6,6,1]
#points=[]
#for i in range(len(listaccia)):
#    points.append(point(listaccia[i][0],listaccia[i][1],listaccia[i][2],'city'))
#matrixgrid=np.zeros((grid[0],grid[1],grid[2]))
gridvector=[]
dimpoints=len(points)
mempoints=[]
nsteinerpoints=4
for i in range(nsteinerpoints):
    points.append(point(0,0,0,'steiner'))
print(dimpoints)
connectionmatrix=np.zeros((dimpoints,dimpoints))
pmax=extremescalculation()[0]
pmin=extremescalculation()[1]
print (pmax,pmin)
print (gridvector)

distx=pmax[0]-pmin[0]
disty=pmax[1]-pmin[1]
distz=pmax[2]-pmin[2]
listindexcouple=[]
memtrack=[]
print(distx,disty,distz)    
gridconstructor(distx,disty,distz)
minspanningcalc(dimpoints,listindexcouple)


print (gridvector)
plotspanningtree(listindexcouple)

print ('somma spanning tree',somma)
sommaspanning=somma
print (listindexcouple)
dimpoints=len(points)
connectionmatrix=np.zeros((dimpoints,dimpoints))
memlistcouple=[]

memlistcouple=steinerongrid(nsteinerpoints,listindexcouple).copy()


lisindexcouple=[]
listindexcouple=memlistcouple.copy()

minspanningcalc(dimpoints,memlistcouple)
print(listindexcouple)


print (memlistcouple)
print ('somma spanning tree',sommaspanning)
print ('somma steiner',memsomma,dimpoints)
listposagents=[]
for el in points:
    listposagents.append([el.x,el.y,el.z])
print (listposagents)

points=[]
listindexcouple=[]
i=0
for el in listposagents:
    i+=1
    if i<=dimpoints-nsteinerpoints:
        points.append(point(el[0],el[1],el[2],'city'))
    else:
        points.append(point(el[0],el[1],el[2],'steiner'))

for el in points:
    print(el.pointype)
dimpoints=len(points)    
minspanningcalc(dimpoints,listindexcouple)
    
plotspanningtree(listindexcouple)
