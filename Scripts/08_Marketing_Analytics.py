#!/usr/bin/env python
# coding: utf-8

# # Retail Analytics Platform
# 
# ## Notebook 08 - Marketing Analytics
# 
# ### Business Objective
# 
# Analyze product performance, category performance, store performance, marketing effectiveness and revenue contribution using retail sales data.
# 
# ### Analytical Techniques
# 
# - Revenue Analytics
# - Product Performance Analytics
# - Category Performance Analytics
# - Store Performance Analytics
# - Marketing ROI Analytics
# - Product Mix Analytics
# - Consumer Purchase Behavior Analytics
# 
# ### Expected Outputs
# 
# - marketing_category_summary.csv
# - marketing_product_summary.csv
# - marketing_store_summary.csv
# - marketing_roi.csv
# - marketing_kpi_summary.csv
# 
# ### Author
# 
# Umesh Zure

# In[ ]:


# ============================================================
# IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

print("Libraries Loaded Successfully")


# In[ ]:


# ============================================================
# LOAD DATASET
# ============================================================

sales_df = pd.read_csv(
    "../data/sample_data/retail_sales.csv"
)

print("Dataset Loaded Successfully")
print("Shape:", sales_df.shape)


# In[ ]:


# ============================================================
# DATASET OVERVIEW
# ============================================================

print("="*60)
print("COLUMN NAMES")
print("="*60)

print(sales_df.columns.tolist())

sales_df.head()


# In[ ]:


# ============================================================
# MARKETING ANALYTICS DATA OVERVIEW
# ============================================================

print("="*60)
print("MARKETING ANALYTICS DATA OVERVIEW")
print("="*60)

print("Orders     :", sales_df["Order_ID"].nunique())
print("Products   :", sales_df["Product"].nunique())
print("Categories :", sales_df["Category"].nunique())
print("Stores     :", sales_df["Store"].nunique())
print("Revenue    :", round(sales_df["Revenue"].sum(),2))


# In[ ]:


# ============================================================
# CATEGORY PERFORMANCE ANALYTICS
# ============================================================

category_summary = (
    sales_df.groupby("Category")
    .agg(
        Revenue=("Revenue","sum"),
        Quantity=("Quantity","sum")
    )
    .reset_index()
    .sort_values(
        by="Revenue",
        ascending=False
    )
)

category_summary


# In[ ]:


# ============================================================
# PRODUCT PERFORMANCE ANALYTICS
# ============================================================

product_summary = (
    sales_df.groupby("Product")
    .agg(
        Revenue=("Revenue","sum"),
        Quantity=("Quantity","sum")
    )
    .reset_index()
    .sort_values(
        by="Revenue",
        ascending=False
    )
)

product_summary.head(10)


# In[ ]:


# ============================================================
# STORE PERFORMANCE ANALYTICS
# ============================================================

store_summary = (
    sales_df.groupby("Store")
    .agg(
        Revenue=("Revenue","sum"),
        Quantity=("Quantity","sum")
    )
    .reset_index()
    .sort_values(
        by="Revenue",
        ascending=False
    )
)

store_summary


# In[ ]:


# ============================================================
# MARKETING ROI ANALYTICS
# ============================================================

marketing_roi = category_summary.copy()

marketing_roi["Marketing_Spend"] = (
    marketing_roi["Revenue"] * 0.10
)

marketing_roi["ROI_Percentage"] = (
    (
        marketing_roi["Revenue"]
        -
        marketing_roi["Marketing_Spend"]
    )
    /
    marketing_roi["Marketing_Spend"]
) * 100

marketing_roi


# In[ ]:


# ============================================================
# PRODUCT MIX ANALYTICS
# ============================================================

product_mix = (
    sales_df.groupby("Category")
    .agg(
        Revenue=("Revenue","sum")
    )
    .reset_index()
)

product_mix["Revenue_Share_Pct"] = (
    product_mix["Revenue"]
    /
    product_mix["Revenue"].sum()
) * 100

product_mix.sort_values(
    by="Revenue_Share_Pct",
    ascending=False
)


# In[ ]:


# ============================================================
# CONSUMER PURCHASE BEHAVIOR ANALYTICS
# ============================================================

consumer_behavior = (
    sales_df.groupby("Category")
    .agg(
        Orders=("Order_ID","count"),
        Revenue=("Revenue","sum"),
        Quantity=("Quantity","sum")
    )
    .reset_index()
    .sort_values(
        by="Revenue",
        ascending=False
    )
)

consumer_behavior


# In[ ]:


# ============================================================
# MARKETING KPI DASHBOARD
# ============================================================

marketing_kpi = pd.DataFrame({

    "Metric":[
        "Total Revenue",
        "Total Orders",
        "Total Products",
        "Total Categories",
        "Total Stores"
    ],

    "Value":[
        sales_df["Revenue"].sum(),
        sales_df["Order_ID"].nunique(),
        sales_df["Product"].nunique(),
        sales_df["Category"].nunique(),
        sales_df["Store"].nunique()
    ]
})

marketing_kpi


# In[ ]:


# ============================================================
# SAVE OUTPUT FILES
# ============================================================

category_summary.to_csv(
    "../data/processed/marketing_category_summary.csv",
    index=False
)

product_summary.to_csv(
    "../data/processed/marketing_product_summary.csv",
    index=False
)

store_summary.to_csv(
    "../data/processed/marketing_store_summary.csv",
    index=False
)

marketing_roi.to_csv(
    "../data/processed/marketing_roi.csv",
    index=False
)

marketing_kpi.to_csv(
    "../data/processed/marketing_kpi_summary.csv",
    index=False
)

print("="*60)
print("MARKETING ANALYTICS OUTPUTS GENERATED")
print("="*60)


# In[ ]:


# ============================================================
# EXECUTION SUMMARY
# ============================================================

print("Notebook Completed Successfully")

print("\nGenerated Files:")

print("1. marketing_category_summary.csv")
print("2. marketing_product_summary.csv")
print("3. marketing_store_summary.csv")
print("4. marketing_roi.csv")
print("5. marketing_kpi_summary.csv")

