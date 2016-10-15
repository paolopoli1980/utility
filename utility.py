import glob
import os, os.path
import ase
from ase.io import read
from ase.io import write
from ase import Atoms
from ase.constraints import FixAtoms
from ase.constraints import FixCartesian


def help():
	print ("find  -  to find a file")
	print ("del   -  to delete a file")
	print ("fixallatoms - to fix atoms in vasp file")
	print ("makecartesianposcar - to change the file chosen in xyz file")
	print ("constcoord - to put the coordinate at the same value")

def constcoord():
        path=raw_input("insert path with name files =")
        cord=raw_input("wich does coordinate you want to change? = ")
 	value=input("Insert value");		
	print path
	try:
		f2=open(path,"r")
		f3=open("NEWPOSCAR","w")
		
		stringa="*"
		while (stringa!='Cartesian\n') and (stringa!='Direct\n'):
			stringa=f2.readline()
			f3.write(stringa)
			print stringa
         	f3.write(stringa)
		while stringa!="":
			print("ok")
			if cord=='x':
				stringa=f2.readline()
				stringa2=stringa.split()
		   		stringa2[0]=value
				stringa3=""			
				for el in stringa2:
					stringa3=stringa3+str(" ")+str(el)
				f3.write(str(stringa3)+str("\n"))
				
		
			if cord=='y':
				stringa=f2.readline()
				stringa2=stringa.split()
		   		stringa2[1]=value
				stringa3=""			
				for el in stringa2:
					stringa3=stringa3+str(" ")+str(el)
				f3.write(str(stringa3)+str("\n"))
				

			if cord=='z':
				stringa=f2.readline()
				stringa2=stringa.split()
		   		stringa2[2]=value
				stringa3=""			
				for el in stringa2:
					stringa3=stringa3+str(" ")+str(el)
				f3.write(str(stringa3)+str("\n"))

			if stringa=='':
				print("operation was done")
				break
		
	except:
		print("Is not possible to open this file")

	print("NEWPOSCAR was created")
	f2.close()
	f3.close()

	
def fixallatoms():
        path=raw_input("insert path with name files =")
	cord=raw_input("wich does coordinate you want to fix? = ")
 
	print path
	try:
		f2=open(path,"r")
		f3=open("NEWPOSCAR","w")
		
		stringa="*"
		while (stringa!='Cartesian\n') and (stringa!='Direct\n'):
			stringa=f2.readline()
			f3.write(stringa)
			print stringa
         	f3.write(stringa)
		while stringa!="":
			print("ok")
			if cord=='x':
				stringa=f2.readline()
				stringa2=stringa.split()
		   		stringa2[3]='F'
				stringa3=""			
				for el in stringa2:
					stringa3=stringa3+str(" ")+str(el)
				f3.write(str(stringa3)+str("\n"))
				
		
			if cord=='y':
				stringa=f2.readline()
				stringa2=stringa.split()
		   		stringa2[4]='F'
				stringa3=""			
				for el in stringa2:
					stringa3=stringa3+str(" ")+str(el)
				f3.write(str(stringa3)+str("\n"))
				

			if cord=='z':
				stringa=f2.readline()
				stringa2=stringa.split()
		   		stringa2[5]='F'
				stringa3=""			
				for el in stringa2:
					stringa3=stringa3+str(" ")+str(el)
				f3.write(str(stringa3)+str("\n"))

			if stringa=='':
				print("operation was done")
				break
		
	except:
		print("Is not possible to open this file")

	print("NEWPOSCAR was created")
	f2.close()
	f3.close()

def makecartesianposcar():
    path=raw_input("insert path with name files =")
    slab=read(path)
    write('POSCAR', slab)


def find():
	path=raw_input("insert path (/for any directories) =")
	tipology=raw_input("key file letters (1), key letter into file (2) =")
	key=raw_input("insert key for example(*.txt) =")
	
	if tipology=='1':
		line=path+str("/")+str(key)
		print line
	if tipology=='1':
		for root, dirs, files in os.walk(path): 
			for f in glob.glob(root+str("/")+str(key)):
				f1.write(f)
				print f
	if tipology=='2':
		kw=raw_input("insert key word into the file =")
		for root, dirs, files in os.walk(path): 
			for f in glob.glob(root+str("/")+str(key)):
				f1.write(f)
				x = open(f, "r").read()  
			        if kw in f:
					print f
   
		
def delete():

	path=raw_input("insert path (/for any directories) =")
	tipology=raw_input("key file letters (1), key letter into file (2) =")
	key=raw_input("insert key for example(*.txt) =")
	sure=raw_input("Are removing some files are you sure? =")
	sure2=raw_input("Are removing some files are you sure? =")

	if (sure=='yes') and (sure2=='yes'):
		if tipology=='1':
			line=path+str("/")+str(key)
			print line
		if tipology=='1':
			for root, dirs, files in os.walk(path): 
				for f in glob.glob(root+str("/")+str(key)):
					if os.path.exists(f):
						os.remove(f)
		if tipology=='2':
			kw=raw_input("insert key word into the file")
			for root, dirs, files in os.walk(path): 
				for f in glob.glob(root+str("/")+str(key)):
					f1.write(f)
					x = open(f, "r").read()  
					if kw in f:
						if os.path.exists(f):
							os.remove(f)

						print f

	 

command=""
f1=open("save.txt","w")	
while command!="exit":
	command=raw_input("Insert command (to remind the commands you can insert help, exit to exit) = ")

	
	if (command=="find"):
		find()
	if (command=="del"):
		delete()
	if (command=="help"):
		help()
	if command=="makecartesianposcar":
		makecartesianposcar()
	if command=="fixallatoms":
		fixallatoms()
	if command=="xyz":
		makexyz()
	if command=="constcoord":
		constcoord()


f1.close()
