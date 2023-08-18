#!/usr/bin/env python
# coding: utf-8

# In[19]:


#             Armstorng Number

number=int(input("Enter The Number: "))

sum=0
temp=number
while (temp>0):
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp //= 10
    
if(sum == sum):
    print("This Number is armstorng")
else:
    print("This Number is Not armstorng")


# In[ ]:





# In[ ]:




