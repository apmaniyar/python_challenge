
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


csvpath1 = "/Users/arjun.maniyar/Documents/Project Files/GWAR201802DATA4-Class-Repository-DATA/02-Homework/03-Python/Instructions/PyBank/raw_data/budget_data_1.csv"
csvpath1_pd = pd.read_csv(csvpath1)
csvpath1_pd.head()


# In[3]:


csvpath2 = "/Users/arjun.maniyar/Documents/Project Files/GWAR201802DATA4-Class-Repository-DATA/02-Homework/03-Python/Instructions/PyBank/raw_data/budget_data_2.csv"
csvpath2_pd = pd.read_csv(csvpath2)
csvpath2_pd.head


# In[4]:


frames = [csvpath1_pd, csvpath2_pd]


# In[5]:


mergecsv = pd.concat(frames)
mergecsv.head()


# In[6]:


print("The total number of months is " + str(len(mergecsv) + 1))


# In[7]:


revenue = mergecsv['Revenue'].sum()


# In[8]:


print("The total revenue was "+ "$" + str(revenue))


# In[9]:


ave_change = revenue/(len(mergecsv) + 1)


# In[10]:


print ("The average change over the entire period was " + "$" + str(ave_change))


# In[11]:


mergecsv["Difference"] = mergecsv["Revenue"].shift(1) - mergecsv["Revenue"].shift(0)
mergecsv.head


# In[12]:


new_low = mergecsv.sort_values("Difference")

new_low.head


# In[13]:


worst = new_low.iloc[:1]
print("Here is some data on greatest month-over-month decrease:" + str(worst))


# In[14]:


new_high = new_low.iloc[::-1]
new_high


# In[15]:


single_high = new_high.iloc[1:2]
single_high


# In[16]:


print("Here is some data on greatest month-over-month increase:" + str(single_high))

