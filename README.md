# CodexDemo_Evening

This repository contains a simple Streamlit application for analyzing sales data from a CSV file. A sample dataset (`sample_sales.csv`) is provided for demonstration purposes.

## Running the app

Install the required dependencies (Streamlit and pandas) and start the app using:

```bash
pip install streamlit pandas
streamlit run app.py
```

Upload a CSV file with the following columns:

- `Date`: Date of the sale (YYYY-MM-DD)
- `Product`: Name of the product
- `Quantity`: Units sold
- `UnitPrice`: Price per unit

The app will display:

1. **Total revenue per product** – revenue is `Quantity * UnitPrice` aggregated by product.
2. **Sales trend over time** – line chart of daily revenue.
3. **Top 5 best-selling products** – based on quantity sold.
