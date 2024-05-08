#!/usr/bin/env python
# coding: utf-8

# In[1]:


# two number of sum
num1 = int(input("Enter num 1:-"))
num2 = int(input("Enter num 2:-"))

summ = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2


print()

print("Total sum", summ)
print("Total sum", sub)
print("Total sum", mul)
print("Total sum", div)


# In[6]:


# find out the number squir root

number = float(input("Enter num :-"))

squr = number ** 0.5

print(number,"Squir Root" ,squr)


# In[10]:


# calculate of tringle are

hight = float(input("Enter Hight:-"))
Base = float(input("Enter Base:="))

area = 0.5 * hight * Base

print (hight , Base ,"area is" ,area)



# In[21]:


# swap of two number   without third variable

# a = float(input("Enter num:"))
# b = float(input("Enter num:"))

# befor = a , b 

# after = b , a

# print (befor)
# print(after)

# with third variable

a = float(input("Enter num:"))
b = float(input("Enter num:"))

temp = a
# print (temp)

a = b 
print("a",a)

b = temp 
print("b",b)


# In[24]:


# how to convert killomter to mile

km = float(input("Enter km"))

mile = km * 0.621371
print("km to mile",mile)


# In[31]:


# how to write a progarm to find nagative possitive and zero
num = float(input("Enter num"))

if num > 0:
    print("possitive")
elif num < 0 :
    print("nagative")
else :
    print("zero")


# In[33]:


# number even or odd
num = float(input("Enter num"))

if num % 2 == 0:
    print("even")
else :
    print("odd")


# In[41]:


year = int(input("Enter num"))

if year % 400 == 0 and year  % 100 == 0  :
    print("leap year")
elif year % 4 == 0  and year  % 100 != 0  :
    print("leap year")
else :
    print(" not leap year")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




