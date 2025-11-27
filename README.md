# Coffee-Shop-Sales-Analysis
This project is a deep-dive analysis of 149,000+ real-world simulated coffee shop transactions collected from 3 store locations in NYC. The goal was to uncover meaningful business insights related to sales performance, customer behavior, product trends, and revenue distribution.

☕ Coffee Shop Sales Analysis – Data Analytics Project

A deep-dive data analysis project exploring 149,000+ coffee shop transactions from three NYC locations, aimed at uncovering insights on customer behavior, sales performance, and product trends. This project transforms raw data into actionable business intelligence using Python, statistical analysis, and rich visualizations.

📌 Project Overview

This project focuses on understanding business performance through data-driven insights. Key questions explored:

When do customers visit the most?

Which products contribute most to revenue?

How do sales vary across stores, weekdays, and time of day?

Can statistical tests validate assumptions about customer behavior?

Using real-world simulation data, the project identifies peak hours, high-performing products, weekly patterns, and store-wise revenue differences.

📂 Dataset

149,000+ transactions

3 store locations in NYC

Contains timestamps, categories, product details, quantities, and unit prices

Preprocessing includes: cleaning, handling missing values, feature extraction (hour, day, month)

🛠️ Tools & Libraries

Python

Pandas

NumPy

Matplotlib

Seaborn

SciPy

📈 Key Outcomes & Insights 🔹 Feature Engineering

Extracted hourly, daily, and monthly trends

Created KPIs such as revenue, footfall, average bill, and product contribution

🔹 Visualizations

Created clear, insightful plots covering:

Revenue & transactions over time

Top-selling products

Store-wise performance comparison

Category distribution

Heatmaps for hour vs weekday behavior

🔹 Statistical Analysis

Applied t-tests to validate:

Whether certain days show significantly higher sales

Differences in customer spending across time periods

🔹 Business Insights

Friday mornings record the highest sales

Coffee contributes ~38% of total revenue

Peak hours fall between 8 AM – 11 AM

One store consistently outperforms others in both revenue and footfall

📁 Project Structure ├── data/ │ ├── coffee_shop_sales.csv │ └── cleaned_data.csv │ ├── notebooks/ │ ├── Coffee_Sales_Analysis.ipynb │ └── Visualizations.ipynb │ ├── visuals/ │ ├── revenue_trends.png │ ├── weekday_heatmap.png │ └── top_products.png │ ├── scripts/ │ └── analysis.py │ └── README.md

🚀 How to Run the Project

Clone the repository

git clone https://github.com/your-username/coffee-shop-sales-analysis.git

Navigate to the project folder

cd coffee-shop-sales-analysis

Install dependencies

pip install -r requirements.txt

Open the Jupyter Notebook

jupyter notebook

🧠 What I Learned

Cleaning & wrangling large datasets

Feature engineering for business KPIs

Creating meaningful and aesthetic data visualizations

Applying statistical tests (t-tests)

Presenting insights using data storytelling

📜 License

This project is open-source and available under the MIT License.
