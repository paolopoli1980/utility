 
<html>
  <head>
    <title></title>
    <meta content="">
    <style></style>
  </head>
  <body>

 
 

 
  

<table border="1">
%contatore=0

%for col in lista:
%contatore=contatore+1 
  <tr>
 
%if contatore == 1:
<td> nome {{col}} </td>
%end
%if contatore == 2:
<td> cognome {{col}} </td>
%end

%if contatore == 3:
<td> telefono {{col}} </td>
%contatore=0
%end

</tr>
%end
</table>
 


</div>

  </body>
</html>
