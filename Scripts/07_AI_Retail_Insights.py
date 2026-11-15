#!/usr/bin/env python
# coding: utf-8

# # Retail Analytics Platform
# 
# ## Phase 7 - AI Retail Insights
# 
# ### Objective
# 
# Generate AI-driven business insights using outputs from previous analytics phases.
# 
# ### Business Value
# 
# Transform raw analytics into actionable business recommendations.
# 
# ### Insight Areas
# 
# - Sales Performance
# - Customer Segmentation
# - Customer Churn
# - Demand Forecasting
# - Business Recommendations
# 
# ### Outputs
# 
# - ai_retail_insights.csv
# 

# In[4]:


# ============================================================
# RETAIL ANALYTICS PLATFORM
# PHASE 7 - AI RETAIL INSIGHTS
# ============================================================

from datetime import datetime
import pandas as pd
import warnings
import time
from pathlib import Path

warnings.filterwarnings("ignore")

print("=" * 60)
print("STARTING AI RETAIL INSIGHTS")
print("=" * 60)

start_time = time.time()
run_timestamp = datetime.now()

print(f"Execution Started : {run_timestamp}")


# In[5]:


# ============================================================
# LOAD ANALYTICS OUTPUT FILES
# ============================================================

kpi_df = pd.read_csv("../data/processed/kpi_summary.csv")

rfm_df = pd.read_csv(
    "../data/processed/rfm_customer_segmentation.csv"
)

churn_df = pd.read_csv(
    "../data/processed/churn_summary.csv"
)

forecast_df = pd.read_csv(
    "../data/processed/forecast_summary.csv"
)

print("Files Loaded Successfully")

print("KPI Shape      :", kpi_df.shape)
print("RFM Shape      :", rfm_df.shape)
print("Churn Shape    :", churn_df.shape)
print("Forecast Shape :", forecast_df.shape)


# In[6]:


# ============================================================
# VALIDATION
# ============================================================

assert len(kpi_df) > 0
assert len(rfm_df) > 0
assert len(churn_df) > 0
assert len(forecast_df) > 0

print("Validation Passed")

