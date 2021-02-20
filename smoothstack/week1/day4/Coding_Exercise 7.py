#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random


# In[5]:


#1.  Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
#between 1500 and 2700 (both included). Go to the editor
res = [i for i in range(1500,2701)]  # list comprehension
result = list(filter(lambda x: x%7 ==0 and x%5 == 0,res)) #filter funtion
print(result)
print("\n")


# In[15]:


#2.  Write a Python program to convert temperatures to and from celsius, fahrenheit.
#Formula : c/5 = f-32/9
print("convert 60C to F")
ans1 = lambda x: (9/5)*x + 32
print(str(ans1(60))+ "F")
print("\n")

print("convert 45F to c")
ans1 = lambda x: ((x-32)/9)*5
print(str(int(ans1(45)))+ "C")
print("\n")
      


# In[28]:


#3.  Write a Python program to guess a number between 1 to 9. Go
x = random.randrange(1,10)
notguessed = True
while (notguessed):
    y = int(input("Guess a number between 1-9: "))
    if x == y :
        notguessed= False
        print('Well guessed!')
    


# In[57]:


#4. Write a Python program to construct the following pattern, using a nested for loop.
pattern = "*"
x = 0
for i in range (1,10):
    for j in range(i,i+1):
        if j < 6:
            print(pattern*j)
        else:
            x+=2 
            print(pattern*(j-x))
            
print("\n")
        


# In[58]:


#6.  Write a Python program that accepts a word from the user and reverse it.
inp = input("Enter a word: ")
print(inp[::-1])
print("\n")


# In[76]:


#7.  Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

evenList = list(filter(lambda x : x%2 == 0 ,numbers))
even = len(evenList)
odd = len(numbers)- even
print("Numbers of even numbers %s"% even)
print("Numbers of odd numbers %s"% odd)
print("\n")


# In[77]:


#Write a Python program that prints each item and its corresponding type from the following list.
d = [1452, 11.23, 1+2j, True, "w3resource", (0, -1), [5, 12], {"class":"V","section":"A"}]
res = list(map(lambda x : type(x),d))
print(res)


# In[78]:


type(10)


# In[79]:


#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
res = ""
for i in range (0,7):
    if i == 3 or i == 6:
        continue
    else:
        res += str(i)+" "
print(res)


# In[ ]:




