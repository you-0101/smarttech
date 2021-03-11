#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import xlrd


# In[4]:


import os


# In[5]:


import math


# In[6]:


from statsmodels.tsa.holtwinters import SimpleExpSmoothing


# In[7]:


from statsmodels.tsa.holtwinters import Holt


# In[8]:


from statsmodels.tsa.holtwinters import ExponentialSmoothing


# In[9]:


from scipy.stats import linregress


# In[10]:


df=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\6_Forecasting_Data.xlsm',sheet_name='Timeseries')


# In[11]:


data = df['Demand']


# In[12]:


xgo = df['t']


# In[13]:


data1=data.astype('float64')


# In[14]:


ses = SimpleExpSmoothing(data).fit()


# In[15]:


data2=ses.forecast(12)


# In[49]:


data2


# In[16]:


ses.sse


# In[17]:


for i in range(12):
    data1[i+36]=data2[i+36]


# In[18]:


data1.plot(style='--',marker='o',color='blue')


# In[19]:


linregress(x=xgo,y= data)


# In[20]:


linregress(x=xgo,y= data).pvalue


# In[21]:


hz= ExponentialSmoothing(data,trend='add').fit()


# In[22]:


hz.params


# In[23]:


print(hz.level[0], hz.slope[0])


# In[24]:


data3=data.astype('float64')


# In[25]:


data4=hz.forecast(12)


# In[55]:


data4


# In[26]:


for i in range(12):
    data3[i+36]=data4[i+36]


# In[27]:


data3.plot(style='-',color='blue')


# In[28]:


df['resid']=hz.resid


# In[50]:


df['resid']


# In[29]:


from statsmodels.tsa.stattools import acf


# In[30]:


from statsmodels.graphics.tsaplots import plot_acf


# In[31]:


plot_acf(df['resid'],lags=12)


# In[32]:


acf(x=hz.resid,nlags=12)


# In[33]:


from statsmodels.tsa.holtwinters import ExponentialSmoothing


# In[34]:


data5=data.astype('float64')
smooth=[i*i for i in range(30)]
average1=0
average2=0
half=0


# In[35]:


for i in range(24):
    for j in range(12):
        average1=data5[i+j]+average1
        average2=data[i+j+1]+average2
    half=((average1/12)+(average2/12))/2
    smooth[6+i]=half
    average1=0
    average2=0


# In[36]:


real_smooth=[]
for k in range(6,30):
    real_smooth.append(smooth[k])


# In[54]:


real_smooth


# In[37]:


import matplotlib.pyplot as plt


# In[38]:


x = np.arange(6,30)
plt.plot(data5,label='Demand')
plt.plot(x,real_smooth,label='Smooth')
plt.legend(loc='upper right')
plt.show()


# In[39]:


season =[i for i in range(30)]


# In[40]:


for i in range(6,30):
    season[i]=(data5[i]/smooth[i])


# In[51]:


season


# In[41]:


ini_season=[]
ini_season.append((season[12]+season[24])/2)
ini_season.append((season[13]+season[25])/2)
ini_season.append((season[14]+season[26])/2)
ini_season.append((season[15]+season[27])/2)
ini_season.append((season[16]+season[28])/2)
ini_season.append((season[17]+season[29])/2)
ini_season.append((season[6]+season[18])/2)
ini_season.append((season[7]+season[19])/2)
ini_season.append((season[8]+season[20])/2)
ini_season.append((season[9]+season[21])/2)
ini_season.append((season[10]+season[22])/2)
ini_season.append((season[11]+season[23])/2)


# In[42]:


for i in range(2):
    for j in range(12):
        ini_season.append(ini_season[j])


# In[52]:


ini_season


# In[43]:


deseason=[i for i in range(36)]
for i in range(36):
    deseason[i]=data5[i]/ini_season[i]


# In[44]:


deseason


# In[45]:


Seas = ExponentialSmoothing(data5, trend= 'add',seasonal= 'mul',seasonal_periods=12).fit()


# In[46]:


Seas.params


# In[47]:


data6=Seas.forecast(12)


# In[53]:


data6


# In[48]:


x = np.arange(36,48)
plt.plot(data5)
plt.plot(x,data6,'o''--''b',label='None')
plt.legend(loc='upper left')
plt.show()


# In[ ]:




