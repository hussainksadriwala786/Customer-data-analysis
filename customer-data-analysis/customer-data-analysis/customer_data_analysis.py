"""
Customer Data Analysis
------------------------
Uncovers customer behavioral patterns using Pandas and statistical methods,
with results visualized in Matplotlib.

Author: Hussain Sadriwala
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DATA_PATH = "data/customer_data.csv"
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows, {df.shape[1]} columns")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    before_missing = df["AnnualIncome_k"].isna().sum()

    # Fill missing income with the median for that gender
    df["AnnualIncome_k"] = df.groupby("Gender")["AnnualIncome_k"].transform(
        lambda s: s.fillna(s.median())
    )

    # Bucket customers into age groups for easier segmentation
    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=[17, 25, 35, 45, 55, 65],
        labels=["18-25", "26-35", "36-45", "46-55", "56-65"],
    )

    print(f"Filled {before_missing} missing income values")
    return df


def explore_data(df: pd.DataFrame) -> None:
    print("\n--- Summary Statistics ---")
    print(df[["Age", "AnnualIncome_k", "SpendingScore", "PurchaseFrequency"]].describe())

    print("\n--- Average Spending Score by Age Group ---")
    print(df.groupby("AgeGroup", observed=True)["SpendingScore"].mean().round(1))

    print("\n--- Correlation: Income vs Spending Score ---")
    corr = df["AnnualIncome_k"].corr(df["SpendingScore"])
    print(f"Correlation coefficient: {corr:.3f}")


def visualize_data(df: pd.DataFrame) -> None:
    # 1. Spending score distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df["SpendingScore"], bins=20, color="#2E5077", edgecolor="white")
    plt.title("Distribution of Customer Spending Scores")
    plt.xlabel("Spending Score")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "spending_score_distribution.png", dpi=150)
    plt.close()

    # 2. Income vs Spending Score scatter
    plt.figure(figsize=(8, 5))
    colors = df["Gender"].map({"Male": "#3D6A96", "Female": "#C97A7A"})
    plt.scatter(df["AnnualIncome_k"], df["SpendingScore"], c=colors, alpha=0.6)
    plt.title("Annual Income vs Spending Score")
    plt.xlabel("Annual Income (k$)")
    plt.ylabel("Spending Score")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "income_vs_spending.png", dpi=150)
    plt.close()

    # 3. Average spending score by age group
    avg_by_age = df.groupby("AgeGroup", observed=True)["SpendingScore"].mean()
    plt.figure(figsize=(8, 5))
    avg_by_age.plot(kind="bar", color="#1B3A57")
    plt.title("Average Spending Score by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Average Spending Score")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "spending_by_age_group.png", dpi=150)
    plt.close()

    print(f"\nCharts saved to '{OUTPUT_DIR}/'")


def main():
    df = load_data(DATA_PATH)
    df = clean_data(df)
    explore_data(df)
    visualize_data(df)


if __name__ == "__main__":
    main()
