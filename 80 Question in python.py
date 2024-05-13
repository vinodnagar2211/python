#!/usr/bin/env python
# coding: utf-8

# In[7]:


# User will input (3ages).Find the oldest one

a = int(input("Enter age:-"))
b = int(input("Enter age:-"))
c = int(input("Enter age:-"))

print()

if a > b and a > c :
    print ("A is large:-",a)
elif b > c :
    print ("B is large :-",b)
else :
    print("c is large :-" ,c)
    


# In[8]:


# Write a program that will convert celsius value
celsius  =  float(input("Enter celsius value:-"))

fa = (celsius * 9/5) + 32

print(fa)


# In[10]:


# User will input (2numbers).Write a program to swap the numbers

a = int(input("Enter num a :-"))
b = int(input("Enter num b :-"))
print()
# before
a , b = a , b
print("befor swap ",a,b)
print()
# after
a , b = b , a
print("after swap",a,b)



# In[2]:


# Write a program that will give you the sum of 3 digit

num = int(input("Enter num :- "))

a = num % 10      # 245 % 10 = 5
num = num // 10   # 245 // 10 = 24
b = num % 10      # 24 % 10 = 4
c = num // 10     # 24 // 10 = 3

rev = (a + b + c)
print (rev)


# In[13]:


# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.
num = (input("num "))
rev = num[ : : -1]
print()
print("befor",num)
print("after",rev)




# In[15]:


# Write a program that will tell whether the number entered by the user is odd or even

num = int(input("num"))

if num % 2 == 0 :
    print("even")
else :
    print("odd")


# In[19]:


# Write a program that will tell whether the given year is a leap year or not.

year = int(input("year"))

if year % 400 == 0 and year % 100 == 0 :
    print("leap year")
elif year % 4 == 0 and year % 100 != 0 :
    print("leap")
else :
    print("Not leap")



# In[ ]:


# Write a program to find the euclidean distance between two coordinates


# In[23]:


# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.
a = int(input("Enter 1"))
b = int(input("Enter 2"))
c = int(input("Enter 3"))

t = a + b + c

if t == 180 and a != 0 and b != 0 and  c != 0 :
    print("yea")
else :
    print("not")


# In[7]:


# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit


cost =     int(input("Enter cost price :-"))
selling = int(input("Enter Selling price :-"))
diff = selling - cost           
if selling > cost :
           print ("Profit is",diff,"Rs")
else :
           print("Lose is",diff,"Rs")
    


# In[11]:


# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.
p = float(input("p"))
r = float(input("r"))
t = float(input("t"))

si = (p * t * r) / 100

print("The Simple interst is :-",si)
    
    





# In[ ]:


# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.


# In[13]:


# Write a program that will tell whether the given number is divisible by 3 & 6.
num = int(input("enter"))

if num % 3 == 0 and num % 6 == 0 :
    print("full Divisiable")
else : 
    print("Not divisiable")


# In[4]:


"""  Write a program that will determine weather when the value of
temperature and humidity is provided by the user.
TEMPERATURE(C) HUMIDITY(%) WEATHER
>= 30 >=90 Hot and Humid
>= 30 < 90 Hot
<30 >= 90 Cool and Humid
<30 <90 Cool   """

temp = int(input("temp"))
hu = int(input("hu"))

if temp >= 30 and hu >= 90 :
    print("Hot and Humid")
elif temp >= 30 and hu < 90 :
    print("Hot")
elif temp < 30 and hu >= 90 :
    print("Cool and Humid")
elif temp < 30 and hu < 90 :
    print("Cool")


# In[9]:


# 7. Write a program that will take three digits from the user and add the square of each digit.
# a  = int(input("a"))
# b  = int(input("b"))
# c  = int(input("c"))

# a  = a ** 2
# b = b ** 2
# c = c **2

# sun = a + b + c
# print(sun)


i = int(input("num"))

a = i % 10         # 432    a = 2
i = i // 10      # 432    i = 43
b = i % 10       #  43     b = 3
c = i // 10

a  = (a ** 2) + (b ** 2) + (c **2)


print(a)


# In[ ]:


# 18. Write a program that will check whether the number is armstrong number or not.



# In[ ]:


# 19. Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not



# In[ ]:


# 20. Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax
# (if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _ – 30%)(0-1lakh print k).


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




