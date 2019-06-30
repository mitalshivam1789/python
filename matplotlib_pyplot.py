import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5,6,7]) # when having only y axis value
plt.ylabel('some numbers')
#plt.plot([1,2,3,4,5],[1,4,9,16,25])#plt.plot([x],[y])
plt.plot([1,2,3,4,5],[1,4,9,16,25],'ro')#cordinates of points
plt.axis([0,6,0,30])# values on axis

plt.show()
import numpy as np
t = np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
# r--  - for dash symbol
# bs  - for square symbol
# g^  - for triangle symbol
plt.show()
data = {'a':np.arange(50),'c':np.random.randint(0,50,50),'d':np.random.randn(50)}
data['b'] = data['a']+10*np.random.randn(50)
data['d'] = np.abs(data['d'])*100

plt.scatter('a','b',c='c',s='d',data = data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()