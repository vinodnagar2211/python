#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # how to creat DataFrame usting Dictionary

# In[8]:


a={
    "Emp_Id":[1,2,3,4,5,6,7,8],
    "Name":["sam","Govrav","Kriti","Sam","Pallavi","Ankush","Mohit","Ram"],
    "Department":["HR","IT","IT","Operationos","HR","Operations","HR","IT"],
    "Salary":[1000,2000,3000,4000,5000,6000,7000,8000]
    
}


# In[9]:


import pandas as pd
a


# In[18]:


import pandas as pd
df=pd.DataFrame(a)
df


# In[19]:


df.columns


# In[22]:


df["Name"]


# In[69]:


df['Name'].value_counts()


# In[70]:


df['Department'].value_counts()


# In[ ]:





# In[23]:


df['Name'][0:4]


# In[24]:


df['Name'][3]


# In[25]:


df.head()


# In[26]:


df.head(2)


# In[27]:


df.tail()


# In[28]:


df.tail(3)


# In[46]:


df.sample(4)


# In[50]:


df['Name'][0]='vinod'
df


# In[51]:


df


# # loc== df.loc_range,columns_range

# In[52]:


df.loc[2:5,['Name','Department']]


# In[53]:


df.loc[2:5,:]


# In[60]:


df.iloc[2:5,[1,3]]


# In[78]:


df.to_csv("C:\\Users\\HP\\Desktop\\New folder\\vinod.csv")


# In[81]:


df=pd.read_csv('C:\\Users\\HP\\Desktop\\New folder\\vinod.csv')
df


# In[6]:


import pandas as pd
import numpy as np
df=pd.read_csv("C:\\Users\\HP\\Desktop\\placement.csv")
df


# In[7]:


df.head()


# In[9]:


df.tail()


# In[11]:


df.empty


# In[13]:


df.isnull()


# In[14]:


df['cgpa'].isnull().sum()


# In[15]:


df.shape


# In[16]:


df.size


# In[21]:


df=df.copy()
df


# In[23]:


df.sort_values(by='cgpa')


# In[24]:


df.sort_index()


# In[27]:


df=df.astype(int)
df


# In[28]:


df.add(4)
df


# In[30]:


df['vinod']=df['cgpa'].add(10)
df


# In[34]:


df=df.drop(columns=['vinod'],axis=1)


# In[35]:


df


# In[36]:


df.count()


# In[37]:


df.max()


# In[39]:


df.min()


# In[40]:


df['cgpa'].min()


# In[41]:


df.mean()


# In[42]:


df.median()


# In[43]:


df.sum()


# In[44]:


df


# In[47]:


df.filter(items=['cgpa','placed'])


# In[48]:


df.filter(items=[5,6,7],axis=0)


# In[49]:


df.filter(like='5',axis=0)


# In[ ]:





# In[ ]:





# In[5]:


import numpy as np
import pandas as pd


# In[8]:


pd.read_csv("C:\\Users\\HP\\Desktop\\covid_toy.csv")


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




