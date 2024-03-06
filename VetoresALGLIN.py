#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


u = np.array([4, ])
u


# In[3]:


v = np.array([4, 8, 1])
v


# In[4]:


u + v


# In[5]:


w = u-v
w


# In[6]:


# Cuidado: u*v não é produto escalar
p = u*v
p
# É apenas uma multiplicação elemento a elemento


# **Produto escalar ou produto interno (inner) ou dot product**

# In[7]:


# usando a função inner do módulo numpy
np.inner(u,v)


# In[ ]:


# usando a função dot do módulo numpy
np.dot(u,v)


# In[ ]:


# usando o símbolo @ de python


# In[ ]:


u@v


# **Calculando módulo ou norma utilizando a sublib linalg**

# In[ ]:


np.linalg.norm(u)


# In[ ]:


# Importando apenas a função norm
from numpy.linalg import norm
norm(u)


# In[ ]:





# **Ângulo entre vetores**

# In[ ]:


print(u)
print(v)


# In[ ]:


cosseno =u@v/(norm(u)*norm(v))
cosseno


# In[ ]:


ang = np.arccos(0.5)
ang
# a resposta sai em radianos


# In[ ]:


np.rad2deg(ang)


# In[ ]:


np.deg2rad(180)


# In[ ]:


cosseno =u@v/(norm(u)*norm(v))
cosseno


# In[ ]:


ang=np.arccos(cosseno)
ang


# In[ ]:


ang = np.rad2deg(ang)
ang


# **Produto vetorial ou cross product**

# In[8]:


a = np.array([4, 2, 3])


# In[9]:


b = np.array([3, 1, 1])


# In[10]:


c = np.cross(a,b)


# In[11]:


np.linalg.norm(c)


# In[ ]:


np.sqrt(9)


# In[ ]:


9**(1/2)

