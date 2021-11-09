#!/usr/bin/env python
# coding: utf-8

# #importing libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1.Read the data set
# 

# dataset=pd.read_excel('iris1.xls')

# 2.Display the columns in  the data

# In[13]:


dataset.columns


# 3.Mean of each column of dataset

# In[15]:


dataset.mean(axis=0)


# 4.Check for null values

# In[16]:


dataset.isnull()


# 5.Meaningful visualizations using the dataset

# In[20]:



x_axis=[]
x_axis=dataset.columns
x_axis


# In[22]:


x=x_axis.drop('Classification')


# In[23]:


y_axis=[]
y_axis=dataset.mean(axis=0)
y_axis


# In[24]:


plt.plot(x,y_axis)
plt.title('Mean values')
plt.xlabel('x')
plt.ylabel('y')


# In[27]:


dataset['Classification'].value_counts()


# Using pairplot

# In[28]:


sns.pairplot(dataset, hue = 'Classification')


# Using violin plot

# In[33]:


sns. violinplot( x ='SL', y ='Classification', data=dataset, inner = 'quartile')


# In[34]:


sns.violinplot(x='SW',y='Classification',data=dataset,inner='quartile')


# In[ ]:




