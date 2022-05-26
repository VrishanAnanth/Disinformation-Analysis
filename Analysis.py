#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


a = pd.read_excel('Sentiment_Analysis_1.xlsx')
data = pd.read_csv("disinformation_full_1.csv")
types=[]
for i in a['Sources of News']:
    b=i.split(',')
    types.append(len(b))
a['Number of News Sources']=types


# In[116]:


## STRONG RESULTS##

#a.groupby('Age')[['Frequency of sharing news']].mean().loc[['Less than 18 years','18 to 30 years','31 to 45 years','45 to 60 years', 'More than 60 years']].plot.barh()

#a.groupby('Age')['Verify authenticity of news'].mean().loc[['Less than 18 years','18 to 30 years','31 to 45 years','45 to 60 years', 'More than 60 years']].plot.barh()
#plt.legend(loc=(1.04,0))
#plt.show()


# In[4]:


print(data.columns)


# In[19]:


dark=[]
for i in (data['Money1 or 2']):
    if i =='B':
        dark.append(-1)
    elif i == 'A':
        dark.append(1)
    else:
        dark.append(0)
data['Image Formatted/Plain']=dark


# In[21]:


data.groupby('Age')[['Image Formatted/Plain']].mean().loc[['Less than 18 years','18 to 30 years','31 to 45 years','45 to 60 years', 'More than 60 years']].plot.barh()
plt.xlabel('Likelihood Scale')
plt.legend(loc=(1.04,0))
plt.show()


# In[139]:


bel=[]
fai=[]

for i in a.columns:
    if 'Faith' in i:
        fai.append(i)
    elif 'Believability' in i:
        bel.append(i)


# In[140]:


for i in range(len(bel)):
    (a.groupby('Age')[[bel[i],fai[i]]].mean().loc[['Less than 18 years','18 to 30 years','31 to 45 years','45 to 60 years', 'More than 60 years']].plot.barh())
    plt.xlabel('Likelihood Scale')
    plt.legend(loc=(1.04,0))
    plt.show()


# In[126]:





# In[128]:


for i in range(4):
    (a.groupby('Age')[[pm[i],who[i],doc[i]]].mean().loc[['Less than 18 years','18 to 30 years','31 to 45 years','45 to 60 years', 'More than 60 years']].plot.barh())
    plt.xlabel('Likelihood Scale')
    plt.legend(loc=(1.04,0))
    plt.show()


# In[63]:


for i in range(3):
    (a.groupby('Age')[[fact[i],fact1[i]]].mean().loc[['Less than 18 years','18 to 30 years','31 to 45 years','45 to 60 years', 'More than 60 years']].plot.barh())
    plt.xlabel('Likelihood Scale')
    plt.legend(loc=(1.04,0))
    plt.show()


# In[69]:


fake1=[]
fake2=[]
for i in fake:
    if '1' in i:
        
        fake1.append(i)
    else:
        fake2.append(i)
        
for i in range(3):
    (a.groupby('Age')[[fake1[i],fake2[i]]].mean().loc[['Less than 18 years','18 to 30 years','31 to 45 years','45 to 60 years', 'More than 60 years']].plot.barh())
    plt.xlabel('Likelihood Scale')
    plt.legend(loc=(1.04,0))
    plt.show()


# In[71]:


print(trust)
trust1=[]
trust2=[]
for i in trust:
    if '1' in i:
        
        trust1.append(i)
    else:
        trust2.append(i)
        
for i in range(3):
    (a.groupby('Age')[[trust1[i],trust2[i]]].mean().loc[['Less than 18 years','18 to 30 years','31 to 45 years','45 to 60 years', 'More than 60 years']].plot.barh())
    plt.xlabel('Likelihood Scale')
    plt.legend(loc=(1.04,0))
    plt.show()

