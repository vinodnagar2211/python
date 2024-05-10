#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range (1,11):
    print(i)


# In[2]:


for i in range(10,0,-1):
    print(i)


# In[3]:


sum = 0
for i in range(1,11):
    sum = sum+i
print(sum)


# In[4]:


list=[1,2,3,4,5,6]
for i in list:
    print(i)


# In[5]:


list = [2,3,4,5]
produ = 1
for i in list:
    produ = produ * i
print(produ)


# In[6]:


list = [1,2,3,4,5]
p = 1
for i in list:
    p = p * i
print(p)


# In[7]:


for i in range(2,11 , 2):
    print(i)


# In[8]:


s = "nohanlal"
for i in s:
    print(i)


# In[9]:


list = [1,2,3,4,5,6,7,8,9]
total = 0
for i in list:
    total = total + i
ave = total / len(list)
print(ave)


# In[10]:


s = "Mohan Lal"
for i in s:
    if i.isupper():
        print(i)


# In[11]:


s = "apna collage"
print(s[5:])


# In[12]:


age = 15
if (age >= 18):
    print("yes")
else :
    print("no")
    
    


# In[13]:


age = 65
if (age <= 18):
    print("yes")
else :
    print("no")


# num = int(input("Enter num ->"))
# if num % 2 == 0:
#     print("even")
# else :
#     print("odd")

# In[15]:


a = int(input("Enter num 1-:"))
b = int(input("Enter num 2-:"))
c = int(input("Enter num 3-:"))

if (a > b and a > c ):
    print(" a is large",a)
elif(b > a and b > c):
    print("b is large ",b)
else:
    print("c is large",c)


# In[16]:


num = int(input("Enter num -:"))

if num % 7 == 0:
    print (num,"multipal of 7")
else :
    print(num,"not Multipal 7")


# In[17]:


h = [1,2,3,4,5,5,6,77,8]

for i in h :
    print(i)


# In[18]:


l=(1,2,3,4,5,6,7,8,9)
a = 5
g =0
for i in l:
    if i == a :
        print(g)
    g = g +1


# In[19]:


num = int(input("Enter num"))

for i in range (1,11):
    print(num ,"*",i ,"=", num *i)
    


# In[20]:


a = int(input("1"))
b = int(input("2"))
c = int(input("3"))
d = a+b+c
print("total sum",d)


# In[3]:


email = "vin@gamil.com"
pas = int(1234)

mail = input("Email")
pa = int(input("pass"))

if email == mail and pas == pa :
    if pas == pa:
        print("welcome")
    else:
        print("worng pass")
else:
    print("incrorrect email")


# In[5]:


email = "vin@gamil.com"
pas = int(1234)

mail = input("Email")
pa = int(input("pass"))

if email == mail and pas == pa :
    print("welcome")
else :
    print("incorrect mail and pas")


# In[12]:


email = "vin@gamil.com"
pas = int(1234)

mail = input("Email")
pa = int(input("pass"))

if email == mail and pas == pa :
    print("welcome")
elif email == mail and pas != pa :
    print("your pass is wrong")
elif email != mail and pas == pa :
    print("your email is wrong")
# elif email != mail and pas != pa :
#     print("your email and pass both  is wrong")
else :
    print("your email and pass both  is wrong")


# In[ ]:


a = int(input("enter num"))
b = int(input("enter num"))

add = a + b
sub = a - b
mul = a * b
div = a / B

opp = 

if 


# In[ ]:





# In[20]:


for i in range(1,7):
    for j in range(1,i+1):
''        print("*",end = "")
    print()


# In[21]:


for i in range(7,0,-1):
    for j in range(1,i+1):
        print("*",end = "")
    print()


# In[29]:


for i in range (7):
    for j in range (5):
        if i ==0 or i == 6 or j == 0 and i != 0 and i != 6  :
            print("*",end = "")
        else :
            print(end=" ")
    print()


# In[3]:


for row in range (7) :
    for col in range(5):
        if row == 0 or row == 3 or row == 6  or col == 0 :
            print("*",end = "")
        else :
            print(end=" ")
    print()
    


# In[4]:


for row in range (7) :
    for col in range(5):
        if row == 0 or row == 3   or col == 0 :
            print("*",end = "")
        else :
            print(end=" ")
    print()


# In[10]:


for row in range(7):
    for col in range(5):
        if col == 0 or col == 4  :
            print("*",end = "")
        else :
            print(end = "&")
    print()


# In[13]:


year = int(input("Enter year : ="))

if year % 400 == 0 and year % 100 == 0:
    print("This is Leap year") 
elif year % 4 == 0 and year % 100 != 0:
    print("This is Leap year")
else : ("Not Leap Year")


# In[15]:


# how to find Leap and not leap year
num = int(input("Enter num:-"))

if num % 2 == 0 :
    print("This number is Even")
else :
    print("This number is Odd")


# In[22]:


for i in range (1,6):
    for j in range (1, i +1):
        print("*",end = "")
    print ()


