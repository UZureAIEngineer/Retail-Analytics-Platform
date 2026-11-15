#!/usr/bin/env python
# coding: utf-8

# # Retail Analytics Platform
# 
# ## Notebook 09 - A/B Testing & Promotion Analytics
# 
# ### Business Objective
# 
# Evaluate the effectiveness of retail promotions using A/B testing methodologies, promotion lift analysis, revenue uplift measurement, and statistical significance testing.
# 
# ### Analytical Techniques
# 
# - A/B Testing Framework
# - Test vs Control Analysis
# - Promotion Lift Analytics
# - Revenue Uplift Analysis
# - Statistical Significance Testing
# - Business Decision Analytics
# 
# ### Expected Outputs
# 
# - ab_test_summary.csv
# - promotion_uplift.csv
# - statistical_summary.csv
# - ab_testing_kpi_summary.csv
# 
# ### Author
# 
# Umesh Zure

# In[1]:


# ============================================================
# IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import warnings
from scipy import stats

warnings.filterwarnings("ignore")

print("Libraries Loaded Successfully")


# In[2]:


# ============================================================
# LOAD DATASET
# ============================================================

sales_df = pd.read_csv(
    "../data/sample_data/retail_sales.csv"
)

print("Dataset Loaded Successfully")
print("Shape :", sales_df.shape)


# In[3]:


# ============================================================
# DATASET OVERVIEW
# ============================================================

print("="*60)
print("A/B TESTING DATA OVERVIEW")
print("="*60)

print("Orders     :", sales_df["Order_ID"].nunique())
print("Products   :", sales_df["Product"].nunique())
print("Categories :", sales_df["Category"].nunique())
print("Stores     :", sales_df["Store"].nunique())
print("Revenue    :", round(sales_df["Revenue"].sum(),2))


# In[4]:


# ============================================================
# CREATE TEST AND CONTROL GROUPS
# ============================================================

np.random.seed(42)

sales_df["Test_Group"] = np.where(
    np.random.rand(len(sales_df)) > 0.5,
    "Promotion_A",
    "Promotion_B"
)

sales_df[["Order_ID","Test_Group"]].head()


# In[5]:


# ============================================================
# TEST VS CONTROL ANALYSIS
# ============================================================

ab_summary = (
    sales_df.groupby("Test_Group")
    .agg(
        Orders=("Order_ID","count"),
        Revenue=("Revenue","sum"),
        Quantity=("Quantity","sum")
    )
    .reset_index()
)

ab_summary


# In[6]:


# ============================================================
# REVENUE UPLIFT ANALYSIS
# ============================================================

promo_a = ab_summary.loc[
    ab_summary["Test_Group"]=="Promotion_A",
    "Revenue"
].iloc[0]

promo_b = ab_summary.loc[
    ab_summary["Test_Group"]=="Promotion_B",
    "Revenue"
].iloc[0]

uplift_pct = (
    (promo_a - promo_b)
    /
    promo_b
) * 100

promotion_uplift = pd.DataFrame({

    "Metric":["Revenue Uplift %"],
    "Value":[round(uplift_pct,2)]

})

promotion_uplift


# In[7]:


# ============================================================
# AVERAGE REVENUE ANALYSIS
# ============================================================

avg_revenue = (
    sales_df.groupby("Test_Group")
    .agg(
        Avg_Revenue=("Revenue","mean")
    )
    .reset_index()
)

avg_revenue


# In[8]:


# ============================================================
# STATISTICAL SIGNIFICANCE TEST
# ============================================================

group_a = sales_df[
    sales_df["Test_Group"]=="Promotion_A"
]["Revenue"]

group_b = sales_df[
    sales_df["Test_Group"]=="Promotion_B"
]["Revenue"]

t_stat, p_value = stats.ttest_ind(
    group_a,
    group_b,
    equal_var=False
)

statistical_summary = pd.DataFrame({

    "Metric":[
        "T Statistic",
        "P Value"
    ],

    "Value":[
        round(t_stat,4),
        round(p_value,4)
    ]

})

statistical_summary


# In[9]:


# ============================================================
# A/B TEST RESULT INTERPRETATION
# ============================================================

if p_value < 0.05:
    result = "Statistically Significant"
else:
    result = "Not Statistically Significant"

print("A/B Test Result :", result)


# In[10]:


# ============================================================
# A/B TESTING KPI DASHBOARD
# ============================================================

ab_kpi = pd.DataFrame({

    "Metric":[
        "Total Revenue",
        "Total Orders",
        "Promotion A Revenue",
        "Promotion B Revenue",
        "Revenue Uplift %"
    ],

    "Value":[
        round(sales_df["Revenue"].sum(),2),
        sales_df["Order_ID"].count(),
        round(promo_a,2),
        round(promo_b,2),
        round(uplift_pct,2)
    ]
})

ab_kpi


# In[11]:


# ============================================================
# SAVE OUTPUT FILES
# ============================================================

ab_summary.to_csv(
    "../data/processed/ab_test_summary.csv",
    index=False
)

promotion_uplift.to_csv(
    "../data/processed/promotion_uplift.csv",
    index=False
)

statistical_summary.to_csv(
    "../data/processed/statistical_summary.csv",
    index=False
)

ab_kpi.to_csv(
    "../data/processed/ab_testing_kpi_summary.csv",
    index=False
)

print("A/B Testing outputs generated successfully")


# In[12]:


# ============================================================
# EXECUTION SUMMARY
# ============================================================

print("Notebook Completed Successfully")

print("\nGenerated Files:")

print("1. ab_test_summary.csv")
print("2. promotion_uplift.csv")
print("3. statistical_summary.csv")
print("4. ab_testing_kpi_summary.csv")

