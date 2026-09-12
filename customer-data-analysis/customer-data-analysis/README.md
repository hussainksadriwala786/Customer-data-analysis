# Customer Data Analysis

Uncovered customer behavioral patterns using Pandas and statistical methods,
with results visualized in Matplotlib.

## Overview

This project explores a customer dataset to understand spending behavior
across different age groups, income levels, and genders — the kind of
segmentation analysis a retail or marketing team would use to target
campaigns more effectively.

## Dataset

`data/customer_data.csv` contains one row per customer:

| Column             | Description                          |
|--------------------|---------------------------------------|
| CustomerID         | Unique customer identifier            |
| Age                | Customer age                          |
| Gender             | Male / Female                         |
| AnnualIncome_k     | Annual income in thousands ($)        |
| SpendingScore      | Score (1-100) assigned based on spending behavior |
| PurchaseFrequency  | Number of purchases in the past year  |
| MembershipYears    | Years since joining as a customer     |

Run `generate_data.py` to regenerate the dataset (a few missing income
values are injected intentionally so the cleaning step is meaningful).

## What the analysis does

1. **Load** the raw CSV.
2. **Clean**
   - Fills missing income values using the median for that gender
   - Buckets customers into age groups (18-25, 26-35, ... 56-65)
3. **Explore**
   - Summary statistics
   - Average spending score per age group
   - Correlation between income and spending score
4. **Visualize**
   - Histogram: distribution of spending scores
   - Scatter plot: income vs. spending score (colored by gender)
   - Bar chart: average spending score by age group

Charts are saved to the `outputs/` folder.

## Tech Stack

- Python
- Pandas
- Matplotlib

## How to run

```bash
pip install -r requirements.txt
python generate_data.py            # creates data/customer_data.csv
python customer_data_analysis.py   # cleans, explores, and charts the data
```

## Project Structure

```
customer-data-analysis/
├── data/
│   └── customer_data.csv
├── outputs/
│   ├── spending_score_distribution.png
│   ├── income_vs_spending.png
│   └── spending_by_age_group.png
├── generate_data.py
├── customer_data_analysis.py
├── requirements.txt
└── README.md
```
