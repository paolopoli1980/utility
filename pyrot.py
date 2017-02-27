from ase.io import read
from ase.io import write
import math
import os


c=0

def rotation2d(angle):
	for el in atoms:
		if el.symbol!='Au':
			xold=el.position[0]
			yold=el.position[1]
			el.position[0]=xold*math.cos(angle)-yold*math.sin(angle)
			el.position[1]=xold*math.sin(angle)+yold*math.cos(angle)

		
		


def c_m(c):
	
	for el in atoms:
		if el.symbol!='Au':
			if c==0:
				cm=el.position
			c+=1
			if c>0:
				cm=cm+el.position
	cm=cm/(c+1)
	return cm

i=-36

while i<180:
	atoms=[]
	atoms=read('CONTCAR')
	cm=c_m(c)
	i+=36	


	vet=[]
 

	for el in atoms:
		if el.symbol!='Au':
			z=el.position[2]
			el.position=el.position-cm
			el.position[2]=z
		
	for el in atoms:
		if el.symbol!='Au':
			print el

	nameang=str(i)
	angle=i*math.pi/180.0
	rotation2d(angle)
	
	for el in atoms:
		if el.symbol!='Au':
			el.position=el.position+cm
			el.position[2]=19
			

	write('POSCAR',atoms)
	os.system('mkdir rot'+str(nameang))	
	os.system('cp POSCAR rot'+str(nameang))
		


