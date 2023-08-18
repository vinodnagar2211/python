#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#   Replace a e i o u  to xz

a=input("Enter the ")
b="aeiou,AEIOU"
result=""
for i in a:
    if i in b:
        result=result+"xz"
    else:
        result=result+i
print(result)

