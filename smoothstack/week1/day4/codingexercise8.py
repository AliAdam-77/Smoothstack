#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Create a function func() which prints a text ‘Hello World’
def func():
    print("Hello World")
func()
print("\n")


# In[2]:


#2.Create a function which func1(name) which takes a value name and prints the output “Hi My name is Google’
def func1(name):
    print("Hi My name is %s"%name)
func1("Google")
print("\n")


# In[7]:


#3.Define a function func3(x,y,z) that takes three arguments x,y,z where z is true it will return x and when
#z is false it should return y . func3(‘hello’goodbye’,false)
def func3(x,y,z):
    if z :
        return x
    else:
        return y
ans = func3("hello",'goodbye',False)
print("func3('hello','goodbye',False)","=",ans)
print("\n")


# In[8]:


#4.define a function func4(x,y) which returns the product of both the values.
def func4(x,y):
    return x,y
x,y = func4(2,3)
print("func4(2,3)","=",x,y)
print("\n")


# In[10]:


#5.define a function called as is_even that takes one argument , which returns true when even values is
#passed and false if it is not.
def is_even(x):
    if x%2== 0:
        return True
    else:
        return False
res = is_even(3)
res2 = is_even(2)
print("is_even(3)","=",res)
print("is_even(2)","=",res2)
print("\n")


# In[11]:


#6.define a function that takes two arguments ,and returns true if the first value is greater than the
# value and returns false if it is less than or equal to the second.

def is_greater(x,y):
    if x > y :
        return True
    else:
        return False
ans1= is_greater(2,3)
print("is_greater(2,3)","=",ans1)
ans1= is_greater(2,2)
print("is_greater(2,2)","=",ans1)
ans1= is_greater(2,1)
print("is_greater(2,1)","=",ans1)
print("\n")

# In[14]:


#7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.\

def summ(*args):
    return sum(args)
    
x = summ(1,2,3,4)
print("summ(1,2,3,4)","=",x)
print("\n")

# In[16]:


#8.Define a function which takes arbitrary number of arguments and returns a list containing only the
#arguments that are even.
def evenList(*args):
    even = []
    for i in args:
        if is_even(i):
            even.append(i)
    return even
e = evenList(6,7,8,9,2,4,5)
print("evenList(6,7,8,9,2,4,5)","=",e)
print("\n") 
        


# In[20]:


#9.Define a function that takes a string and returns a matching string where every even letter is
#uppercase and every odd letter is lowercase

def change(s):
    res = ""
    for i,v in enumerate(s):
        if is_even(i):
            res+=v.upper()
        else:
            res+=v.lower()
    return res

        
s= "hdsfdsk"
res = change(s)
print("hdsfdsk","=",res)
print("\n")

# In[21]:


# 10.Write a function which gives lesser than a given number if both the numbers are even, but returns
# greater if one or both or odd.


# In[25]:


# 11.Write a function which takes two-strings and returns true if both the strings start with the same
# letter.
def sameFirst(x,y):
    if x[0]==y[0]:
        return True
    return False
print('sameFirst("abcd","aaaa")' ,"=",sameFirst("abcd","aaaa"))
print('sameFirst("abcd","bbbb")' ,"=",sameFirst("abcd","bbbb"))
print("\n")

# In[29]:


# 12.Given a value,return a value which is twice 
def square(l):
    for i in range(len(l)):
        l[i]= l[i]**2
    return l

l = [1,2,3,4,5,6,7]
print("square([1, 2, 3, 4, 5, 6, 7])","=",square([1,2,3,4,5,6,7]))
print("\n")

# In[27]:


# 13.A function that capitalizes first and fourth character of a word in a string.
def lastFunc(s):
    ans = ""
    for i,v in enumerate(s):
        if i == 0 or i == 3:
            ans += v.upper()
        else:
            ans += v.lower()
    return ans
print("lastFunc('abcdefg')","=",lastFunc('abcdefg'))
print("\n")

# In[ ]:




