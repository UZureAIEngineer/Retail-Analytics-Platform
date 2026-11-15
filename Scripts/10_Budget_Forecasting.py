#!/usr/bin/env python
# coding: utf-8

# # Retail Analytics Platform
# 
# ## Notebook 10 - Budget Forecasting & Business Planning Analytics
# 
# ### Business Objective
# 
# Develop a budget forecasting framework to support retail business planning, revenue forecasting, variance analysis, and decision-making.
# 
# ### Analytical Techniques
# 
# - Revenue Forecasting
# - Budget Forecasting
# - Variance Analysis
# - Business Planning Analytics
# - Scenario Modelling
# - Financial Performance Monitoring
# 
# ### Expected Outputs
# 
# - budget_forecast.csv
# - revenue_projection.csv
# - variance_analysis.csv
# - scenario_analysis.csv
# - budget_kpi_summary.csv
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
# DATA PREPARATION
# ============================================================

sales_df["Order_Date"] = pd.to_datetime(
    sales_df["Order_Date"]
)

sales_df["Month"] = (
    sales_df["Order_Date"]
    .dt.to_period("M")
    .astype(str)
)

sales_df.head()


# In[4]:


# ============================================================
# MONTHLY REVENUE ANALYSIS
# ============================================================

monthly_revenue = (
    sales_df.groupby("Month")
    .agg(
        Revenue=("Revenue","sum")
    )
    .reset_index()
)

monthly_revenue


# In[5]:


# ============================================================
# REVENUE FORECASTING
# ============================================================

avg_revenue = monthly_revenue["Revenue"].mean()

future_months = [
    "2026-01",
    "2026-02",
    "2026-03"
]

revenue_projection = pd.DataFrame({

    "Month": future_months,

    "Forecast_Revenue":[
        round(avg_revenue * 1.02,2),
        round(avg_revenue * 1.04,2),
        round(avg_revenue * 1.06,2)
    ]
})

revenue_projection


# In[6]:


# ============================================================
# BUDGET FORECASTING
# ============================================================

budget_forecast = revenue_projection.copy()

budget_forecast["Budget"] = (
    budget_forecast["Forecast_Revenue"] * 0.95
)

budget_forecast


# In[7]:


# ============================================================
# VARIANCE ANALYSIS
# ============================================================

variance_analysis = budget_forecast.copy()

variance_analysis["Variance"] = (
    variance_analysis["Forecast_Revenue"]
    -
    variance_analysis["Budget"]
)

variance_analysis["Variance_Pct"] = (
    variance_analysis["Variance"]
    /
    variance_analysis["Budget"]
) * 100

variance_analysis


# In[8]:


# ============================================================
# SCENARIO MODELLING
# ============================================================

scenario_analysis = pd.DataFrame({

    "Scenario":[
        "Pessimistic",
        "Expected",
        "Optimistic"
    ],

    "Revenue":[
        round(avg_revenue * 0.90,2),
        round(avg_revenue * 1.00,2),
        round(avg_revenue * 1.10,2)
    ]

})

scenario_analysis


# In[9]:


# ============================================================
# BUDGET KPI DASHBOARD
# ============================================================

budget_kpi = pd.DataFrame({

    "Metric":[
        "Total Historical Revenue",
        "Average Monthly Revenue",
        "Forecast Revenue",
        "Budget Revenue",
        "Forecast Variance"
    ],

    "Value":[
        round(
            sales_df["Revenue"].sum(),2
        ),
        round(
            avg_revenue,2
        ),
        round(
            budget_forecast["Forecast_Revenue"].sum(),2
        ),
        round(
            budget_forecast["Budget"].sum(),2
        ),
        round(
            variance_analysis["Variance"].sum(),2
        )
    ]
})

budget_kpi


# In[10]:


# ============================================================
# SAVE OUTPUT FILES
# ============================================================

budget_forecast.to_csv(
    "../data/processed/budget_forecast.csv",
    index=False
)

revenue_projection.to_csv(
    "../data/processed/revenue_projection.csv",
    index=False
)

variance_analysis.to_csv(
    "../data/processed/variance_analysis.csv",
    index=False
)

scenario_analysis.to_csv(
    "../data/processed/scenario_analysis.csv",
    index=False
)

budget_kpi.to_csv(
    "../data/processed/budget_kpi_summary.csv",
    index=False
)

print("="*60)
print("BUDGET FORECASTING OUTPUTS GENERATED")
print("="*60)


# In[11]:


# ============================================================
# EXECUTION SUMMARY
# ============================================================

print("Notebook Completed Successfully")

print("\nGenerated Files:")

print("1. budget_forecast.csv")
print("2. revenue_projection.csv")
print("3. variance_analysis.csv")
print("4. scenario_analysis.csv")
print("5. budget_kpi_summary.csv")


# In[ ]:




