#!/usr/bin/env python
# coding: utf-8

# In[17]:


#                Fibonacci Number

a=0
b=1
number=int(input("Enter The Num: "))

if(number == 1):
    print(a)
else:
    for i in range(1,number+1):
        c=a+b
        a=b
        b=c
        print(c)


# In[ ]:





# In[ ]:




