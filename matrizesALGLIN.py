#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


v = np.array([4, 5, 6])
print(v)


# In[6]:


v.ndim


# In[7]:


v[0]


# In[8]:


v[1]


# In[9]:


v[0:2]


# In[10]:


v[0:3]


# In[11]:


print(v)


# In[12]:


u=np.array([1,2,3])


# In[13]:


for i in range(3):
  print(u[i])


# In[14]:


soma = 0
for i in range(3):
  soma = soma + u[i]


# In[15]:


print(soma)


# In[16]:


w = np.array([10, 15, 20, 30, 50])


# In[17]:


soma2 = 0
for i in range(5):
  soma2 = soma2 + w[i]
  print(soma2)


# In[18]:


soma2 = 0
for i in range(5):
  soma2 = soma2 + w[i]
print(soma2)


# In[19]:


print(u)
print(v)


# In[20]:


produto_esc = 0
for i in range(3):
  produto_esc = produto_esc + u[i]*v[i]
print(produto_esc)


# In[21]:


A = np.array([[1, 2],
              [0, -1], 
              [4, 6]])
print(A)


# In[22]:


A.ndim


# In[23]:


A.shape


# In[24]:


A[1,1]


# In[25]:


A[2,1]


# In[26]:


A[1:3,0:2]


# In[27]:


A = np.array([[2,3],
              [1, 0],
              [5, 4]])


# In[28]:


B = np.array([[6, 7],
              [8, 9]])


# In[29]:


print(A)
print(B)


# In[30]:


for i in range(3):
  for j in range(2):
    print(A[i,j])


# In[ ]:




