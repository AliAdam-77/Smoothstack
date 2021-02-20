#!/usr/bin/env python
# coding: utf-8

# In[ ]:
# Underweight - 18.5
# Normal weight -18.5  25.0
# Overweight - 25.0  30.0
# Obesity - 30.0 



def checkbmi(l):
    BMI = lambda w,h : (int(w)/float(h)**2)
    ans = ""
    for w,h in l:
        x = BMI(w,h)
        if x < 18.5:
            ans+="Underweight "
        elif x >= 18.5 and x <=25.0:
            ans+="Normal "
        elif x >= 25.0 and x <=30.0:
            ans+="Overweight "
        else:
            ans+="Obese "

    return ans


# In[ ]:


l =[]
leng = int(input("Enter the length: "))
while(leng):
    x = input("Enter Weight and Height: ").split()
    l.append(tuple(x))
    leng -= 1

res = checkbmi(l)
print(res)

# In[ ]:




