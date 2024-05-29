#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  autots import AutoTS
import seaborn as sns


# In[11]:


df=pd.read_csv("C:\\Users\\HP\\Desktop\\AAPL.csv")
df.head()


# In[ ]:





# In[13]:


get_ipython().system('pip install autots')


# In[ ]:





# In[20]:


df=df[['Date','Close']]
df["Date"]=pd.to_datetime(df.Date)
df['Close'].plot(figsize=(12,8),title='Apple Stock',fontsize=20,label="Close Price")
plt.legend()
plt.grid()
plt.show()


# In[ ]:





# In[23]:


from autots import AutoTS
model=AutoTS(forecast_length=10,frequency='infer',
            ensemble='simple',drop_data_older_than_periods=200)
model=model.fit(df,date_col='Date',value_col='Close',id_col=None)


# In[ ]:





# In[ ]:





# In[ ]:


# from autots import AutoTs:This line imports a module called AutoTS from a library.AutoTs is a tool for automatic time
#     Series
#     frequency='infer':This parameter specifies the time ferquency of your data.'infer'means that AutoTS will try to automatically
#         ensmble=simple:The parameter specifies the type of ensemble model to use. in this case.its set to 'simple'which likely
#             means its using a basic ensmble qpproch tor combininng multiple forecating methods.
            
#             model=model.fit(data,date_col="Date",value_col="Clise",id_col=None): This line trains the forecasting 


# In[ ]:





# In[24]:


prediction =model.predict()
forecast=prediction.forecast
print("Stock Price Prediction of Apple")
print(forecast)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


=====================================================================================================================


# In[29]:


get_ipython().system(' pip install yfinance')


# In[30]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  autots import AutoTS
import seaborn as sns
import yfinance as yf
import datetime
from datetime import date,timedelta


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




