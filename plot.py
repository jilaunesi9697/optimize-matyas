#!/usr/bin/env python
# coding: utf-8

# In[30]:


import matplotlib.pyplot as plt
import numpy as np
def tarsim():
 x=[1,5,10,20,25,30,40,50,60,70,90,100]
 y=[100,90,70,60,5,25,50,40,30,20,10,1]
 fig,ax=plt.subplots()
 ax.plot(x,y,'r*')
 fig2,ax2=plt.subplots()
 ax2.plot(x,y,'b-')
 fig3,ax3=plt.subplots()
 ax3.plot(x,y, 'g.')
 
 return  plt;
plt1=tarsim()
plt1.show()
    


# In[38]:


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)
ax.plot3D(x, y, z, 'gray')
ax.set_title('3D line plot')
plt.show()

 
  


# In[44]:


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

X, Y, Z = axes3d.get_test_data(0.05)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
plt.show()


# In[15]:



from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

X, Y, Z = axes3d.get_test_data(0.05)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()


# In[41]:


import numpy as np
import matplotlib.pyplot as plt
f= lambda x,y:np.sin(x)*np.cos(y)
x= np.linspace(-5,5,100)
y= np.linspace(-5,5,100)
x,y= np.meshgrid(x,y)
f=f(x,y)
fig=plt.figure(figsize=[12,8])
ax=fig.gca(projection='3d')
ax.plot_surface(x,y,f)
plt.show()


# In[82]:


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from numpy import meshgrid
x = np.outer(np.linspace(-2,2, 30), np.ones(30))
y = x.copy().T # transpose
z = np.cos(x ** 2 + y ** 2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
plt.show()


# In[68]:


plt.contour(x,y,z)
plt.show()
plt.scatter(x,y,z)
plt.show()


# In[81]:



X,Y = meshgrid(-2:.2:2)                             
Z = X .* exp(-X.**2 - Y.**2)
surf(X,Y,Z)
show()


# In[ ]:




