import math
import os
import shutil
from ase.io import *
 
import numpy as np
from ase.io import write

norm=np.linalg.norm

a= read('CONTCAR')

n=25
m=24

mo=a[n].mass
mc=a[m].mass

pos=a.get_positions()
posCM = (mc*pos[m]+mo*pos[n])/(mc+mo)
print posCM
 

distvect=pos[n]-pos[m]
print distvect
versor=[]
 
versor=distvect/norm(distvect)
print versor

step=0.02
disteq=1.155
dist=0.8-step
distance=[]
ncicles=14
#dist=1.297
#number_lines = len(fop.readlines())
#print number_lines
#fop.close()
print pos[m],pos[n]


for i in range(ncicles):
	fset=open("setdist","w")
        dist=dist+step
	fset.write(str(dist))
	fset.close()
        pos[m]=(posCM*(mc+mo)-(distvect*(dist/disteq))*mo)/(mc+mo)
	print pos[m]
	pos[n]=pos[m]+distvect*(dist/disteq)
	print pos[n]
	dist=norm(pos[m]-pos[n])
	a.positions=pos
	distance.append(dist)
	os.mkdir('processP'+str(i+1))
	os.system('cp INCAR processP'+str(i+1))
	os.system('cp KPOINTS processP'+str(i+1))
	os.system('cp POTCAR processP'+str(i+1))
	os.system('cp CONTCAR processP'+str(i+1))
        os.system('cp setdist processP'+str(i+1))
	os.system('cp subvaspspec.py processP'+str(i+1))
        os.chdir('processP'+str(i+1))
	write('POSCAR',a)
	os.chdir('..')

print (distance)


#print (xc,yc,zc)


vectRU=[]

#for i in range(12):
	


