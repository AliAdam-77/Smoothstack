#!/usr/bin/env python
# coding: utf-8

# In[32]:


bookshop= [
[34587, "Learning Python, Mark Lutz",         4, 40.95],
[98762, "Programming Python, Mark Lutz",      5, 56.80],
[77226, "Head First Python, Paul Barry",      3, 32.95],
[88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

print("\n")

print(bookshop)
print("\n")
print("\n")


# In[30]:


ans = lambda x: (x[0],(x[2],x[3]))
final = []
for i in bookshop:
    if i[3] < 100:
        i[3]+=10
    final.append(tuple(ans(i)))

        



# In[47]:


print(final)
print("\n")
print("\n")

# In[46]:


#ans1 = lambda x: (x[0],x[1][0])
final2 = []
for x in final:
    final2.append(tuple((x[0],x[1][0])))
print(final2)
print("\n")
print("\n")   


# In[ ]:




