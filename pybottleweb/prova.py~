from bottle import route, run, template,get,post,request,static_file, redirect

import os
import os.path
import sqlite3 
import cPickle


@get('/cancella')
def cancella():
  return """<form method="POST" action="/cancella">
                 <input name="nome"     type="text" />
                 <input name="cognome"     type="text" />
                 <input name="telefono"     type="text" />
                 <input type="submit" value="ok" />"""
 

@post('/cancella')
def cancella():
  lista_data=cPickle.load(open('save.pkl','rb'))  
  print(lista_data)
  name     = request.forms.get('nome')
  cognome = request.forms.get('cognome')
  telefono=request.forms.get('telefono')
  conta=0	
  
 
	
   
  for colonna in lista_data: 
    	
    if ((lista_data[conta]==name) and (lista_data[conta+1]==cognome) and (lista_data[conta+2]==telefono)):
       print("ci sono")	
       del lista_data[conta]
       del lista_data[conta]
       del lista_data[conta]
    conta=conta+1 		    	     	   		
  cPickle.dump(lista_data,open('save.pkl','wb+')) 

@get('/aggiungi')
def aggiungi():
  return """<form method="POST" action="/aggiungi">
                 <input name="nome"     type="text" />
                 <input name="cognome"     type="text" />
                 <input name="telefono"     type="text" />
                 <input type="submit" value="ok" />"""
          

@post('/aggiungi')
def aggiungi():
  name     = request.forms.get('nome')
  cognome = request.forms.get('cognome')
  telefono=request.forms.get('telefono')
  
  lista_data=cPickle.load(open('save.pkl','rb'))
   
  lista_data.append(name)
  lista_data.append(cognome)
  lista_data.append(telefono)
  
  
  cPickle.dump(lista_data,open('save.pkl','wb+'))
  redirect('/me')     
  #return """<form method="POST" action="/aggiungi">%end
  #               <input name="nome"     type="text" />"""
 


@get('/login')
def get_login():
	
	return """<form method="POST" action="/login">
                 <input name="name"     type="text" />
                <input name="password" type="password" />
                <input type="submit" value="wqwqw" />
                </form>"""

@post('/login')
def post_login():
	name     = request.forms.get('name')
	password = request.forms.get('password')
        redirect('/me')
#	return template("""Benvenuto {{username}}!""",username=name)



@route('/me')
def get_me():
  lista_data=cPickle.load(open('save.pkl','rb'))
  print lista_data
  return template('prova',lista=lista_data)
#run(host='192.168.2.1')
 
#run(host='127.0.0.1', port=8000, debug=True)
run(host='0.0.0.0', port=8080, debug=True)
