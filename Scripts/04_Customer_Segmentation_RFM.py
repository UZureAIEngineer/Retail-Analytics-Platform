#!/usr/bin/env python
# coding: utf-8

# # Retail Analytics Platform
# 
# ## Phase 3 - Customer Segmentation (RFM Analysis)
# 
# ### Objective
# Perform customer segmentation using the RFM methodology.
# 
# ### RFM Components
# 
# - Recency
# - Frequency
# - Monetary Value
# 
# ### Output
# 
# - Customer Scores
# - Customer Segments
# - Business Recommendations
# 
# ### Author
# 
# Umesh Zure

# In[2]:


# --------------------------------------------------
# Retail Analytics Platform
# Phase 3 - Customer Segmentation
# --------------------------------------------------

import pandas as pd
import numpy as np

print("Libraries loaded successfully")


# In[3]:


df = pd.read_csv("../data/sample_data/retail_sales.csv")

df.head()


# In[4]:


customer_ids = [
    "CUST001",
    "CUST002",
    "CUST003",
    "CUST001",
    "CUST004",
    "CUST005",
    "CUST002",
    "CUST003",
    "CUST006",
    "CUST001"
]

df["Customer_ID"] = customer_ids

df.head()


# In[5]:


df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Date conversion completed")


# In[6]:


analysis_date = df["Order_Date"].max()

print("Analysis Date:", analysis_date)


# In[7]:


rfm = df.groupby("Customer_ID").agg({
    "Order_Date": lambda x: (analysis_date - x.max()).days,
    "Order_ID": "count",
    "Revenue": "sum"
})

rfm.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]

rfm


# In[8]:


rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    3,
    labels=[3, 2, 1]
)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    3,
    labels=[1, 2, 3]
)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    3,
    labels=[1, 2, 3]
)

rfm


# In[9]:


rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)

rfm


# In[10]:


def segment_customer(score):

    if score >= "333":
        return "Champions"

    elif score >= "233":
        return "Loyal Customers"

    elif score >= "132":
        return "Potential Loyalists"

    else:
        return "At Risk"

rfm["Segment"] = rfm["RFM_Score"].apply(segment_customer)

rfm


# In[11]:


segment_summary = (
    rfm["Segment"]
    .value_counts()
    .reset_index()
)

segment_summary


# In[12]:


rfm.to_csv(
    "../data/processed/rfm_customer_segmentation.csv"
)

segment_summary.to_csv(
    "../data/processed/rfm_segment_summary.csv"
)

print("RFM outputs exported successfully")

