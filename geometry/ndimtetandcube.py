########################################################################
# number of vertex and n-1 faces of a n dimensional tetrahedron and cube
########################################################################

import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

cubefaces=[]
cubevertex=[]
tetravertex=[]
tetrafaces=[]
ndim=[]
n=10
for i in range(n):
    ndim.append(i)
    cubefaces.append(2*i)
    cubevertex.append(2**i)
    tetravertex.append(i+1)
    tetrafaces.append(i+1)


plt.figure()
# cubevertex
plt.subplot(221)
plt.plot(ndim,cubevertex)
plt.ylabel('cubevertex')
plt.xlabel('ndim')
plt.title('cubevertex')
plt.grid(True)


# cubefaces
plt.subplot(222)
plt.plot(ndim,cubefaces)
plt.ylabel('cubefaces')
plt.xlabel('ndim')
plt.title('cubefaces')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(ndim,tetravertex)
plt.ylabel('tetravertex')
plt.xlabel('ndim')
plt.title('tetravertex')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(ndim,tetrafaces)
plt.ylabel('tetrafaces')
plt.xlabel('ndim')
plt.title('tetrafaces')
plt.grid(True)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5,
                    wspace=0.35)

plt.show()
