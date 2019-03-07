#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
import math

#SI unit
h = 6.62*10**-34
c = 3*10**8
k = 1.38*10**-23

v = np.linspace(10**0,10**15.5,100,endpoint = True)
print(v)

num=100

T=5000
B = 2*h*v**3/c**2/(math.e**(h*v/k/T)-1)

plt.plot(v,B,'.')
plt.xlabel=("Frequency (Hz)")
plt.ylabe1=("Intenalty Watta/Hz/m^2")

dB=np.random.normal(0.,10**-8.5,num)
B += dB
plt.plot(v,B)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




