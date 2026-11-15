#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello Retail Analytics")



# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("Retail Analytics Platform Ready!")
print("=" * 50)

print("Pandas Version:", pd.__version__)
print("NumPy Version :", np.__version__)


# In[4]:


import pandas as pd

print(pd.__version__)


# In[9]:


import matplotlib.pyplot as plt

sales_data.plot(
    x="Store",
    y="Revenue",
    kind="bar",
    figsize=(8,4),
    title="Store Revenue Comparison",
    color="steelblue"
)

plt.show()


# In[10]:


import pandas as pd

df = pd.read_csv("../data/sample_data/retail_sales.csv")

df.head()


# In[11]:


import pandas as pd

df = pd.read_csv("../data/sample_data/retail_sales.csv")

df.head()


# In[12]:


print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])

df.info()


# In[5]:


import numpy as np

print(np.__version__)


# In[6]:


import pandas as pd

sales_data = pd.DataFrame({
    "Store": ["Mumbai", "Pune", "Delhi", "Bangalore"],
    "Revenue": [125000, 98000, 145000, 115000]
})

sales_data


# In[1]:


import sys

print(sys.executable)


# In[2]:


import sys
print(sys.executable)


# In[3]:


import sys

print(sys.executable)

