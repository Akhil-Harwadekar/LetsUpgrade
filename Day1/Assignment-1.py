#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 1
# 
# ### 06/11/2020

# ### Question 1

# B]  RAINBOW
print("RAINBOW")

# ### Question 2

# In[1]:


def printName(name):
    x = name.upper()
    print(f'"{x}"')
    
printName('lets upgrade')


# ### Question 3

# In[2]:


costPrice = int(input())   #Enter the Cost Price 
sellingPrice = int(input())   #Enter the Selling Price

l='Loss'
p='Profit'
n='Neither'

if (costPrice > sellingPrice):
    print(l)
elif (costPrice < sellingPrice):
    print(p)
else:
    print(n)


# ### Question 4

# In[3]:


rupees = 80
euro = int(input())  #Enter the amount in Euro 

print(rupees*euro)  #Output in Rupees

