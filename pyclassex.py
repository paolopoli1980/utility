import random
class unit():

	def __init__(self):
		self.x=0
		self.y=0
	def met(self,nobj,l):
		for j in range(nobj):
			if obj[j].x>0:
				print "the unit number"+str(j)+"has" +str(obj[j].x)+"value"
				if j!=l:
					self.y+=1	

					
		
		
def random_definition():
	for k in obj:
		k.x=random.uniform(-1,1)

obj=[unit(),unit(),unit()]
nobj=len(obj)
print nobj

random_definition()
l=-1

for i in obj:
	l+=1
	i.met(nobj,l)

for i in obj:
	print i.y 




