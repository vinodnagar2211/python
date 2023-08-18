#!/usr/bin/env python
# coding: utf-8

# In[43]:


#       prime or not prime
number=int(input("Enter The Number: "))

for i in range (2,number):
    
    if(number == 1):
        print("This Number is Not Prime")
    elif (number%i==0):
        print("This Number is Not prime")
        break
else:
        print("This Number is Prime")


# In[ ]:




