# # Police Dataset
# #The data is from a Police Checkpost
# 
# #Q1: Remove the column that only contains missing Values#Police Datasett
 # In[2]:
import pandas as pd

# In[3]:
data = pd.read_csv(r"E:\Police Dataset for Project.csv")

# In[4]:
data

# In[7]:
data.isnull().sum()

# In[6]:
data.drop(columns = 'country_name', inplace = True)

# In[ ]:
#Q2: For Speeding, were Men or Women stopped more often?
# In[8]:
data.head()

# In[9]:
data[data.violation == 'Speeding'].driver_gender.value_counts()

# In[ ]:
#Q3: Does gender affect who gets searched during a stop? 

# In[10]:
data.head()

# In[11]:
data.groupby('driver_gender').search_conducted.sum()

# In[12]:
data.search_conducted.value_counts()

# In[ ]:
#Q4: What is the mean of stop_duration column?

# In[13]:
data.stop_duration.value_counts()

# In[14]:
data['stop_duration']= data['stop_duration'].map( {'0-15 Min' : 7.5, '16-30 Min' : 24, '30+ Min' : 45})

# In[16]:
data['stop_duration'].mean()

# In[15]:
data

# In[ ]:
#Q5: Compare the age distributions for each violation

# In[17]:
data.groupby('violation').driver_age.describe()

