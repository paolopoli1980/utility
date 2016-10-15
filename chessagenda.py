# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 11:49:37 2016

@author: ppoli
"""

black=[['Tb','Cb','Ab','Kb','Rb','Ab','Cb','Tb'],['Pb','Pb','Pb','Pb','Pb','Pb','Pb','Pb'],['**','**','**','**','**','**','**','**'],['**','**','**','**','**','**','**','**'],['**','**','**','**','**','**','**','**'],['**','**','**','**','**','**','**','**'],['Pn','Pn','Pn','Pn','Pn','Pn','Pn','Pn'],['Tn','Cn','An','Kn','Rn','An','Cn','Tn']]
white=[['Tn','Cn','An','Rn','Kn','An','Cn','Tn'],['Pn','Pn','Pn','Pn','Pn','Pn','Pn','Pn'],['**','**','**','**','**','**','**','**'],['**','**','**','**','**','**','**','**'],['**','**','**','**','**','**','**','**'],['**','**','**','**','**','**','**','**'],['Pb','Pb','Pb','Pb','Pb','Pb','Pb','Pb'],['Tb','Cb','Ab','Rb','Kb','Ab','Cb','Tb']]

letterW=['a','b','c','d','e','f','g','h']
letterB=['h','g','f','e','d','c','b','a']


nomefile=raw_input("nome file=")

f1=open(nomefile,'r')
#color=f1.readline()

color=f1.readline()
color=color[0:len(color)-1]
stringa=""
f2=open("stampa.txt","w")

def stampa(color):
     
    if color=='B':
        cont=8
        for el in white:
            f2.write(str(el)+str(cont))
            f2.write(str("\n"))
            print el,str(cont)
            print "\n"
            cont-=1
        print "[ a      b     c     d     e     f     g     h ]"
        f2.write("[ a      b     c     d     e     f     g     h ]\n")
        
    if color=='N': 
        cont=1
        for el in black:
            f2.write(str(el)+str(cont))
            f2.write(str("\n"))
 
            print el,str(cont)
            print "\n"
            cont+=1
        print " [ h     g     f     e      d     c     b    a ]"
        f2.write(" [ h     g     f     e      d     c     b    a ]\n")

    f2.write("*******************************************************\n")     
def start(color):
    piece=""
    stringa=""
    while stringa!='*\n':
        stringa=f1.readline()
        print stringa
            
        if stringa!='*\n':
            if stringa[0]!='&':
                if color=='B':
                    cont=-1
                    for el in letterW:
                        cont+=1
                        if el==stringa[0]:
                            piece=white[8-int(stringa[1])][cont]
                            white[8-int(stringa[1])][cont]="**"
                    cont=-1
                    for el in letterW:
                        cont+=1
                        if el==stringa[2]:
                            white[8-int(stringa[3])][cont]=piece
            if stringa[0]!='&':

                if color=='N':
    
                    cont=-1
                    for el in letterB:
                        cont+=1
                        if el==stringa[0]:
                            piece=black[int(stringa[1])-1][cont]
                            black[int(stringa[1])-1][cont]="**"
                    cont=-1
                    for el in letterB:
                        cont+=1
                        if el==stringa[2]:
                            black[int(stringa[3])-1][cont]=piece                                                    
            if stringa[0]=='&':
                if color=='N':
                    cont=-1
                    for el in letterB:
                        cont+=1
                        if el==stringa[1]:
                            black[int(stringa[2])-1][cont]=stringa[3:5]
                if color=='B':
                    cont=-1
                    for el in letterW:
                        cont+=1
                        if el==stringa[1]:
                            white[8-int(stringa[2])][cont]=stringa[3:5]

                                                    
                    
        if stringa!='*\n":                        
            stampa(color)                                                    
    
stampa(color)
start(color)
f1.close()
f2.close()                
                    
                    
                
            
            
        



