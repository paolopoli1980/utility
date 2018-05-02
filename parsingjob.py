import requests
from bs4 import BeautifulSoup


# Collect and parse first page


limax=1000
def call_sub():
    for i in range(len(stringa)):
        if stringa[i:i+22]=='<span class="company">':
            
            print (stringa[i:i+22])
            j=i+22
            stringa2=""
            cont=0
            while stringa[j]!='<' and cont<limax:
                stringa2+=str(stringa[j])
                j+=1
                cont+=1
               # print (cont)
                    
            if cont<limax:
                cont=0
                print (stringa2)    
                k=i
                while stringa[k:k+8]!='location' and cont<limax:
                    k+=1
                    cont+=1
                stringa3=""
                t=k
                cont=0
                while stringa[t]!='<' and cont<limax:
                    stringa3+=stringa[t]
                    t+=1

                print (stringa3)            
                k=i    
                while stringa[k:k+6]!='date">' and cont<limax:
                    
                    k+=1
                    cont+=1
                    
                t=k
                stringa3=""
                while stringa[t]!='<' and cont<limax:
                    stringa3+=stringa[t]
                    t+=1

                print (stringa3)            
    print (len(stringa))

def english_indeed_scientistdev(n):
    global stringa
    for r in range(n):
        if r==0:
            page = requests.get('https://www.indeed.co.uk/jobs?q=Scientific+Software+Developer')
        else:
            page = requests.get('https://www.indeed.co.uk/jobs?q=Scientific+Software+Developer&start='+str(r*10))
        soup = BeautifulSoup(page.text, 'html.parser')
        #print (soup)
        f1=open('translate.txt','w')
        f1.write(str(soup))
        f1.close()
        f1=open('translate.txt','r')
        stringa=str(f1.read())
        f1.close()
        call_sub()
    
def english_indeed_data(n):
    global stringa
    for r in range(n):
        if r==0:
            page = requests.get('https://www.indeed.co.uk/jobs?q=Data+Scientist')
        else:
            page = requests.get('https://www.indeed.co.uk/jobs?q=Data+Scientist&start='+str(r*10))
        soup = BeautifulSoup(page.text, 'html.parser')
        #print (soup)
        f1=open('translate.txt','w')
        f1.write(str(soup))
        f1.close()
        f1=open('translate.txt','r')
        stringa=str(f1.read())
        f1.close()
        call_sub()

 

        
def italian_indeed_data(n):
    global stringa
    for r in range(n):
        if r==0:
            page = requests.get('https://it.indeed.com/jobs?q=Data+Scientist')
        else:
            page = requests.get('https://it.indeed.com/jobs?q=Data+Scientist&start='+str(r*10))
        soup = BeautifulSoup(page.text, 'html.parser')
        #print (soup)
        f1=open('translate.txt','w')
        f1.write(str(soup))
        f1.close()
        f1=open('translate.txt','r')
        stringa=str(f1.read())
        f1.close()
        call_sub()
print ('1->datascientist ita,2->datascientisr uk,3->scientificdeveloper uk')

q1=input("Choose your option")
q2=input("How many pages?")
q2=int(q2)
if q1=='1':
    italian_indeed_data(q2)
if q1=='2':
    english_indeed_data(q2)
if q1=='3':
    english_indeed_scientistdev(q2)
