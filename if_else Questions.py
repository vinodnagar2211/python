#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ****************************************Doubt Quetions ********************************************

#                                     test 2 question 7
# write the output of the following:
# num = input("num")

# if ture :
#     print("101")
# else :
#     print("202")

print("********************************************************")            #  Between
print("=====================================================")                # End


# test 2 qutestion 8
"""write the logical expression for the following :
a is greater then B and C greater than D  """
    
print("=====================================================")





# In[ ]:





# # ========================================================

# In[ ]:





# In[ ]:


# **********************************Two method which one best*******************************************


# In[ ]:


#  only int valid string is not valid
#  incorrect code write by me
num = int(input("num"))

if int(num) == int(num) :
    if num == 1 :
        print("som")
    elif num == 2 :
        print("tue")
    else :
        print("only 1 2")
else :
    print("only number")





    
print("****************************************************************")
# write code with GPT
num = input("Enter a number: ")

if num.isdigit():
    num = int(num)
    if num == 1 :
        print("som")
    elif num == 2 :
        print("tue")
    else :
        print("only 1 2")
else :
    print("only number")
    
print("=====================================================")


# In[ ]:





# In[ ]:





# In[ ]:


# https://pynative.com/python-basic-exercise-for-beginners/


# In[4]:


"""Exercise 1: Calculate the multiplication and sum of two numbers
(Given two integer numbers, return their product only if the product is equal to 
 or lower than 1000. Otherwise, return their sum.)"""

num1 = int(input("num1:-"))
num2 = int(input("num2:-"))

mul = num1 * num2
summ = num1 + num2


if mul >= 1000 :
    print ("Multiply is num1 ",num1 ,"num2",num2,"=",mul)
else :
    print("Sum is nul",num1,"num2",num2,"=",summ)
    



# In[ ]:


# https://csiplearninghub.com/python-if-else-conditional-statement-practice/#google_vignette


# In[ ]:


# Bank Program
print('''
 1 Chaque Your Balance
 2 Change Your Pin
 3 Print Your Bank Dairy
 4 Give Your Feedback
      ''')
num = int(input("enter num"))

if num == 1 :
    print("Your Balance is 5000")
elif num == 2 :
    print("Enter New pin")
elif num == 3 :
    print("Enter Your Bank Dairy")
elif num == 4 :
    print("Enter Your Feed Back")
    fd = int(input('''
                   1 is Poor
                   2 is Good
                   3 is very Good
                   4 Best
                 '''))
    if fd == 1 :
        print("Your Raitng is Poor")
    elif fd == 2 :
        print("Raitng is Good")
    elif fd == 3 :
        print("Your Raitng is very Good")
    elif fd == 4 :
        print("Your Raitng is Best")
    
    
    
    
    


# In[3]:


# Write a program to check whether a person is eligible for voting or not

age = int(input("Enter age : -"))

if age >= 21 :
    print("Eligible for Vote")
else :
    print(" No Eligible For Vote ")


# In[5]:


# Write a program to check whether a number entered by user is even or odd

num = int(input("Enter num : -"))

if num % 2 == 0 :
    print("Even number is:-",num)
else : 
     print("Odd number is:-",num)


# In[7]:


# write a program to check whether a number is divisible by 7 or not
num = int(input("Enter num : -"))

if num % 7 == 0 :
    print("Divisible This number")
else :
    print("No Divisible This number")


# In[9]:


# write a program to display "Hello "if a number entered by user is a multipal of five
num = int(input("Enter num : -"))

if num % 5 == 0 :
    print("Divisible This number")
else :
    print("No Divisible This number")



# In[14]:


""" write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria
Unit                                    Price                    
first 100  units                          no charge
next  100  units                          Rs 5 per unit
After 200  units                          Rs 10 per unit
(For example if inuput unit is 350 than total bill amount is Rs 2000) """

unit = int(input("unit"))

if unit <= 100 :
    print("no Charge")
elif unit >= 100  and unit < 200 :
    print("per unit charge is 5, Total Charge is :-",unit * 5)
else :
    print ("per unit change is 10, total Charge is :-",unit * 10)


# In[16]:


# write a program to display the last digit of a number (hint:any number % 10 will return the last digit)

num =  int(input("num : -"))

num = num / 10 
print("number will be return only 10 % ",num)


# In[19]:


# write a program to check whether the last digit of a number(entered by user is divisible by 3 or not)

num = int(input("num:-"))

a = num % 10

if a % 3 == 0 :
    print("last number is Divisible of 3 and last number is ",a)
else :
    print("Not Divisible")


# In[ ]:


# Python if else Statement Practice Test 2


# In[3]:


""" Write a program to accept percentage from the user and display the grade according to the following criteria
 mark                                         Grade
 > 90                                          A
 > 80  and <= 90                               B
 >=60  and < 80                                C
 below 60                                      D   """

num = int(input("num : -"))

if num > 90 and  num <= 100 :
    print("Grade is :- A")
elif num > 80 and num <= 90 :
     print("Grade is :- B")
elif num >= 60 and num <= 80 :
     print("Grade is C")
elif num < 60 :
     print("Grade is :-  {} D".format(num))
