#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ==================================================
# Retail Analytics Platform
# Notebook: 02_Retail_EDA_Clean
# Purpose : Retail Data Exploration
# Author  : Umesh Zure
# Date    : 22-Oct-2026
# ==================================================


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Retail Analytics Environment Ready")


# In[4]:


df = pd.read_csv("../data/sample_data/retail_sales.csv")

df.head()


# In[5]:


print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

df.info()


# In[6]:


df.isnull().sum()


# In[7]:


total_revenue = df["Revenue"].sum()
total_orders = len(df)

print("Total Revenue :", total_revenue)
print("Total Orders  :", total_orders)


# In[8]:


store_sales = df.groupby("Store")["Revenue"].sum()

store_sales


# In[9]:


store_sales.plot(
    kind="bar",
    figsize=(8,4),
    title="Revenue by Store"
)

plt.show()


# In[10]:


# ==================================================
# KPI Summary
# ==================================================

total_revenue = df["Revenue"].sum()
total_orders = len(df)
average_revenue = df["Revenue"].mean()
total_quantity = df["Quantity"].sum()

print("Total Revenue  :", total_revenue)
print("Total Orders   :", total_orders)
print("Average Revenue:", round(average_revenue,2))
print("Total Quantity :", total_quantity)


# In[11]:


store_sales = (
    df.groupby("Store")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

store_sales


# In[12]:


import matplotlib.pyplot as plt

store_sales.plot(
    kind="bar",
    figsize=(8,4),
    title="Revenue by Store",
    color="steelblue"
)

plt.ylabel("Revenue")
plt.show()


# In[13]:


category_sales = (
    df.groupby("Category")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

category_sales


# In[14]:


category_sales.plot(
    kind="bar",
    figsize=(8,4),
    title="Revenue by Category",
    color="green"
)

plt.ylabel("Revenue")
plt.show()


# In[15]:


product_sales = (
    df.groupby("Product")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

product_sales

