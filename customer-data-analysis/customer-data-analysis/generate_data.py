"""
generate_data.py
Creates a synthetic customer dataset for behavioral analysis.
Run this once to (re)create data/customer_data.csv
"""

import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(7)

N = 400
genders = ["Male", "Female"]

customer_id = np.arange(1001, 1001 + N)
age = np.random.randint(18, 65, N)
gender = np.random.choice(genders, N)
annual_income_k = np.round(np.random.normal(55, 20, N).clip(15, 150), 1)
spending_score = np.random.randint(1, 100, N)
purchase_frequency = np.random.poisson(6, N)  # purchases per year
membership_years = np.round(np.random.uniform(0, 8, N), 1)

df = pd.DataFrame({
    "CustomerID": customer_id,
    "Age": age,
    "Gender": gender,
    "AnnualIncome_k": annual_income_k,
    "SpendingScore": spending_score,
    "PurchaseFrequency": purchase_frequency,
    "MembershipYears": membership_years,
})

# inject a few missing values to mimic real-world data
missing_idx = np.random.choice(df.index, 12, replace=False)
df.loc[missing_idx, "AnnualIncome_k"] = np.nan

Path("data").mkdir(exist_ok=True)
df.to_csv("data/customer_data.csv", index=False)
print(f"Saved {len(df)} rows to data/customer_data.csv")
