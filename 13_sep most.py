#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[4]:


df=pd.read_csv('C:\\Users\\HP\\Desktop\\covid_toy.csv')
df


# In[5]:


df.head()


# In[6]:


df.head(3)


# In[7]:


df.tail()


# In[8]:


df.tail(3)


# In[10]:


df.describe()


# In[11]:


df.info()


# In[12]:


df.dtypes


# In[13]:


df.columns


# In[14]:


top_left_conner=df.iloc[1:5,1:4]
top_left_conner


# In[15]:


df.empty


# In[16]:


df.isnull()


# In[23]:


df.isnull().sum()



# In[25]:


df['age'].isnull().sum()


# In[27]:


df["fever"].isnull().sum()


# In[29]:


df.shape


# In[30]:


df.size


# In[31]:


df.values


# In[33]:


df=df.copy()
df


# In[36]:


df.sort_values(by='age')


# In[37]:


df.sort_index()


# In[41]:


df=df.astype(int)
df


# In[43]:


df.add(5)
df


# In[47]:


df['age']=df['fever'].add(1)
df


# In[48]:


df=df.drop(columns=['age'],axis=1)
df


# In[49]:


df.count()


# In[52]:


df['fever'].min()


# In[54]:


df.mean()


# In[56]:


df['fever'].sum()


# In[65]:


# ==========================not==============
df.filter(items = ['fever','city'])
df


# In[66]:


df.filter(items=[5,6,7],axis=0)


# In[67]:


#      NOt  Under Standing
df.to_dict()


# In[68]:


df.to_srting()


# In[76]:


#  ======== Not ========== Change=========
df.rename(columns={'fever':'not',
                  'city':'village'})
df


# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


import numpy as np
import pandas as pd
df=pd.read_csv('C:\\Users\\HP\\Desktop\\covid_toy.csv')
df


# In[3]:


df.head()


# In[5]:


#    Not ===========Under Standing
df['age'] = df['fever'].where(df['fever']>5 , other = 0)
df


# In[14]:


#  ========NOt Under standing
df.filter(like = '5' , axis = 0)


# In[6]:


df.head()


# In[23]:


# ==========================not==============
df.filter(items=['city','has_covid'],axis=1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




