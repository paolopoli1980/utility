import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

a=np.random.rand(50,2)
b=np.random.rand(50,2)+0.5
matrix=np.concatenate((a, b), axis=0)
kmeans = KMeans(n_clusters=2, random_state=0).fit(matrix)
kmeans.predict([[0, 0], [2, 2]])
kmeans.cluster_centers_
fig, ax=plt.subplots()
ax.plot(matrix[:,0],matrix[:,1],'o')

#print(matrix)
print (kmeans.cluster_centers_)
c=kmeans.cluster_centers_
plt.show()   
list1=[]
list2=[]
for el in matrix:
    print(el)
    if np.sqrt((el[0]-c[0][0])**2+(el[1]-c[0][1])**2)<np.sqrt((el[0]-c[1][0])**2+(el[1]-c[1][1])**2):
        list1.append(el)
    else:
        list2.append(el)
print (list1)
print (list2)
x1=len(list1)
x2=len(list2)
s1=(x1,2)
s2=(x2,2)

mat1=np.zeros(s1)
mat2=np.zeros(s2)
print (mat1)
for i in range(x1):
    mat1[i]=list1[i]
for i in range(x2):
    mat2[i]=list2[i]
    
fig, ay=plt.subplots()
ay.plot(mat1[:,0],mat1[:,1],marker='^')
ay.plot(mat2[:,0],mat2[:,1],marker='o')
plt.show()
        
        
