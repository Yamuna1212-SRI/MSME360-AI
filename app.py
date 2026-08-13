import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="MSME360 AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 MSME360 AI")
st.subheader("Intelligent Digital Business Management Platform for MSMEs")

st.write(
    "An AI-powered business assistant that helps MSMEs "
    "analyse sales, monitor inventory and make smarter decisions."
)

# Sample sales data
sales_data = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Sales": [
        42000, 45000, 47000, 49000, 53000, 56000,
        59000, 61000, 65000, 68000, 72000, 76000
    ]
})

# Sample inventory data
inventory_data = pd.DataFrame({
    "Product": [
        "Cotton Shirt",
        "Formal Shirt",
        "Jeans",
        "T-Shirt",
        "Jacket"
    ],
    "Stock": [120, 35, 18, 85, 12],
    "Reorder_Level": [50, 40, 30, 50, 20]
})

# Sidebar
st.sidebar.title("MSME360 AI")

menu = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Sales Forecast",
        "Smart Inventory",
        "AI Recommendations"
    ]
)

# Dashboard
if menu == "Dashboard":

    st.header("📊 Business Dashboard")

    total_sales = sales_data["Sales"].sum()
    average_sales = sales_data["Sales"].mean()

    low_stock = sum(
        inventory_data["Stock"]
        < inventory_data["Reorder_Level"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Annual Sales",
        f"₹{total_sales:,.0f}"
    )

    col2.metric(
        "Average Monthly Sales",
        f"₹{average_sales:,.0f}"
    )

    col3.metric(
        "Low Stock Items",
        low_stock
    )

    st.divider()

    st.subheader("📈 Monthly Sales")

    st.line_chart(
        sales_data.set_index("Month")["Sales"]
    )

    st.subheader("📦 Inventory")

    st.dataframe(
        inventory_data,
        use_container_width=True
    )

# Sales Forecast
elif menu == "Sales Forecast":

    st.header("📈 AI Sales Forecast")

    X = np.arange(1, 13).reshape(-1, 1)
    y = sales_data["Sales"].values

    model = LinearRegression()
    model.fit(X, y)

    next_month = np.array([[13]])

    prediction = model.predict(next_month)[0]

    st.success(
        f"🤖 Predicted next-month sales: ₹{prediction:,.0f}"
    )

    st.line_chart(
        sales_data.set_index("Month")["Sales"]
    )

    st.info(
        "AI Insight: Sales are showing a positive growth trend. "
        "The business should maintain sufficient inventory."
    )

# Smart Inventory
elif menu == "Smart Inventory":

    st.header("📦 Smart Inventory Management")

    inventory_data["Status"] = np.where(
        inventory_data["Stock"]
        < inventory_data["Reorder_Level"],
        "⚠️ Reorder Required",
        "✅ Stock Healthy"
    )

    st.dataframe(
        inventory_data,
        use_container_width=True
    )

    st.subheader("⚠️ AI Inventory Alerts")

    low_stock_products = inventory_data[
        inventory_data["Stock"]
        < inventory_data["Reorder_Level"]
    ]

    for _, row in low_stock_products.iterrows():

        st.warning(
            f"{row['Product']}: Current stock "
            f"{row['Stock']} units. "
            f"Reorder level: "
            f"{row['Reorder_Level']} units."
        )

# AI Recommendations
elif menu == "AI Recommendations":

    st.header("🤖 AI Business Recommendations")

    latest_sales = sales_data["Sales"].iloc[-1]
    previous_sales = sales_data["Sales"].iloc[-2]

    growth = (
        (latest_sales - previous_sales)
        / previous_sales
    ) * 100

    if growth > 0:

        st.success(
            f"📈 Sales increased by {growth:.1f}% "
            "compared with the previous month."
        )

    st.warning(
        "📦 Check products that are below their "
        "reorder level."
