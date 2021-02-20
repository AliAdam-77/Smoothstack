#!/usr/bin/env python
# coding: utf-8
import re

# # Coding Exercise 3:

# ## 1. Write a string that returns just the letter ‘r’ from ‘Hello World’
# #### For example, ‘Hello World’[0] returns ‘H’.You should write one line of code. Don’t assign avariable name to the string.

# In[3]:


print("Hello World"[8])


# ## 2. String slicing to grab the word ‘ink’ from the word ‘thinker’
# #### S=’hello’,what is the output of h[1]

# In[4]:


print("thinker"[2:5])


# In[6]:


s= 'hello'
print(s[0])


# ## 3. S=’Sammy’ what is the output of s[2:]”

# In[7]:


S = "sammy"
print(S[2:])


# ## 4. With a single set function can you turn the word ‘Mississippi’ to distinct character word.

# In[8]:


print(set("Mississippi"))
print("\n")

# ## 5. determine, whether the phrase represents a palindrome or not.

# In[ ]:


def isPalindrome(s):
    
    s = re.sub(r"[^a-zA-Z]","",s)
    x = s.lower()
    
    
    y = x[::-1]
    
    if x == y:
        return "Y"
    else:
        return "N"


l = int(input("input:\n"))
inp = []
while(l):
    inp.append(raw_input())
    l-=1
ans = ""
for i in inp:
    ans = ans + isPalindrome(i) +" "

print("\n")
print("answer:\n")
print(ans)


# In[ ]:




