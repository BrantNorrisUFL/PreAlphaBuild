#!/usr/bin/env python
# coding: utf-8

# In[48]:


from qutip import *


# In[49]:


import numpy as np

import matplotlib.pyplot as plt


# In[50]:


print(Qobj([[0],[0],[0],[0]]))


# In[51]:


x = np.array([[0, 0, 0, 0]])


# In[52]:


print(Qobj(x))


# In[53]:


basis(4,0)


# In[54]:


basis(4,1)


# In[55]:


coherent(4,0.5-0.5j)


# In[56]:


destroy(4)


# In[57]:


sigmax()


# In[58]:


sigmay()


# In[59]:


sigmaz()


# In[60]:


jmat(5/2.0, '-')


# In[61]:


jmat(5/2.0, '+')


# In[62]:


obj = Qobj([[0],[1]])


# In[63]:


print(obj)


# In[64]:


obj.isherm


# In[65]:


obj = sigmax()


# In[66]:


obj.isherm


# In[67]:


obj = coherent(2,1)


# In[68]:


print(obj)


# In[69]:


obj.isherm


# In[70]:


obj = sigmaz()


# In[71]:


obj.isherm


# In[ ]:





# In[ ]:




