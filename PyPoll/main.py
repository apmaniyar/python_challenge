
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


csvpath1 = "/Users/arjun.maniyar/Documents/Project Files/GWAR201802DATA4-Class-Repository-DATA/02-Homework/03-Python/Instructions/PyPoll/raw_data/election_data_1.csv"
csvpath1_pd = pd.read_csv(csvpath1)
csvpath1_pd.head()


# In[6]:


csvpath2 = "/Users/arjun.maniyar/Documents/Project Files/GWAR201802DATA4-Class-Repository-DATA/02-Homework/03-Python/Instructions/PyPoll/raw_data/election_data_2.csv"
csvpath2_pd = pd.read_csv(csvpath2)


# In[7]:


frames = [csvpath1_pd, csvpath2_pd]


# In[9]:


mergecsv = pd.concat(frames)
mergecsv.head


# In[23]:


print("The total number of votes is " + str(len(mergecsv) + 1))


# In[29]:


candidate = mergecsv.Candidate.unique()
print("Candidate: "+ candidate)


# In[37]:


Vestal = mergecsv.Candidate.value_counts()["Vestal"]
print("Vestal had " + str(Vestal) + " votes")
Torres = mergecsv.Candidate.value_counts()["Torres"]
print("Torres had " + str(Torres) + " votes")
Seth = mergecsv.Candidate.value_counts()["Seth"]
print("Seth had " + str(Seth) + " votes")
Cordin = mergecsv.Candidate.value_counts()["Cordin"]
print("Cordin had " + str(Cordin) + " votes")
Khan = mergecsv.Candidate.value_counts()["Khan"]
print("Khan had " + str(Khan) + " votes")
Correy = mergecsv.Candidate.value_counts()["Correy"]
print("Correy had " + str(Correy) + " votes")
Li = mergecsv.Candidate.value_counts()["Li"]
print("Li had " + str(Li) + " votes")


# In[38]:


print("The winner of the popular vote was Khan with 2218231 votes")

