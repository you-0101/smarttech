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


df=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\5_Naive Bayes_Data.xlsx',sheet_name='AboutMandrillApp')


# In[7]:


df2=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\5_Naive Bayes_Data.xlsx',sheet_name='AboutOther')


# In[8]:


df['lower']=df.Tweet.str.lower()


# In[9]:


df2['lower']=df2.Tweet.str.lower()


# In[10]:


app = []
replace_app =[]


# In[11]:


other =[]
replace_other=[]


# In[12]:


for j in range(df.shape[0]):
    app.append(df.iloc[j]['lower'])
    


# In[13]:


for j in range(df2.shape[0]):
    other.append(df2.iloc[j]['lower'])


# In[14]:


for j in range(df.shape[0]):
    replace_app.append(app[j].replace(". "," ").replace(": "," ").replace("?"," ").replace("!"," ").replace(","," ").replace(";"," "))


# In[15]:


for j in range(df2.shape[0]):
    replace_other.append(other[j].replace(". "," ").replace(": "," ").replace("?"," ").replace("!"," ").replace(","," ").replace(";"," "))


# In[16]:


app_token=[]


# In[17]:


other_token=[]


# In[18]:


for j in range(df.shape[0]):
    app_token.append(replace_app[j].split(" "))


# In[19]:


for j in range(df2.shape[0]):
    other_token.append(replace_other[j].split(" "))


# In[20]:


real_app_token=[]


# In[21]:


real_other_token=[]


# In[22]:


for i in range(df.shape[0]):
    for j in range(len(app_token[i])):
        if len(app_token[i][j])>3 :
            real_app_token.append(app_token[i][j])


# In[23]:


for i in range(df2.shape[0]):
    for j in range(len(other_token[i])):
        if len(other_token[i][j])>3 :
            real_other_token.append(other_token[i][j])


# In[24]:


app_cout_token ={ }


# In[25]:


other_cout_token={ } 


# In[26]:


for lst in real_app_token:
    try: app_cout_token[lst] +=1
    except: app_cout_token[lst] =1


# In[27]:


for lst in real_other_token:
    try: other_cout_token[lst] +=1
    except: other_cout_token[lst] =1


# In[28]:


total=len(app_cout_token)+len(real_app_token)


# In[29]:


total2=len(other_cout_token)+len(real_other_token)


# In[30]:


from pandas import DataFrame


# In[31]:


new_df=DataFrame([app_cout_token],index=['num'])


# In[32]:


new2_df=DataFrame([other_cout_token],index=['num'])


# In[33]:


new_df.loc['num+1']=new_df.loc['num']+1


# In[34]:


new2_df.loc['num+1']=new2_df.loc['num']+1


# In[35]:


new_df.loc['percent']=new_df.loc['num+1']/total


# In[36]:


new2_df.loc['percent']=new2_df.loc['num+1']/total2


# In[37]:


new_df.loc['LN']=np.log(new_df.loc['percent'])


# In[38]:


new2_df.loc['LN']=np.log(new2_df.loc['percent'])


# In[39]:


df3=pd.read_excel(r'C:\Users\HyunSeok\Desktop\air\5_Naive Bayes_Data.xlsx',sheet_name='TestTweets')


# In[40]:


df3['lower']=df3.Tweet.str.lower()


# In[41]:


test =[]
replace_test=[]


# In[42]:


for j in range(df3.shape[0]):
    test.append(df3.iloc[j]['lower'])


# In[43]:


for j in range(df3.shape[0]):
    replace_test.append(test[j].replace(". "," ").replace(": "," ").replace("?"," ").replace("!"," ").replace(","," ").replace(";"," "))


# In[44]:


test_token=[]


# In[45]:


for j in range(df3.shape[0]):
    test_token.append(replace_test[j].split(" "))


# In[46]:


real_test_token=[]
each_test_token=[]


# In[47]:


for i in range(df3.shape[0]):
    for j in range(len(test_token[i])):
        if len(test_token[i][j])>3 :
            real_test_token.append(test_token[i][j])
    each_test_token.append(real_test_token)
    real_test_token=[]


# In[48]:


app_exit_column=[]
result_app_predi =[]
isint=0


# In[49]:


for j in range  (len(each_test_token)):
    for k in range (len(each_test_token[j])):
        for i in range(len(new_df.columns)):
            if(new_df.columns[i] == each_test_token[j][k]):
                app_exit_column.append(each_test_token[j][k])
                isint=1
                break;
        if isint==0:
                app_exit_column.append(1)
        else:
            isint=0
    result_app_predi.append(app_exit_column)
    app_exit_column=[]


# In[50]:


other_exit_column=[]
result_other_predi =[]


# In[51]:


isint =0
for j in range  (len(each_test_token)):
    for k in range (len(each_test_token[j])):
        for i in range(len(new2_df.columns)):
            if(new2_df.columns[i] == each_test_token[j][k]):
                other_exit_column.append(each_test_token[j][k])
                isint=1
                break
        if isint==0:
                other_exit_column.append(1)
        else:
            isint=0
    result_other_predi.append(other_exit_column)
    other_exit_column=[]


# In[52]:


app_predi =0
other_predi =0


# In[53]:


Ending_result =[]


# In[54]:


for i in range (len(result_app_predi)):
    for j in range (len(result_app_predi[i])):
        if result_app_predi[i][j]==1:
            app_predi=app_predi+(-7.78738)
        else:
            app_predi=app_predi+new_df[result_app_predi[i][j]][3]
    for k in range (len(result_other_predi[i])):
        if result_other_predi[i][k]==1:
            other_predi=other_predi+(-7.61431)
        else:
            other_predi=other_predi+new2_df[result_other_predi[i][k]][3]

    if app_predi>other_predi:
        Ending_result.append("app")
    else:
        Ending_result.append("other")
    app_predi=0
    other_predi=0


# In[56]:


Ending_result


# In[ ]:




