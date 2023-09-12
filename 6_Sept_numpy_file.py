#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
a=[1,2,3,4,5]
b=np.array(a)
b


# In[2]:


print("Total Dimention=",b.ndim)
print("Total Shape=",b. shape )


# In[3]:


a=[[1,2,3],[4,5,6],[7,8,9]]
b=np.array(a)
b


# In[4]:


print("Total Dimention=",b.ndim)
print("Total Shape=",b. shape )


# # creat user Define (user input list)

# In[5]:


a=[]
size=int(input('Enter Size:'))
for i in range(size):
    val = input("Enter Item")
    a.append(val)
print(a)
b=np.array(a)
b


# In[6]:


a = np.zeros(4)
a


# In[7]:


a = np.zeros((2,3))
a


# In[8]:


a.shape


# In[9]:


a.ndim


# In[10]:


a = np.ones(5)
a


# In[11]:


a = np.ones((2,3))
a


# In[12]:


a = np.eye(3,4)
a


# In[13]:


a = np.eye(3,3)
a


# In[14]:


a = np.eye(3,3)
print(a)


# In[15]:


a= np.diag([1,2,3,55])
a


# In[16]:


a=np.random.randint(1,10,3)
a


# In[17]:


a=np.random.rand(3)
a


# In[18]:


a=np.random.randn(6)
a


# In[ ]:





# In[19]:


a=int(input("Enter min"))
b=int(input("Enter max"))
c=int(input("Enter Total"))

d = np.random.randint(a,b,c)
d


# In[ ]:


np.random.seed(34)
a=np.random.randint(1,10,3)
a


# In[ ]:





# In[ ]:


a=np.linspace(1,5,4)
a


# In[ ]:





# In[ ]:





# In[20]:


a=np.random.randint(1,50,12)
a


# In[25]:


a.reshape(1,12)


# In[24]:


a.reshape(3,4)


# In[ ]:





# In[4]:


import numpy as np
a=np.random.randint(1,50,12)
a


# In[5]:


a.shape


# In[9]:


a.reshape(-1,4)


# In[10]:


a.reshape(2,-1)


# In[ ]:





# In[16]:


a=np.array([1,2,3,4,3,5,7,8,65,4,4,3,3,4,5,6,7,7,8,7])
np.unique(a,return_index=True,return_counts=True)


# In[ ]:





# In[19]:


a=np.array([1,2,3,4,5,6,7,8,9])
b=a[3:6]
print(b)
b[:]=0
print(b)


# In[20]:


a


# In[23]:


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9])
b=a[3:6].copy()
b[:]=0
a


# In[ ]:





# In[24]:


a=np.arange(1,15)
a


# In[25]:


a>10


# In[26]:


a<10


# In[27]:


b=a>10
a[b]


# In[30]:


a[a%2==0]


# In[ ]:





# In[34]:


import numpy as np
a=np.arange(1,5)
a


# In[35]:


a**2


# In[39]:


a+2


# In[37]:


a.reshape(2,2)


# In[40]:


b=np.arange(5,9)
b.reshape(2,2)


# In[41]:


a+b


# In[42]:


a-b


# In[43]:


a*b


# In[45]:


a=a.reshape(2,2)
b=b.reshape(2,2)


# In[ ]:





# In[46]:


b


# In[47]:


a+b


# In[48]:


a


# In[ ]:





# In[49]:


a.dot(b)


# In[ ]:





# In[51]:


a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print(a)
print(b)


# In[ ]:


np.vst


# In[ ]:





# In[2]:


import numpy as np
a  = [[1,2,3] , [4,5,6] , [7,8,9]] 
b = np.array(a) 
b


# In[11]:


import numpy as np
a  = np.array ([[1,2,3],[4,5,6],[7,8,9]])
a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