else :
    print("Not Valid number")


# In[8]:


# """Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria
  Cost price (in Rs)                                    Tax      
    >100000                                              15 %
    >50000 and <=100000                                  10%
    <= 50000                                             5%      """

amount = int(input("Amount :-"))

if amount > 100000 : 
    print ("you tax is 15% is ",amount * 15/100 ,"total is ", amount * 15/100 + amount )
elif amount > 50000 and amount <= 100000 :
    print ("you tax is 10% is ",amount *10 /100,"total is ", amount * 10/100 + amount )
elif amount <= 50000 :
    print ("you tax is 5%  is ",amount * 5 / 100,"total is ", amount * 5/100 + amount )


# In[10]:


# write a program to check whether an years is leap year or not
year = int(input("year : -"))

if year % 400 == 0 and year % 100 ==0 :
    print("leap Year")
elif year % 4 == 0 and year % 100 != 0 :
    print("leap year")
else :
    print("Not leap Year")


# In[17]:


# write a program to accept a mumber from 1 to 7 and display the name of the day like 1 for Sunday,2 for Monday and so on.
# ===================================
# Not :- String dal di to

# ==================================

day = int(input("Day_name :-"))
if day == 1 :
    print("Monday")
elif day == 2 :
    print("Tuesday")
elif day == 3 :
    print("Wednesday")
elif day == 4 :
    print("Thursay")
elif day == 5 :
    print("Friday")
elif day == 6 :
    print("Saturday")
elif day == 7 :
    print("Sunday")
else :
    print("Not Valid Opetion")


# In[ ]:





# In[ ]:





# In[2]:


"""write a program to accept a number from 1 to 12 and display name of the month and days in that month like
   1 fro january and number of day 31 and so . """

m = int(input("Month_name:-"))

if  m  == 1 :
    print("month_name is January and in day 31 ")
elif m == 2 :
     print("month_name is February and in day 29 ")
elif m == 2 :
     print("month_name is February and in day 31 ")
elif m == 3 :
     print("month_name is March and in day 31 ")
elif m == 4 :
     print("month_name is April and in day 30 ")
elif m == 5 :
     print("month_name is May and in day 31 ")
elif m == 6 :
     print("month_name is June and in day 30 ")
elif m == 7 :
     print("month_name is july and in day 31 ")
elif m == 8 :
     print("month_name is August and in day 31 ")
elif m == 9 :
     print("month_name is Septmember and in day 30 ")
elif m == 10 :
     print("month_name is October and in day 31 ")
elif m == 11 :
     print("month_name is November and in day 30 ")
elif m == 12 :
     print("month_name is December and in day 31 ")
else :
    print("Not Valid Number")


# In[5]:


city = input("city_name ( Delhe,Agra,Jaipure )")


if city == "Delhe" :
    print("Red Fort")
elif city == "Agra" :
    print("Taj Mahal")
elif city == "Jaipure" :
    print("Jal Mahar")
else :
    print("Worng Type Opetion Type only (Delhe,Agra,Jaipure) ")


# In[ ]:


test 3


# In[9]:


# write a program to check whether a number entered is three digit number not

num = input("num")

if num == 3 :
    print("number is 3 digit")
else :
    print("Not 3 digit")


# In[ ]:


# write a program to check whether a persom is elgible for woting or not


# In[ ]:


# write a program to check whether a person is senior citizen or not


# In[11]:


# write a program to find the lowest number out of two numbers excepted from user

num1 = int(input("num1:-"))
num2 = int(input("num2:-"))

if num1 > num2 :
    print("num1 is large",num1)
else :
    print("num2 is large",num2)


# In[15]:


# write a program to check whether a number (accepted from user) is positive or nagative

num = int(input("num :-"))

if num >= 0 :
    print("num is positive")
else :
    print("num is nagative")


# In[ ]:


# write a program to check whether a number is even or odd


# In[21]:


# write a program to whether a number (accepted from user) is divisible by 2 and 3

num = int(input("num:-"))

if num % 2 == 0 and num % 3 == 0 :
    print("num {} is 2 and 3 divisible".format(num))
else :
    print("num {} is not divisible".format(num))


# In[ ]:


# write a program to find the largest number out of three numbers excepted from user


# In[24]:


num1 =int(input("1:-"))
num2 =int(input("2:-"))
num3 =int(input("3:-"))

if num1 > num2 and num1 and num > num3 :
    print("num1 is grether",num1)
elif num2 > num3 :
    print("num2 is grether",num2)
else :
    print("num3 is grether",num3)


# In[ ]:


test 4


# In[3]:


# Accept the temperature in degree Celsius of water and check whether it is boiling or not (boiling point of water in 100 c)

temp = int(input('temp'))
if temp >= 100 :
    print('water is boiling')
else : 
    print('not Boiling water')


# In[11]:


# Accept the age of 4 people and display the oldest one
a = int(input("num:-1"))
b = int(input("num:-2"))
c = int(input("num:-3"))
d = int(input("num:-4"))

if a > b and a > c and a > d :
    print('a is largest',a)
elif b > a and b > c and b > d :
    print('b is largest')
elif c > a and c > b and c > d :
    print(' c is largest')
else :
    print('d is largest')


# In[ ]:


# Accept the age of 4 people and display the youngest one
a = int(input("num:-1"))
b = int(input("num:-2"))
c = int(input("num:-3"))
d = int(input("num:-4"))

if a < b and a < c and a < d :
    print('a is youngest',a)
elif b < a and b < c and b < d :
    print('b is youngest')
elif c < a and c < b and c < d :
    print(' c is youngest')
else :
    print('d is youngest')


# In[ ]:


# write a program to check whether a number is prime or not
num = int(input()


# In[ ]:


# write a program to check a character is vovel or not


# In[ ]:


test 5


# In[ ]:


# accept the following from the user and calculate the percentage of class attended:
1 question


# In[3]:


""" accept the percentage from the user and display the grade according to the following criteria:
below 25============= D
25 to 45 =============C
45 to 50 =============B
50 to 60 =============B+
60 to 80 =============A
above 80 =============A+        """


num = int(input("number"))

if num < 25 :
    print("Your Number is {} Grade is :- D ".format(num))
elif num > 25 and num < 45 :
        print("Your Number is {} Grade is :- C ".format(num))
elif  num > 45 and num < 50 :
        print("Your Number is {} Grade is :- B ".format(num))
elif  num > 50 and num < 60 :
        print("Your Number is {} Grade is :- B+ ".format(num))
elif num > 60 and num < 80 :
    print("Your Number is {} Grade is :- A ".format(num))
elif num > 80 :
    print("Your Number is {} Grade is :- A+ ".format(num))
else :
    print("Not Valid number")
          


# In[8]:


"""a company decided to give bonus to employee according to following ceiteria
Time period of Service              Bonus
More than 10 year                   10 %
>=6 and <=10                        8 %
less than 6 year                    5 %            """

year = int(input("Ener Year :-"))

if year > 10 :
    print("Your Bonus is :- 10 %" )
elif year >= 6 and year <= 10 :
    print("Your Bonus is :- 8 %")
else :
    print("Your Bonus is :- 5 %")


# In[30]:


# accept to marked price from the user and calculate the Net amount as (Marked Price- Discount) to pay according to following criteria:
    
price = int(input("Enter Market Price :-"))

if price > 10000 :
    dis = price / 100 * 20
    print("Your price is {} Your discont is {} and Pay amount{}".format(price, dis,price - dis))
elif price > 7000 and price <= 10000 :
    dis = price / 100 * 15
    print("Your price is {} Your discont is {} and Pay amount{}".format(price, dis,price - dis))
else :
    dis = price / 100 * 10
    print("Your price is {} Your discont is {} and Pay amount{}".format(price, dis,price - dis))


# In[33]:


"""write a program to accept percentage and display the Category according to the following criteria:
percentage                           Category
< 40                                   Failed
>= 40 and < 50                         Fair
>= 55 and < 65                         Good
>= 65                                  Excellent   """

num = int(input("Ener number :-"))

if num < 40 :
    print("Faild")
elif num >= 40 and num < 55 :
    print("Fair")
elif num >= 55 and num < 65 :
    print("Good")
elif num >= 65  and num < 100 :
    print("Excellent")


# In[ ]:


# 6 accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle
=============================================


# In[36]:


# write a program to accept two numbers and mathematical operators and perform accordingly
first = int(input("Enter First Number"))
secound = int(input("Enter secound Number "))
oper = input("Enter Operator")

if oper == "+" :
    print("Sum ",first + secound)
elif oper == "-" :
    print("Subtract ",first - secound)
elif oper == "*" :
    print("Multiply ",first * secound)
elif oper == "/" :
    print("Divisible ",first / secound)
else :
    print("Not Valid Operator")


# In[44]:


""" Accept the age,sex (M,F) number of days and display the wages accordingly
Age                                 Sex        wage/Day
>= 18 and < 30                       "M"          700
                                     "F"          750
>= 30 and <= 40                      "M"          800
                                     "F"          850          """

age = int(input("Age:-"))
gender = input("m/f:-")
Day = int(input("Day:-"))

if age >= 18 and  age < 30 and gender == "m" :
    print("age{} gender {} and wage/day one 700 toata {}".format(age,gender,Day *700))
elif age >= 18 and  age < 30 and gender == "f" :
    print("age{} gender {} and wage/day 700 toata {}".format(age,gender,Day *750))    
elif age >= 30 and  age < 40 and gender == "m" :
    print("age{} gender {} and wage/day 800 toata {}".format(age,gender,Day *800))
elif age >= 30 and  age < 40 and gender == "f" :
    print("age{} gender {} and wage/day 850 toata {}".format(age,gender,Day *850))
else :
    print("Not valid Age and gender")

    


# In[ ]:


test 6


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# https://community.edyoda.com/t/ds010923-practice-questions-based-on-conditional-statements/9647


# In[ ]:


# https://pythonistaplanet.com/examples-of-conditional-statements-in-python/


# In[ ]:


# https://www.analyticsvidhya.com/blog/2021/08/python-if-else-conditional-statements/


# In[ ]:


# 100 python program cumpas x

