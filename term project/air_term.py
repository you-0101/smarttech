#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import xlrd
import os
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import matplotlib.pyplot as plt
from scipy.stats import linregress


# In[2]:


df=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\중간\term project\air term.xlsx',sheet_name='seoul')
df1=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\중간\term project\air term.xlsx',sheet_name='all')
df2=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\중간\term project\air term.xlsx',sheet_name='lost')
df3=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\중간\term project\air term.xlsx',sheet_name='new')


# In[3]:


df


# In[4]:


data1=df['percent of seoul']
data2=df['dog percent']


# In[5]:


hz= ExponentialSmoothing(data1,trend='add').fit()
hz.params


# In[6]:


forecasting=hz.forecast(7)


# In[7]:


for i in range(5,12):
    df.loc[i]=np.nan
for i in range(5,12):
    df['percent of seoul'][i]=forecasting[i]


# In[8]:


x = np.arange(5,12)
plt.plot(data1,'o''--''b',label='real_percent_seoul')
plt.plot(x,forecasting,'o''--''r',label='predict_percent_seoul')
plt.legend(loc='upper left')
plt.show()


# In[9]:


hz= ExponentialSmoothing(data2,trend='add').fit()


# In[10]:


forecasting=hz.forecast(7)
for i in range(5,12):
    df['dog percent'][i]=forecasting[i]
    df['year'][i]=2014+i


# In[11]:


x = np.arange(5,12)
plt.plot(data2,'o''--''b',label='real_dog_percent')
plt.plot(x,forecasting,'o''--''r',label='predict_dog_percent')
plt.legend(loc='upper left')
plt.show()


# In[12]:


df #to show the change


# In[13]:


df1


# In[14]:


data1=df1['dog percent']
data2=df1['per house']
data3=df1['total dog']


# In[15]:


hz= ExponentialSmoothing(data1,trend='add').fit()


# In[16]:


forecasting=hz.forecast(3)


# In[17]:


for i in range(5,8):
    df1.loc[i]=np.nan
for i in range(5,8):
    df1['dog percent'][i]=forecasting[i]
df1['year'][5]=2020
df1['year'][6]=2023
df1['year'][7]=2025


# In[18]:


x = np.arange(5,8)
plt.plot(data1,'o''--''b',label='dog_percent')
plt.plot(x,forecasting,'o''--''r',label='predict_dog_percent')
plt.legend(loc='upper left')
plt.show()


# In[19]:


hz= ExponentialSmoothing(data2,trend='add').fit()


# In[20]:


forecasting=hz.forecast(3)
for i in range(5,8):
    df1['per house'][i]=forecasting[i]


# In[21]:


x = np.arange(5,8)
plt.plot(data2,'o''--''b',label='per_house')
plt.plot(x,forecasting,'o''--''r',label='predict_per_house')
plt.legend(loc='upper left')
plt.show()


# In[22]:


hz= ExponentialSmoothing(data3,trend='add').fit()


# In[23]:


forecasting=hz.forecast(3)
for i in range(5,8):
    df1['total dog'][i]=forecasting[i]


# In[24]:


x = np.arange(5,8)
plt.plot(data3,'o''--''b',label='total_dog')
plt.plot(x,forecasting,'o''--''r',label='predict_total_dog')
plt.legend(loc='upper left')
plt.show()


# In[25]:


df1 #to show the change


# In[26]:


df2


# In[27]:


data1=df2['lost animal']
data2=df2['lost dog']
data3=df2['percent of dog']
data4=df2['center number']
data5=df2['re-adoption']
data6=df2['back to home']
data7=df2['artificial- dead']


# In[28]:


hz1= ExponentialSmoothing(data1,trend='add').fit()
hz2= ExponentialSmoothing(data2,trend='add').fit()
hz3= ExponentialSmoothing(data3,trend='add').fit()
hz4= ExponentialSmoothing(data4,trend='add').fit()
hz5= ExponentialSmoothing(data5,trend='add').fit()
hz6= ExponentialSmoothing(data6,trend='add').fit()
hz7= ExponentialSmoothing(data7,trend='add').fit()


# In[29]:


forecasting1=hz1.forecast(8)
forecasting2=hz2.forecast(8)
forecasting3=hz3.forecast(8)
forecasting4=hz4.forecast(8)
forecasting5=hz5.forecast(8)
forecasting6=hz6.forecast(8)
forecasting7=hz7.forecast(8)


# In[30]:


for i in range(7,15):
    df2.loc[i]=np.nan
for i in range(7,15):
    df2['year'][i]=2011+i
    df2['lost animal'][i]=forecasting1[i]
    df2['lost dog'][i]=forecasting2[i]
    df2['percent of dog'][i]=forecasting3[i]
    df2['center number'][i]=forecasting4[i]
    df2['re-adoption'][i]=forecasting5[i]
    df2['back to home'][i]=forecasting6[i]
    df2['artificial- dead'][i]=forecasting7[i]


# In[31]:


df2 #to show the change


# In[32]:


x = np.arange(7,15)
plt.plot(data1,'o''--''b',label='lost_animal')
plt.plot(x,forecasting1,'o''--''r',label='predict_lost_animal')
plt.plot(data2,'o''--''g',label='lost_dog')
plt.plot(x,forecasting2,'o''--''y',label='predict_lost_dog')
plt.legend(loc='upper left')
plt.show()


# In[33]:


x = np.arange(7,15)
plt.plot(data3,'o''--''b',label='percent_dog')
plt.plot(x,forecasting3,'o''--''r',label='predict_percent_dog')
plt.legend(loc='upper left')
plt.show()


# In[34]:


x = np.arange(7,15)
plt.plot(data4,'o''--''b',label='center_number')
plt.plot(x,forecasting4,'o''--''r',label='predict_center_number')
plt.legend(loc='upper left')
plt.show()


# In[35]:


x = np.arange(7,15)
plt.plot(data5,'o''--''b',label='percent_re-adoption')
plt.plot(x,forecasting5,'o''--''r',label='predict_percent_re-adoption')
plt.plot(data6,'o''--''g',label='percent_back to home')
plt.plot(x,forecasting6,'o''--''y',label='predict_percent_back to home')
plt.plot(data7,'o''--''k',label='percent_artificial dead')
plt.plot(x,forecasting7,'o''--''c',label='predict_percent_artificial dead')
plt.legend(loc='upper left')
plt.show()


# In[36]:


df3


# In[37]:


data1=df3['new']
data2=df3['lost']


# In[38]:


hz1= ExponentialSmoothing(data1,trend='add').fit()
hz2= ExponentialSmoothing(data2,trend='add').fit()


# In[39]:


forecasting1=hz1.forecast(7)
forecasting2=hz2.forecast(7)


# In[40]:


for i in range(4,11):
    df3.loc[i]=np.nan
for i in range(4,11):
    df3['year'][i]=2015+i
    df3['new'][i]=forecasting1[i]
    df3['lost'][i]=forecasting2[i]


# In[41]:


x = np.arange(4,11)
plt.plot(data1,'o''--''b',label='new')
plt.plot(x,forecasting1,'o''--''r',label='predict_new')
plt.plot(data2,'o''--''g',label='lost')
plt.plot(x,forecasting2,'o''--''y',label='predict_lost')
plt.legend(loc='upper left')
plt.show()


# In[42]:


df3 #to show the change


# In[44]:


df2['number of dog(artificial dead)']=df2['lost dog']/100
df2['number of dog(artificial dead)']=df2['number of dog(artificial dead)']*df2['artificial- dead']


# In[46]:


df2['number of dog(artificial dead)']


# In[ ]:





# In[ ]:




