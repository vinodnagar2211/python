#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#            Leap or Not Leap Year
year=int(input("Enter The Year"))

if(year%400==0 and year%100==0):
    print("This Year is Leap")
elif(year%4==0 and year%100!=0):
    print("This Year is Leap")
else:
    print("This Year is Not Leap")

