#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 


# In[2]:


df = pd.read_csv("C:\\Users\\saurabh\\Desktop\\pyth\\placement.csv")


# In[3]:


df.head() 


# In[4]:


df.head() 


# In[5]:


df.tail() 


# In[6]:


df.describe() 


# In[7]:


df.info() 


# In[8]:


df.dtypes


# In[9]:


df.columns


# In[10]:


df.describe() 


# In[11]:


top_left_corner_df = df.iloc[:5 , :3]
top_left_corner_df


# In[12]:


df.empty


# In[13]:


df.isnull()  #if any missing value then it show true otherwise false . 


# In[14]:


df.isnull().sum()   #total of missing values in a df 


# In[15]:


df['cgpa'].isnull().sum() 


# In[16]:


df.shape  #n(row) , n(columns) 


# In[17]:


df.size   #n(rows)*n(columns) 


# In[18]:


# df.values 


# In[19]:


# df = df.copy() 


# In[20]:


df


# In[21]:


df.sort_values(by = 'cgpa')


# In[22]:


df.sort_index()   #it will sort your indexing in ascending order . 


# In[23]:


df = df.astype(int)   #how to change data type of data frame 


# In[24]:


df.add(4) 


# In[25]:


df['vind'] = df['cgpa'].add(10)


# In[26]:


df


# In[27]:


df = df.drop(columns = ['vind'] , axis = 1) #how to remove single or multiple column 


# In[28]:


df


# In[29]:


df.count()   #total elements in a column


# In[30]:


df.max() 


# In[31]:


df.min() 


# In[32]:


df['cgpa'].min()


# In[33]:


df.mean()


# In[34]:


df.median()


# In[35]:


df.sum() 


# In[36]:


df


# In[37]:


df.filter(items = ['cgpa' , 'placed'])


# In[38]:


df.filter(items = [5,6,7] , axis = 0)


# In[39]:


df.filter(like = '5' , axis = 0)


# In[40]:


# df.to_dict()     #data store in dictionary format 


# In[41]:


# df.to_string()  #save in string 


# In[42]:


df.rename(columns = {'cgpa':'half_yearly_exam' , 
                    'resume_score':'semester_marks'})   #how to rename a column 


# In[45]:


df['new_resume'] = df['resume_score'].where(df['resume_score']>5 , other = 0)


# In[46]:


df


# In[47]:


df = pd.read_csv("C:\\Users\\saurabh\\Desktop\\pyth\\covid_toy.csv")


# In[48]:


df.head() 


# In[49]:


from sklearn.preprocessing import LabelEncoder 


# In[50]:


lb = LabelEncoder() 


# In[51]:


df['gender'] = lb.fit_transform(df['gender'])
df['cough'] = lb.fit_transform(df['cough'])
df['city'] = lb.fit_transform(df['city'])
df['has_covid'] = lb.fit_transform(df['has_covid'])


# In[52]:


df


# In[ ]:




