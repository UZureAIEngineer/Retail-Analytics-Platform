# Canada RMS Enterprise Analytics Platform

## Overview

The Canada RMS (Retail Measurement Services) Enterprise Analytics Platform is an enterprise-scale retail measurement and market intelligence solution developed as part of the Retail Analytics Platform.

The project simulates a real-world Retail Measurement Services ecosystem inspired by large-scale retail measurement and consumer goods analytics environments.

The platform combines Retail Analytics, Data Engineering, Lakehouse Architecture, Business Intelligence, Market Measurement, Distribution Analytics, Pricing Analytics, Promotion Analytics, and Executive Reporting into a unified solution.

---

## Business Objectives

The platform addresses key retail business questions:

- How large is the retail universe?
- Which retailers and channels contribute most to category sales?
- What is current market share by product, brand, and category?
- How effectively are products distributed across stores?
- What is the impact of promotions on sales?
- How is ACV (All Commodity Volume) changing over time?
- How should sampled stores be projected to the retail universe?
- Which categories are gaining or losing share?
- What are the key retail KPIs at executive level?

---

# RMS Business Process Flow

Retail Universe
↓

StoreMaster Creation
↓

Sample Design
↓

Store Classification
↓

Data Collection
↓

Projection Factors
↓

Sales Expansion
↓

ACV Calculation
↓

Distribution Analytics
↓

Pricing Analytics
↓

Promotion Analytics
↓

Market Share Analytics
↓

Executive KPI Reporting

---

# RMS Data Scale

| Entity | Volume |
|----------|---------:|
| Customers | 500,000 |
| Products | 20,000 |
| Stores | 4,000 |
| Transactions | 1,250,000+ |
| Pricing Records | 500,000+ |
| Promotion Records | 250,000+ |
| Distribution Records | 150,000+ |
| ACV Records | 300,000+ |

---

# Technology Stack

## Analytics

- Python
- Pandas
- NumPy

## Data Engineering

- Databricks
- PySpark
- Spark SQL
- Delta Lake

## Reporting

- Power BI
- Executive KPI Reporting
- Weekly RMS Mart

## Data Platform

- Lakehouse Architecture
- Managed Delta Tables
- Distributed Processing

---

# RMS Dimensions

The platform generates enterprise-grade master data structures.

## DIM_GEOGRAPHY

- Province
- City
- Geographic Hierarchy

## DIM_TIME

- Date
- Week
- Month
- Quarter
- Year

## DIM_RETAILER

- Retailer Name
- Channel Classification

## DIM_STORE

- Store Details
- Location
- Store Size
- ACV Weight

## DIM_PRODUCT

- Product
- Brand
- Category
- Subcategory

## DIM_CUSTOMER

- Customer
- Province
- Income Band
- Family Size

---

# RMS Fact Tables

## FACT_SALES

Retail transaction activity including:

- Product
- Customer
- Store
- Units Sold

## FACT_PRICING

- Regular Price
- Promotional Price

## FACT_PROMOTION

- Feature
- Display
- TPR
- BOGO
- Coupon Promotions

## FACT_DISTRIBUTION

- Numeric Distribution
- Weighted Distribution

## FACT_ACV

- All Commodity Volume
- Weekly ACV Tracking

## FACT_PROJECTION

- Projection Factors
- Sample Expansion Metrics

## FACT_EXPANSION

- Sample Sales
- Expanded Sales

---

# Advanced RMS Components

## StoreMaster Framework

Provides:

- Store Registry
- Retailer Mapping
- Geographic Classification
- Channel Assignment

## Universe Estimation

Supports:

- Retail Universe Calculation
- Population Estimation
- Sample Coverage Analysis

## Sampling Engine

Supports:

- Sample Store Selection
- Sample Coverage Tracking
- Statistical Sampling

## Projection Framework

Supports:

- Sample Expansion
- Projection Factors
- Market Estimation

## Store Weighting Logic

Supports:

- Store Weight Calculation
- Weighted Sales Estimation
- Weighted Market Measurement

---

# Retail Analytics Outputs

## ACV Analytics

- Weekly ACV Trends
- Product-Level ACV
- Store-Level ACV

## Distribution Analytics

### Numeric Distribution

Percentage of stores carrying a product.

### Weighted Distribution

Distribution weighted by store importance and volume.

## Market Share Analytics

- Product Share
- Category Share
- Share Change Analysis

## Pricing Analytics

- Regular Price Tracking
- Promotional Price Analysis

## Promotion Analytics

- Baseline Sales
- Incremental Sales
- Promotion Lift %

---

# Executive KPI Layer

Executive dashboards include:

- Customer Counts
- Product Counts
- Store Counts
- Transaction Counts
- Market Share Metrics
- Distribution Metrics
- ACV Metrics
- Promotional KPIs

---

# Databricks Implementation

This RMS solution was successfully executed in Databricks using:

- Serverless Compute
- PySpark
- Delta Lake
- Managed Tables
- Spark DataFrames
- Distributed Processing

Execution included:

- Environment Validation
- Delta Lake Validation
- RMS Data Generation
- Large-Scale Transaction Processing
- KPI Reporting

---

# Lakehouse Architecture

Bronze Layer

- Raw RMS Inputs
- Retailer Data
- Product Data
- Customer Data
- Transaction Data

↓

Silver Layer

- Cleansed RMS Data
- Standardized Dimensions
- Fact Tables

↓

Gold Layer

- Market Share
- Distribution Analytics
- ACV Analytics
- Pricing Analytics
- Executive KPI Mart

↓

Power BI Reporting Layer

---

# Portfolio Highlights

✅ Databricks Implementation

✅ Delta Lake Validation

✅ PySpark Processing

✅ RMS StoreMaster Framework

✅ Universe Estimation Engine

✅ Retail Sampling Engine

✅ Projection Factor Analytics

✅ Store Weighting Logic

✅ ACV Analytics

✅ Distribution Analytics

✅ Market Share Analytics

✅ Executive KPI Reporting

✅ 1.25M+ Retail Transactions

✅ Enterprise Lakehouse Architecture

---

# Repository Location

```text
Retail-Analytics-Platform
│
└── RMS_Enterprise
    ├── README.md
    ├── notebooks
    ├── schemas
    ├── sample_data
    └── screenshots
```
---

# Current Progress

12_Canada_RMS_Data_Generator_v2_Databricks      ✅ Completed

13_RMS_Data_Profiling_ELT                       ✅ Completed

14_RMS_Bronze_Layer_Framework                   ✅ Completed

15_RMS_Silver_Layer_Framework                   ✅ Completed

16_RMS_Gold_Layer_Framework                     ✅ Completed

17_RMS_Data_Quality_Framework                    In Progress

18_RMS_Modernization_Study

19_RMS_DuckDB_Integration

20_RMS_PostgreSQL_Integration

21_RMS_AI_Analytics_Layer

---

## Author

**Umesh Zure**

Retail Analytics | FMCG Analytics | Data Engineering | Databricks | PySpark | Delta Lake | Power BI | AI & Advanced Analytics
