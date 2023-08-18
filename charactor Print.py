#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#       charactor Print
start_value=122

for i in range(4):
    for j in range (i):
        print(" ",end=(""))
    for k in range(4 - i):
        print (chr(start_value),end="")
        start_value-=1
    print()

