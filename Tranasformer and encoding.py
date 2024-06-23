#!/usr/bin/env python
# coding: utf-8

# # One Hot Encodding ANd get_dummies 

# In[1]:


import numpy as np 
import pandas as pd 


# In[2]:


df = pd.read_csv("C:\\Users\\saurabh\\Desktop\\pyth\\cars.csv" , usecols = ['name' , 'km_driven' , 'fuel' , 'owner' , 'selling_price'])


# In[3]:


df.head() 


# In[4]:


df.isnull().sum() 


# In[5]:


df['owner'].value_counts() 


# # One Hot Encoding using Pandas

# In[6]:


pd.get_dummies(df , columns = ['fuel' , 'owner'])


# In[7]:


pd.get_dummies(df , columns = ['fuel' , 'owner'] , drop_first = True)


# # Using One Hot Encoding 

# In[8]:


from sklearn.model_selection import train_test_split 


# In[10]:


x = df.drop(columns = ['km_driven'] , axis = 1)
y = df['km_driven']


# In[11]:


x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.2 , random_state = 42)


# In[12]:


x_train.head() 


# In[13]:


from sklearn.preprocessing import OneHotEncoder 


# In[14]:


ohe = OneHotEncoder(drop = 'first' , sparse = False)


# In[15]:


x_train_new = ohe.fit_transform(x_train[['fuel' , 'owner']])


# In[16]:


x_train_new


# In[17]:


x_test_new = ohe.fit_transform(x_test[['fuel' , 'owner']])


# # Column Transformer 

# In[26]:


df = pd.read_csv("C:\\Users\\saurabh\\Desktop\\pyth\\covid_toy.csv")


# In[27]:


df.head() 


# In[28]:


df.isnull().sum() 


# In[29]:


from sklearn.impute import SimpleImputer # for missing values imputation(filling) 

from sklearn.preprocessing import OneHotEncoder # Category ==> Sub-category ==> column creation 
from sklearn.preprocessing import OrdinalEncoder # Sub-Category ==>Convert into  Numbers 


# In[30]:


x = df.drop(columns = ['has_covid'])
y = df['has_covid']


# In[31]:


from sklearn.model_selection import train_test_split 

x_train , x_test , y_train ,y_test = train_test_split(x,y,test_size=  0.2 , random_state = 42)


# # Manually type output 

# In[32]:


# Adding Simple Imputer to fever column  

si = SimpleImputer() 
x_train_fever = si.fit_transform(x_train[['fever']])

x_test_fever = si.fit_transform(x_test[['fever']])


# In[33]:


# x_train


# In[37]:


x_train_fever.shape


# # step-2 
# 
# Ordinal Encoding ==> Cough 

# In[47]:


oe = OrdinalEncoder(categories = [[ 'Mild' , 'Strong']])

x_train_cough = oe.fit_transform(x_train[[ 'cough']])


# In[48]:


# x_train.head()
x_train_cough.shape


# # step -3    OneHotEncoding ===> Gender , City 

# In[50]:


ohe = OneHotEncoder(drop = 'first' , sparse = False)
x_train_gender_city = ohe.fit_transform(x_train[['gender' , 'city']])


# In[53]:


x_train_gender_city.shape


# # step - 4 (Extracting Age) 

# In[54]:


x_train_age = x_train.drop(columns = ['gender' , 'fever' , 'cough' , 'city']).values 


# In[55]:


x_train_age.shape


# # step-5 (Concatenate all the data )

# In[56]:


x_train_transformed = np.concatenate((x_train_age , x_train_fever , x_train_gender_city , x_train_cough) , axis = 1)


# In[58]:


x_train_transformed.shape


# # We can do this in one cell using Column Transformer 

# In[59]:


from sklearn.compose import ColumnTransformer 


# In[60]:


transformer = ColumnTransformer(transformers = [
    ('a' , SimpleImputer() , ['fever']) ,  #Simple Imputer fill your missing values 
    ('b' , OrdinalEncoder(categories = [['Mild' , 'Strong']]) , ['cough']),
    ('c' , OneHotEncoder(sparse = False , drop = 'first') , ['gender' , 'city'])
] , remainder = 'passthrough')   # remainder = 'ppassthrough' ==> means rest all are columns remain constant . 


# In[62]:


transformer.fit_transform(x_train).shape


# In[ ]:




