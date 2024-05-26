#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://csiplearninghub.com/python-fundamentals-practice-questions/


# In[5]:


n = int(input("Enter num :-"))
for i in range(1 , n + 1) : 
    for j in range (1, i + 1) : 
        print("*",end = "")
    print()


# In[6]:


n = int(input("Enter num :-"))
for i in range(n + 1,1,-1) : 
    for j in range (0, i - 1) : 
        print("*",end = "")
    print()
    
# n = int(input("Enter"))
# for i in range(n + 1,1,-1):     #only for chagne line
#     for i in range(1,i ):
#         print("*",end = "")
#     print()


# In[24]:


n = int(input("num"))
for i in range(0,5):
    for j in range(i+1):
        print("*",end="")
    print()    
        
for i in range(5,0,-1):
    for j in range(i-1):
        print("*",end="")
    print()


# In[21]:


n = int(input("num"))
for i in range(0,n):
    for j in range(1,n-i):
        print("-",end="")
        
    for k in range(0,i+1):
        print("*",eand="")
    print()
    



# In[22]:


n = int(input("num"))
for i in range(0,5):
    for j in range(0,i):
        print("-",end="")
        
    for k in range(5,i,-1):
        print("*",end="")
    print()


# In[25]:


n = int(input("num"))
for i in range(0,n):
    for j in range(1,n-i):
        print("-",end="")
        
    for k in range(0,i+1):
        print("*",end="")
    print()
    
for i in range(0,5):
    for j in range(0,i):
        print("-",end="")
        
    for k in range(5,i,-1):
        print("*",end="")
    print()


# In[ ]:





# In[ ]:





# In[2]:


for i in range (0,6) :
    for j in range (0,5) :
        if (i == 0 or i == 3) or (j == 0 or j == 4) :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()
            
        


# In[9]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 0 or i == 3  or i == 5 or j == 0 or j == 4 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[14]:


for i in range(0,6) :
    for j in range(0,5) :
        if (i == 0 or i == 5 ) or j == 0 :
            print("*",end = "")
        else : 
            print(" ",end = "")
    print()


# In[15]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 0 or i == 5 or j == 0 or j == 4 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[18]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 0 or i == 3  or i == 5 or j == 0 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[19]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 0 or i == 3  or j == 0 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[22]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 3  or j == 0 or j == 4 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[26]:


for i in range(0,6) :
    for j in range(0,7) :
        if i == 0 or i == 5 or j == 3  :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[27]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 5 or j == 0 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[29]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 0 or i == 5 or j == 0 or j == 4 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[33]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 0 or j == 2:
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[36]:


for i in range(0,6) :
    for j in range(0,5) :
        if i == 5 or j == 0 or j == 4 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[ ]:





# In[ ]:


G ,J , K ,M , N ,P ,Q ,R, S,W, X,Y ,Z


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[9]:


#                                        2 Alphabat Join
for i in range(0,6) :
    for j in range(0,7) :
        if i == 0 or j == 2:
            print("*",end = "")
        else :
            print(" ",end = " ")
           
   
    for j in range(0,5) :
        if i == 5 or j == 0 or j == 4 :
            print("*",end = "")
        else :
            print(" ",end = "")
    print()


# In[13]:


#                                  3 Alpha Join

for i in range(0,6) :
    for j in range(0,6) :
        if i == 0 or j == 2:
            print("*",end = "")
        elif j == 5:
            print(" ",end = "")
        else :
            print(" ",end = "")
           
   
    for j in range(0,5) :
        if i == 5 or j == 0 or j == 4 :
            print("*",end = "")
        elif j == 5:
            print(" ",end = "")
        else :
            print(" ",end = "")
   
    for j in range(0,7) :
        if i == 0 or i == 5 or j == 3  :
            print("*",end = "")
        elif j == 5:
            print(" ",end = "")
        else :
            print(" ",end = "")
    print()


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





# In[ ]:





# In[ ]:





# In[ ]:


# Print all uppercase letters in a string using a for loop:

my_string = "Hello World"
for char in my_string:
    if char.isupper():
        print(char)


# In[ ]:


Count the number of vowels in a string using a for loop:

my_string = "Hello World"
vowels = "AEIOUaeiou"
count = 0
for char in my_string:
    if char in vowels:
        count += 1
print(count)
    


# In[ ]:




