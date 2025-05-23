import streamlit as st
import pandas as pd

st.title("Sales Data Analysis")

uploaded_file = st.file_uploader("Upload sales CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']

    st.subheader("Total Revenue per Product")
    revenue = df.groupby('Product')['Revenue'].sum().reset_index()
    st.bar_chart(revenue.set_index('Product'))

    st.subheader("Sales Trend Over Time")
    trend = df.groupby('Date')['Revenue'].sum().reset_index()
    st.line_chart(trend.set_index('Date'))

    st.subheader("Top 5 Best-Selling Products")
    top5 = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top5)
else:
    st.info("Please upload a CSV file.")
