
# Sample Data Directory

## Overview

This directory contains representative sample datasets from the Canada RMS (Retail Measurement Services) Enterprise Analytics Platform.

The full RMS platform generates enterprise\-scale retail measurement data including customer, product, store, transaction, pricing, promotion, distribution, ACV, and market share analytics. Due to repository size and GitHub storage considerations, only small representative samples are stored in this folder.

The sample datasets are provided for:

- Data model understanding
- Analytics demonstrations
- Portfolio review
- Power BI mock reporting
- Data engineering examples
- RMS architecture validation

---

# Why Sample Data?

The full RMS platform supports large\-scale data generation:

| Entity | Production Volume |
| --- | --- |
| Customers | 500,000 |
| Products | 20,000 |
| Stores | 4,000 |
| Transactions | 1,250,000\+ |
| Pricing Records | 500,000\+ |
| Promotion Records | 250,000\+ |
| Distribution Records | 150,000\+ |
| ACV Records | 300,000\+ |

Storing complete generated datasets in GitHub repositories is not practical due to:

- Repository size limitations
- Git performance degradation
- Large clone and download times
- Portfolio review convenience

This folder therefore contains reduced\-size samples that preserve the original data structure and business logic.

---

# Sample Files

## dim\_store\_sample.csv

Sample of the RMS StoreMaster repository.

Includes:

- Store IDs
- Retailers
- Channels
- Provinces
- Cities
- Store Size
- ACV Weight

Business Use Cases:

- Retail coverage analysis
- Geographic analytics
- Store weighting
- Distribution measurement

---

## dim\_product\_sample.csv

Sample product master data.

Includes:

- Product IDs
- UPC Codes
- Product Names
- Brands
- Categories
- Subcategories

Business Use Cases:

- Market share analysis
- Category management
- Product performance reporting
- Distribution analytics

---

## dim\_customer\_sample.csv

Sample customer dimension.

Includes:

- Customer IDs
- Province
- Income Band
- Family Size

Business Use Cases:

- Customer profiling
- Retail segmentation
- Consumer analytics

---

## fact\_sales\_sample.csv

Sample retail transaction dataset.

Includes:

- Transaction IDs
- Customer IDs
- Product IDs
- Store IDs
- Units Sold

Business Use Cases:

- Sales analytics
- Market share calculation
- Demand analysis
- KPI reporting

---

## fact\_pricing\_sample.csv

Sample pricing dataset.

Includes:

- Product IDs
- Regular Price
- Promotional Price

Business Use Cases:

- Price elasticity analysis
- Retail pricing strategy
- Competitive analysis

---

## fact\_promotion\_sample.csv

Sample promotion dataset.

Includes:

- Promotion Types
- Product IDs
- Promotion Activity

Business Use Cases:

- Promotion effectiveness
- Lift analysis
- Incremental sales measurement

---

## fact\_distribution\_sample.csv

Sample distribution analytics data.

Includes:

- Numeric Distribution
- Weighted Distribution
- ACV Metrics

Business Use Cases:

- Distribution measurement
- Coverage reporting
- Availability tracking

---

## executive\_kpi\_sample.csv

Sample executive reporting layer.

Includes:

- Customer KPIs
- Product KPIs
- Store KPIs
- Transaction KPIs

Business Use Cases:

- Executive dashboards
- Retail performance review
- Management reporting

---

# RMS Subject Areas Covered

The data model supports:

- StoreMaster Analytics
- Retail Universe Estimation
- Sample Design
- Projection Factors
- Statistical Expansion
- ACV Analytics
- Numeric Distribution
- Weighted Distribution
- Pricing Analytics
- Promotion Analytics
- Market Share Analytics
- Executive KPI Reporting

---

# Technology Stack

The complete RMS platform was developed using:

- Python
- Pandas
- NumPy
- Databricks
- PySpark
- Delta Lake
- Spark SQL
- Power BI

---

# Related Directories

RMS\_Enterprise

│

├── README.md

├── notebooks/

├── schemas/

├── sample\_data/

├── screenshots/

└── architecture/

For implementation details, architecture diagrams, and Databricks execution evidence, refer to the RMS\_Enterprise root documentation.

