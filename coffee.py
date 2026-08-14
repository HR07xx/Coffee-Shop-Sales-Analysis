from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent


def find_data_file():
    candidates = [
        ROOT / "data" / "coffee_shop_sales.xlsx",
        ROOT / "data" / "coffee_shop_sales.csv",
        ROOT / "coffee_shop_sales.xlsx",
        ROOT / "coffee_shop_sales.csv",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def load_data():
    data_path = find_data_file()
    if data_path is None:
        print("No dataset found. Please add a file named 'coffee_shop_sales.xlsx' or 'coffee_shop_sales.csv' inside the 'data/' folder.")
        print(f"Expected locations: {ROOT / 'data'}")
        return None

    print(f"Loading dataset from: {data_path}")

    if data_path.suffix.lower() == ".csv":
        df = pd.read_csv(data_path)
    else:
        df = pd.read_excel(data_path)

    return df


def prepare_data(df):
    data = df.copy()

    if "transaction_date" in data.columns:
        data["transaction_date"] = pd.to_datetime(data["transaction_date"], errors="coerce")

    if "transaction_time" in data.columns:
        data["transaction_timestamp"] = (
            data["transaction_date"].astype(str).fillna("")
            + " "
            + data["transaction_time"].astype(str).fillna("")
        )
        data["transaction_timestamp"] = pd.to_datetime(data["transaction_timestamp"], errors="coerce")

    if "transaction_date" in data.columns:
        data["transaction_month"] = data["transaction_date"].dt.month
        data["transaction_monthname"] = data["transaction_date"].dt.month_name()
        data["day_of_week"] = data["transaction_date"].dt.dayofweek
        data["day"] = data["transaction_date"].dt.day_name()
        data["transaction_hour"] = data["transaction_timestamp"].dt.hour if "transaction_timestamp" in data.columns else data["Hour"]

    if {"transaction_qty", "unit_price"}.issubset(data.columns):
        data["revenue"] = data["transaction_qty"] * data["unit_price"]

    return data


def print_summary(data):
    print("\n=== Coffee Shop Sales Summary ===")
    print(f"Rows: {len(data)}")
    print(f"Stores: {data['store_id'].nunique() if 'store_id' in data.columns else 'N/A'}")
    print(f"Locations: {data['store_location'].unique() if 'store_location' in data.columns else 'N/A'}")
    print(f"Categories: {data['product_category'].nunique() if 'product_category' in data.columns else 'N/A'}")

    if "revenue" in data.columns:
        print(f"Total Revenue: ${data['revenue'].sum():,.2f}")

    if "transaction_id" in data.columns:
        print(f"Total Orders: {data['transaction_id'].count()}")

    if "transaction_hour" in data.columns:
        hourly = data.groupby("transaction_hour").size().sort_index()
        print("\nTop sales hours:")
        print(hourly.head(10).to_string())

    if "store_location" in data.columns and "revenue" in data.columns:
        store_revenue = data.groupby("store_location")["revenue"].sum().sort_values(ascending=False)
        print("\nStore revenue:")
        print(store_revenue.to_string())


def plot_charts(data):
    if "transaction_hour" in data.columns:
        hourly_orders = data.groupby("transaction_hour", as_index=False).size().rename(columns={"size": "total_orders"})
        plt.figure(figsize=(10, 4))
        sns.barplot(data=hourly_orders, x="transaction_hour", y="total_orders", color="steelblue")
        plt.title("Hourly Orders")
        plt.xlabel("Hour")
        plt.ylabel("Orders")
        plt.tight_layout()
        plt.savefig(ROOT / "hourly_orders.png", dpi=150)
        plt.close()

    if "store_location" in data.columns and "revenue" in data.columns:
        store_revenue = data.groupby("store_location")["revenue"].sum().sort_values(ascending=False)
        plt.figure(figsize=(8, 5))
        sns.barplot(x=store_revenue.index, y=store_revenue.values, palette="viridis")
        plt.title("Revenue by Store Location")
        plt.xlabel("Store Location")
        plt.ylabel("Revenue")
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.savefig(ROOT / "store_revenue.png", dpi=150)
        plt.close()

    if "product_category" in data.columns and "revenue" in data.columns:
        category_revenue = data.groupby("product_category")["revenue"].sum().sort_values(ascending=False)
        plt.figure(figsize=(9, 5))
        sns.barplot(x=category_revenue.values, y=category_revenue.index, palette="magma")
        plt.title("Revenue by Product Category")
        plt.xlabel("Revenue")
        plt.ylabel("Category")
        plt.tight_layout()
        plt.savefig(ROOT / "category_revenue.png", dpi=150)
        plt.close()


def main():
    df = load_data()
    if df is None:
        return 0

    data = prepare_data(df)
    print_summary(data)
    plot_charts(data)
    print("\nCharts saved to the project root as PNG files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
