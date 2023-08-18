#!/usr/bin/env python
# coding: utf-8

# In[2]:


#            factorial Number
number=int(input("Enter The Number: "))
fac=1
if(number<0):
    print("This Number is Not fact")
if(number == 0 ):
    print("This Number fac is=",1)
if(number > 0):
    for i in range(1,number+1):
        fac=fac*i
print("This Number fac is=",fac)


# In[ ]:




