#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import re
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff

warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df=pd.read_csv('E:/Data Analyst/Project/netflix_titles.csv')


# In[8]:


df.head()


# In[12]:


df.tail()


# In[15]:


df.shape


# In[18]:


df.columns


# In[19]:


df.info()


# In[20]:


df.describe()


# # inspect misssing values in the Dataset

# In[26]:


df.isnull().sum().sort_values(ascending=False)


# In[28]:


df['director'].value_counts().head(10)


# # Movies vs Tv Shows

# In[1]:


go.Figure(data=[go.Pie(labels=df.value_counts(normalize=True).index,
values=df.type.value_counts(normalize=True).values, hole=.5,
title='Movie Vs TV Shows')])


# In[41]:


df.type.value_counts()


# In[42]:


df.rating.value_counts()


# In[48]:


sns.barplot(x=df.rating.value_counts(), y=df.rating.value_counts().index, data=df,orient='h')
plt.show()


# In[50]:


df.country.value_counts().head(10)


# # Year wise Count

# In[53]:


plt.figure(figsize=(12,10))
ax= sns.countplot(y='release_year',data=df, order=df.release_year.value_counts().index[0:15])
                     


# Highest Release in 2018 followed by 2017 and 2019

# In[55]:


df.listed_in.value_counts().head(10)


# In[60]:


plt.figure(figsize=(12,10))
ax=sns.countplot(y='listed_in',data=df,order=df.listed_in.value_counts().index[0:15])


# # Handling missing values

# In[65]:


round(df.isnull().sum()/df.shape[0]*100,2).sort_values(ascending=False)


# In[67]:


round(df.isnull().sum())


# In[69]:


df.cast.value_counts().head(10)


# In[71]:


### replace missing values in a cast with "No cast"
df['cast'].replace(np.NaN,'No Cast',inplace=True)


# In[76]:


### replace missing values Director with "No Director"
df['director'].replace(np.NAN,'No Director',inplace=True)


# In[77]:


round(df.isnull().sum()/df.shape[0]*100,2).sort_values(ascending=False)


# In[78]:


df['title']


# In[88]:


cast_shows=df[df.cast!='No Cast'].set_index('title').cast.str.split(',', expand=True).stack().reset_index(level=1),drop=True
plt.figure(figsize=(13,7))
plt.title('Top 10 Actor Movies based on the no.of titles')
sns.countplot(y=filtered_cast_shows, order=cast_shows.value_counts().index[:10],palette='pastel')
plt.show()


# 

# In[94]:


movies_df= df.loc[(df['type']=='Movie')]
movies_df


# In[10]:


shows_df= df.loc[(df['type']=='TV Show')]
shows_df


# In[ ]:





# In[ ]:




