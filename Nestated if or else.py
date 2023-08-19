#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#  Nestated if or else



payment=int(input("Enter Shoping Amount : "))

if(payment<10_000):
    print("Discount 10% ")
else:
    if(payment>=10_000 and payment<20_000):
        print("Your Discount 20% ")
    else:
        if(payment>=20_000 and payment<30_000):
            print("Your Discount 30% ")
        else:
            if(payment>=30_000 ):
                print("Your Discount 40% ")

