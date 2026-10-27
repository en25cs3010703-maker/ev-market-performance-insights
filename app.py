from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json
from pathlib import Path

app = Flask(__name__)
DATA_PATH = Path(__file__).parent / "data" / "ev_market_data.csv"

def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce").fillna(0).astype(int)
    for col in ["Annual_Sales", "Battery_Capacity_kWh", "Driving_Range_km", "Customer_Rating"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.dropna(subset=["Manufacturer", "Country", "Vehicle_Category"])

@app.route("/")
def dashboard():
    df = load_data()
    years = sorted(df["Year"].dropna().unique().tolist())
    categories = sorted(df["Vehicle_Category"].dropna().unique().tolist())
    manufacturers = sorted(df["Manufacturer"].dropna().unique().tolist())
    selected_year = request.args.get("year", "All")
    selected_category = request.args.get("category", "All")
    selected_manufacturer = request.args.get("manufacturer", "All")

    filtered = df.copy()
    if selected_year != "All":
        filtered = filtered[filtered["Year"] == int(selected_year)]
    if selected_category != "All":
        filtered = filtered[filtered["Vehicle_Category"] == selected_category]
    if selected_manufacturer != "All":
        filtered = filtered[filtered["Manufacturer"] == selected_manufacturer]

    total_sales = int(filtered["Annual_Sales"].sum())
    avg_range = round(filtered["Driving_Range_km"].mean(), 1) if not filtered.empty else 0
    avg_rating = round(filtered["Customer_Rating"].mean(), 2) if not filtered.empty else 0
    manufacturer_count = int(filtered["Manufacturer"].nunique())

    sales_by_year = filtered.groupby("Year", as_index=False)["Annual_Sales"].sum()
    fig_year = px.line(sales_by_year, x="Year", y="Annual_Sales", markers=True,
                       title="Annual EV Sales Trend", template="plotly_white")
    fig_year.update_layout(margin=dict(l=20,r=20,t=55,b=20), height=330)

    sales_by_maker = filtered.groupby("Manufacturer", as_index=False)["Annual_Sales"].sum().sort_values("Annual_Sales", ascending=False)
    fig_maker = px.bar(sales_by_maker, x="Manufacturer", y="Annual_Sales", color="Manufacturer",
                       title="Sales by Manufacturer", template="plotly_white")
    fig_maker.update_layout(showlegend=False, margin=dict(l=20,r=20,t=55,b=20), height=350)

    battery = filtered.groupby("Battery_Technology", as_index=False)["Annual_Sales"].sum().sort_values("Annual_Sales", ascending=False)
    fig_battery = px.pie(battery, names="Battery_Technology", values="Annual_Sales",
                         title="Sales by Battery Technology", hole=.48, template="plotly_white")
    fig_battery.update_layout(margin=dict(l=20,r=20,t=55,b=20), height=350)

    fig_range = px.scatter(filtered, x="Battery_Capacity_kWh", y="Driving_Range_km",
                           color="Vehicle_Category", size="Annual_Sales",
                           hover_name="Manufacturer", title="Battery Capacity vs Driving Range",
                           template="plotly_white")
    fig_range.update_layout(margin=dict(l=20,r=20,t=55,b=20), height=350)

    charts = [pio.to_html(fig, full_html=False, include_plotlyjs="cdn") for fig in [fig_year, fig_maker, fig_battery, fig_range]]
    table_rows = filtered.sort_values("Annual_Sales", ascending=False).head(12).to_dict(orient="records")
    return render_template("index.html", years=years, categories=categories, manufacturers=manufacturers,
        selected_year=selected_year, selected_category=selected_category, selected_manufacturer=selected_manufacturer,
        total_sales=f"{total_sales:,}", avg_range=avg_range, avg_rating=avg_rating,
        manufacturer_count=manufacturer_count, charts=charts, table_rows=table_rows, row_count=len(filtered))

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(__import__("os").environ.get("PORT", 5000)), debug=False)
