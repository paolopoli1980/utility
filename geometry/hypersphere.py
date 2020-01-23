######################################################################################
#Hypersphere and Hyperparaboloide
######################################################################################
#We measure an hypersphere and hyperparabolide using a statistic method,
#(Montecarlo principle), where the n dimensional object is put into a n dimensional
#cuboid. The excercise pays attention on the precision of the method in function of the
#number of points used, and about the volume variation, in function of the dimensions number
#of an unitary sphere. The mathematics idea is throw a certain number of points and to count
#how many points are inside respect the number of total points. The volume is measured with
#npoints_into*(Volume_chosen)/totalpoints.
######################################################################################

import numpy as np
import matplotlib.pyplot as plt

volume=[]
dimension=[]

def hypersphere():
    r=1
    for dim in range(2,10):
        npoints=800000
        ncountinto=0

        for j in range(npoints):
            distance=0
            s = np.random.uniform(-r,r,dim)
           # print (s)
            for i in s:
                distance+=i**2
            if distance<=r**2:
                ncountinto+=1
        v=(2*r)**dim*ncountinto/npoints    
        volume.append(v)
        dimension.append(dim)        
    plt.plot(dimension,volume,'ro')
    plt.show()

def paraboloide():
    for dim in range(2,10):
        npoints=800000
        ncountinto=0

        for j in range(npoints):
            distance=0
            s = np.random.uniform(0,2,dim)
           # print (s)
            for i in range(len(s)-1):
                
                distance+=(i-1)**2
            if distance>=s[-1]:
                ncountinto+=1
        v=2**dim*ncountinto/npoints    
        volume.append(v)
        dimension.append(dim)        
    plt.plot(dimension,volume,'ro')
    plt.show()
hypersphere()
#paraboloide()
