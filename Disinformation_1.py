#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
#Install the dython package
# pip install dython


# In[13]:


# documentation for the function used: http://shakedzy.xyz/dython/
from dython.nominal import associations
data = pd.read_csv("disinformation_full.csv")
data.shape


# In[6]:


# Cramers'V for the entire dataset
associations(data, nominal_columns='all', figsize=(30, 30))


# In[7]:


# Theils's U for the entire dataset
associations(data, nominal_columns='all',theil_u=True, figsize=(30, 30))


# In[8]:


# Theils's U with clustering for the entire dataset
associations(data, nominal_columns='all',theil_u=True, clustering=True, figsize=(30, 30))


# In[14]:


data1 = pd.read_csv("disinformation_partial.csv")
data1.shape


# In[15]:


# Cramers'V for the partial dataset with trust columns
associations(data1, nominal_columns='all', figsize=(30, 30))


# In[16]:


# Theils's U for the partial dataset with trust columns
associations(data1, nominal_columns='all',theil_u=True, figsize=(30, 30))


# In[17]:


# Theils's U with clustering for the partial dataset with trust columns
associations(data1, nominal_columns='all',theil_u=True, clustering=True, figsize=(30, 30))

