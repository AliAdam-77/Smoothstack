#!/usr/bin/env python
# coding: utf-8

# In[156]:


import pandas as pd
import numpy as np
import re


# In[45]:


df = pd.read_csv("Salaries.csv",low_memory=False)
# Check and display the head of the DataFrame.
df.columns


# In[30]:


# Use the .info() method to find out how many entries there are.
df.info(verbose=False)


# In[61]:


# What is the average of first 10000 items in BasePay ?
df2= df.head(10000)
df3 = df2["BasePay"].astype(float)
df3.mean()


# In[109]:


# What is the highest amount of TotalPayBenefits in the dataset ?
df["TotalPayBenefits"].max()


# In[175]:


# What is the job title of JOSEPH DRISCOLL ?
df6 = df2.loc[df2["EmployeeName"] == 'JOSEPH DRISCOLL']
df6["JobTitle"].values[0]


# In[174]:


# How much does JOSEPH DRISCOLL make (including benefits)?
df6["TotalPayBenefits"].values[0]


# In[96]:


# What is the name of highest paid person (including benefits)?

df7 = df2.loc[df2["TotalPayBenefits"] == 567595.43]
df7["EmployeeName"].values[0]


# In[111]:


# What is the name of lowest paid person (including benefits)? Do you notice something
# strange about how much he or she is paid?
x = df["TotalPayBenefits"].min()
df8 = df.loc[df["TotalPayBenefits"] == x]
df8["EmployeeName"].values[0]


# In[112]:


df8["TotalPayBenefits"].values[0]


# In[177]:


# What was the average (mean) TotalPay of all employees per year? (2011-2014) ?
df9 = df.groupby("Year").mean("TotalPay")
df9


# In[119]:


# How many unique job titles are there?
df10 = df["JobTitle"]
df11 = df10.nunique()
df11


# In[151]:


# What are the top 7 most common jobs?
df10 = df["JobTitle"]
df12 =df10.value_counts()
df12.sort_values(ascending=False).head(7)


# In[259]:


# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with
# only one occurence in 2013?)
df16 = df.loc[df["Year"] == 2013]

df17= df16.groupby("JobTitle").agg("count")
df17


# In[227]:


# How many people have the word Chief in their job title? (This is pretty tricky)
df13 = df[df['JobTitle'].str.match('.*Chief.*')== True]
df14 = df13[["EmployeeName","JobTitle"]]
df14["EmployeeName"].nunique()


# In[154]:


# Is there a correlation between length of the Job Title string and Salary?


# In[ ]:


# NO

