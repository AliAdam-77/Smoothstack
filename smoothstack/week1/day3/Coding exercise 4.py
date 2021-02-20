#!/usr/bin/env python
# coding: utf-8

# # Coding Exercise 4:

# In[1]:


#1. Create a list with one number, one word and one float value. Display the output of the list.
l = [1,"one",1.111]
print(l)
print("\n")

# In[3]:


#2. I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.
l = [1,1,[1,2]]
print(l[2][1])
print("\n")

# In[4]:


#3. lst=[&#39;a&#39;,&#39;b&#39;,&#39;c&#39;] What is the result of lst[1:]?
lst=["&#39;a&#39;","&#39;b&#39;","&#39;c&#39;"]
print(lst[1:])
print("\n")

# In[5]:


#4. Create a dictionary with weekdays an keys and week index numbers as values.do assign dictionary to a variable
week = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
print(week)
print("\n")

# In[9]:


#5.D={‘k1’:[1,2,3]} what is the output of d[k1][1]
D={'k1':[1,2,3]}
print(D['k1'][1])
print("\n")

# In[11]:


#6. Can you create a list [1,[2,3]] into a tuple
t = tuple([1,[2,3]])
print(t)
print("\n")

# In[13]:


#7. With a single set function can you turn the word ‘Mississippi’ to distinct character word.

s = set('Mississippi')
print(s)
print("\n")

# In[14]:


#8. Can you add an element ‘X’ to the above created set
s.add("X")
print(s)
print("\n")

# In[15]:


#9. Output of set([1,1,2,3])
print(set([1,1,2,3]))
print("\n")

# ### Write a program which will find all such numbers which are divisible by 7 but are not a multipleof 5,between 2000 and 3200 (both included).

# In[16]:


x = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        x.append(i)
print(x)
print("\n")

# ### Write a program which can compute the factorial of a given numbers.

# In[19]:


x = int(input("Enter n to comupute the factorial : "))
if x == 0:
    print(1)
    print("\n")
else:
    res =1
    for i in range (x,1,-1):
        res *= i
    print(res)
    print("\n")


# ### With a given integral number n, write a program to generate a dictionary that contains (i, i * i)

# In[20]:


n = int(input("Enter the n to generate dictonary: "))
d = dict()
for i in range(n ,0,-1):
    d[i] = i*i
print(d)
print("\n")

# ### Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

# In[22]:


x = raw_input("Enter a sequence of comma-separated numbers: ")
li = x.split(",")
t = tuple(li)

print(li)
print(t)
print("\n")


# ### Define a class which has at least two methods: getString: to get a string from console input ,  printString: to print the string in upper case.

# In[24]:


class code4():
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = raw_input("enter string: ")
    def printString(self):
        print(self.s)

x = code4()
x.getString()
x.printString()


# In[ ]:




