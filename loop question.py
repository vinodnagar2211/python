#!/usr/bin/env python
# coding: utf-8

# In[3]:


for i in range (1,11):
    print(i)


# In[4]:


for i in range(10,0,-1):
    print(i)


# In[8]:


sum = 0
for i in range(1,11):
    sum = sum+i
print(sum)


# In[9]:


list=[1,2,3,4,5,6]
for i in list:
    print(i)


# In[15]:


list = [2,3,4,5]
produ = 1
for i in list:
    produ = produ * i
print(produ)


# In[16]:


list = [1,2,3,4,5]
p = 1
for i in list:
    p = p * i
print(p)


# In[19]:


for i in range(2,11 , 2):
    print(i)


# In[5]:


s = "nohanlal"
for i in s:
    print(i)


# In[6]:


list = [1,2,3,4,5,6,7,8,9]
total = 0
for i in list:
    total = total + i
ave = total / len(list)
print(ave)


# In[8]:


s = "Mohan Lal"
for i in s:
    if i.isupper():
        print(i)


# In[14]:


s = "apna collage"
print(s[5:])


# In[21]:


age = 15
if (age >= 18):
    print("yes")
else :
    print("no")
    
    


# In[23]:


age = 65
if (age <= 18):
    print("yes")
else :
    print("no")


# In[27]:


num = int(input("Enter num ->"))
if num % 2 == 0:
    print("even")
else :
    print("odd")


# In[30]:


a = int(input("Enter num 1-:"))
b = int(input("Enter num 2-:"))
c = int(input("Enter num 3-:"))

if (a > b and a > c ):
    print(" a is large",a)
elif(b > a and b > c):
    print("b is large ",b)
else:
    print("c is large",c)


# In[33]:


num = int(input("Enter num -:"))

if num % 7 == 0:
    print (num,"multipal of 7")
else :
    print(num,"not Multipal 7")


# In[34]:


h = [1,2,3,4,5,5,6,77,8]

for i in h :
    print(i)


# In[44]:


l=(1,2,3,4,5,6,7,8,9)
a = 5
g =0
for i in l:
    if i == a :
        print(g)
    g = g +1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