# In[8]:


# how to find vovel and consonet
ch = input("Ener char :-")

if ch in ("a","e","i","o","u","A","E","I","O","U"):
    print("vo")
else:
    print("Co")


# In[7]:


# how to calculate simple interst 
p = float(input("Enter Amount :-"))
r = float(input("Enter Rate:-"))
t = float(input("Enter Time:-"))
si = (p * r * t)/100

print(si)


# In[1]:


# how to find vovel and consonet
# ch = input("Ener char :-")

# if ch in ("a","e","i","o","u","A","E","I","O","U"):
#     print("vo")
# else:
#     print("Co")

# list = ["a","e","i","o","u","A","E","I","O","U"]

# ch = input("Enter char :-")

# for i in list :
#     if i == ch :
#         print("Vovel")
#     else :
#         print("Consonet")
        
        


# In[10]:


num = int(input("Enter num"))

if num == 1 :
    print("not Prime number")
if num > 1 :
    for i in range(2,num):
        if num % i == 0 :
            print(" not prime")
            break
    else :
        print("prime")


# In[12]:


# how to calculate factorial number

num = int(input("Enter num :-"))
fact = 1

if num == 0 :
    print("Factorial is 1")
if num < 0 :
    print ("Not Factorial")
if num  > 0 :
    for i in range(1,num +1 ):
        fact = fact * i
print(fact)
        


# In[33]:


# fibonacci sequance
num = int(input("E"))
a = 0
b = 1

if num == 1 :
    print(a)
else :
    print(a)
    print(b)
for i in range(1,num + 1):
    c = a + b
    a = b
    b = c
    print(c)


# In[4]:


# one input
num = int(input("E"))

orer =len(str(num))
summ = 0 
temp = num

while temp > 0 :
    digit = temp % 10
    cube = digit ** orer
    summ = summ + cube
    temp = temp // 10
if summ == num :
    print("Amstrong number")
else :
    print("Not Amstrong number")
        

# ============================================
# two input
l = int(input("E:-"))
u = int(input("E:-"))

for i in range (l , u + 1 ) :
    orer = len(str(i))
    sun = 0
    temp = i
    while temp > 0 :
        digit = temp % 10
        sun  += digit ** orer
        
        temp = temp // 10
    
    if i == sun :
        print (i)
    
# --------------    
# two input 

l = int(input("E:-"))
u = int(input("E:-"))

for i in range (l , u + 1 ) :
    orer = len(str(i))
    sun = 0
    temp = i
    while temp > 0 :
        digit = temp % 10
        cube = digit ** orer
        sun = sun + cube
        temp = temp // 10
    
    if i == sun :
        print (i)


# In[7]:


# prime number
num = int(input("number"))

if num < 0 :
    print("Plz inter possitive number")
else :
    sun = 0
    while num > 0 :
        sun = sun + num
        num = num - 1
    print(sun)
    
    


# In[13]:


# How to convert alphabat to ASCLL value(number )

cha = (input("Charactor"))

number = ord(cha)

print(number)


# In[2]:


# how to find any number of factor
num = int(input("Enter"))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)


# In[9]:


# let's make a simple calculater

a = int(input("Enter num 1 :-")) 
b = int(input("Enter num 2 :-"))

oper = input("Enter Operator")

if oper == "+" :
    print(a,b,"Sum of to Number",a + b)
elif oper == "-" : 
    print(a,b,"Subtarct of to Number",a - b) 
elif oper == "*" : 
    print(a,b,"Multipal of to Number",a * b) 
elif oper == "/" : 
    print(a,b,"Divisible of to Number",a / b) 
else : print("Not Valid input")


# In[12]:


# print calender
import calendar

year = int(input("Enter year"))
month = int(input("Enter month"))

calendar = calendar.month(year,month)
print(calendar)


# In[17]:


# les's go find palindrom number or not palindrom number

num = input("Enter number :-")
reve = num [ : : -1]

if num == reve :
    print("This is a Palindrom ")
else :
    print("This is a not Palindrom")


# In[21]:


# remove punchuvation
punch = ''' !()_[]{}:;':?\/!@#$%^&*' '''

string  = input("Enter string")

emp_str = ""

for i in string :
    if i not in punch :
        emp_str = emp_str + i
print()
print(emp_str)


# In[29]:


a = "my Name Is Vinod Nagar"
w = a.split(" ") 
print(w)

for i in range (len(w)) :
    w[i] = w[i].lower()
print(w)
w.sort()
print(w)


# In[ ]:


a = "my Name Is Vinod Nagar"

w = a.split()  # all word split
print(w)
for i in range(len(w)) :
    w[i] = w[i].lower()   # all word lower
print(w)
w.sort() # all word sort
print(w)


# In[38]:


# st = input("Enter string")
# s = st.split(" ")
# t = tupel(s)
# print(t)
# vol = "aeiouAEIOU"

# for i in range  (t):
#     if i == vol :
#         print("vovel")
#     else :
#         print("NO")
    


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





# In[ ]:




