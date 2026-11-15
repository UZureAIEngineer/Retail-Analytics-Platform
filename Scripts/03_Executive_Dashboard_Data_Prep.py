#!/usr/bin/env python
# coding: utf-8

# # Retail Analytics Platform
# 
# ## Notebook 03: Executive Dashboard Data Preparation
# 
# ### Objective
# Prepare aggregated datasets and KPI summaries for Power BI Executive Dashboard reporting.
# 
# ### Outputs
# - KPI Summary
# - Product Summary
# - Region Summary
# - Customer Summary
# - Monthly Sales Trend
# 
# ### Author
# Umesh Zure
# 
# ### Tools
# Python, Pandas, Power BI

# In[5]:


# --------------------------------------------------
# Retail Analytics Platform
# Executive Dashboard Data Preparation
# --------------------------------------------------

import pandas as pd
import numpy as np

print("Libraries loaded successfully")


# In[12]:


# Load retail dataset

df = pd.read_csv("../data/sample_data/retail_sales.csv")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

df.head()


# In[9]:


import os

for root, dirs, files in os.walk("../data"):
    print("\nFolder:", root)

    for file in files:
        print("   ", file)


# In[13]:


print("Dataset Information")
print("-" * 40)

print("Rows :", df.shape[0])
print("Columns :", df.shape[1])

df.info()


# In[14]:


# Executive KPI Summary

kpi_summary = pd.DataFrame({

    "Metric": [
        "Total Revenue",
        "Total Orders",
        "Total Products",
        "Total Categories",
        "Total Stores"
    ],

    "Value": [
        df["Revenue"].sum(),
        df["Order_ID"].nunique(),
        df["Product"].nunique(),
        df["Category"].nunique(),
        df["Store"].nunique()
    ]
})

kpi_summary


# In[15]:


product_summary = (
    df.groupby("Product")["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Revenue", ascending=False)
)

product_summary.head()


# In[16]:


# Revenue by Category

category_summary = (
    df.groupby("Category")["Revenue"]
      .sum()
      .reset_index()
      .sort_values("Revenue", ascending=False)
)

category_summary


# In[17]:


# Revenue by Store

store_summary = (
    df.groupby("Store")["Revenue"]
      .sum()
      .reset_index()
      .sort_values("Revenue", ascending=False)
)

store_summary


# In[18]:


# Convert Order Date

df["Order_Date"] = pd.to_datetime(df["Order_Date"])


# In[19]:


monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Revenue"]
      .sum()
      .reset_index()
)

monthly_sales


# In[20]:


# Export files for Power BI

kpi_summary.to_csv(
    "../data/processed/kpi_summary.csv",
    index=False
)

product_summary.to_csv(
    "../data/processed/product_summary.csv",
    index=False
)

category_summary.to_csv(
    "../data/processed/category_summary.csv",
    index=False
)

store_summary.to_csv(
    "../data/processed/store_summary.csv",
    index=False
)

monthly_sales.to_csv(
    "../data/processed/monthly_sales.csv",
    index=False
)

print("Dashboard datasets exported successfully")


# In[21]:


import os

files = os.listdir("../data/processed")

for file in files:
    print(file)

