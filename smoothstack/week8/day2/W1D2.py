#!/usr/bin/env python
# coding: utf-8

# # Day 2 Exercises

# ## 1. Numbers: Example code to add two numbers 50+50 and 100-10 and print it.

# In[1]:


print(50 + 50)


# In[2]:


print(100-10)


# ## 2. 30+*6,6^6,6**6,6+6+6+6+6+6

# In[3]:


print(30+6,6^6,6*6,6+6+6+6+6+6)


# ## 3. Print “Hello World” on the console output. Print output “Hello World : 10”
# 

# In[4]:


print("Hello World")
print("Hellow World : 10")


# ## 4. mortgage 

# In[52]:


r = 6
p = 800000
l = 103

r1 = 0.06
i = (r1/12)
i1 = (1+i)**l

m = int((p*i*i1)/(i1-1))

print("input data: ")
print(r,p,l)
print("answer: ")
print(m)




