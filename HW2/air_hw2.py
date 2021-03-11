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


df=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\4_Cluster Analysis_Data.xlsx',sheet_name='Transactions')


# In[6]:


df["count"]=1


# In[7]:


table=pd.pivot_table(df, index='Customer Last Name', columns='Offer #', values='count',fill_value=0,aggfunc=len)


# In[8]:


from sklearn.cluster import KMeans


# In[9]:


from sklearn.metrics import silhouette_score


# In[10]:


for i in range(0,100):
    kmeans = KMeans(n_clusters=3).fit(table)    
    if(i==0):
        sil1=silhouette_score(table,kmeans.labels_,metric='euclidean')
    else:
        sil=silhouette_score(table,kmeans.labels_,metric='euclidean')
        if(sil>sil1):
            sil1=sil


# In[11]:


for i in range(0,100):
    kmeans = KMeans(n_clusters=4).fit(table)  
    if(i==0):
        sil2=silhouette_score(table,kmeans.labels_,metric='euclidean')
        table["kmean"]=kmeans.labels_
    else:
        sil=silhouette_score(table,kmeans.labels_,metric='euclidean')
        if(sil>sil2):
            sil2=sil
            table["kmean"]=kmeans.labels_


# In[12]:


df1=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\4_Cluster Analysis_Data.xlsx',sheet_name='OfferInformation')


# In[13]:


for i in range(0,100):
    kmeans = KMeans(n_clusters=5).fit(table)    
    if(i==0):
        sil3=silhouette_score(table,kmeans.labels_,metric='euclidean')
    else:
        sil=silhouette_score(table,kmeans.labels_,metric='euclidean')
        if(sil>sil3):
            sil3=sil


# In[14]:


print("3:",sil1,  " 4:",sil2,  " 5:",sil3)


# In[15]:


table2=table


# In[16]:


table2['kmean']=table2['kmean']+1


# In[17]:


for i in range(1,33):
    table2[i]=table2[i]*(table['kmean'])


# In[18]:


sum1=[]
sum2=[]
sum3=[]
sum4=[]


# In[19]:


df1['clu1']=0
df1['clu2']=0
df1['clu3']=0
df1['clu4']=0


# In[20]:


for i in range (1,33):
    num1=0
    num2=0
    num3=0
    num4=0
    for j in range (0, 100):
        if(table2[i][j]==1):
            num1=num1+1
        if(table2[i][j]==2):
            num2=num2+1
        if(table2[i][j]==3):
            num3=num3+1
        if(table2[i][j]==4):
            num4=num4+1
    sum1.append(num1)
    sum2.append(num2)
    sum3.append(num3)
    sum4.append(num4)


# In[21]:


df1['clu1']=sum1
df1['clu2']=sum2
df1['clu3']=sum3
df1['clu4']=sum4


# In[22]:


df1


# In[ ]:




