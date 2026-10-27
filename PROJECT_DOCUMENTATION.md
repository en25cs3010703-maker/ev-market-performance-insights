# Project Documentation: Electric Vehicle Market Performance & Insights

## 1. Problem understanding
EV companies and analysts need a simple way to compare sales patterns, vehicle categories, battery technology, driving range and customer satisfaction.

## 2. Objectives
- Summarize EV sales over time.
- Compare manufacturer performance.
- Explore the relationship between battery capacity and driving range.
- Compare the sales represented by battery technologies.
- Provide interactive filters to support exploration.

## 3. Tools
- Python: application logic
- Pandas: loading and preparing tabular data
- Flask: web application
- Plotly: interactive charts
- CSV: included demonstration dataset
- SQL: schema and example analytical queries

## 4. Data fields
Year, Manufacturer, Country, Vehicle_Category, Battery_Technology, Battery_Capacity_kWh, Driving_Range_km, Annual_Sales, Customer_Rating.

## 5. Workflow
1. Collect a verified EV dataset.
2. Inspect column names, missing values and data types.
3. Clean numeric fields and standardize category labels.
4. Store data in a database if a database server is available.
5. Analyze sales, range, battery technology and ratings.
6. Build charts and dashboard filters.
7. Test the dashboard on desktop and mobile.
8. Publish source code to GitHub and deploy the web app.
9. Record a short walkthrough and document key findings.

## 6. Dashboard visualizations
- Annual EV Sales Trend: sales grouped by year.
- Sales by Manufacturer: compares sales totals across makers.
- Sales by Battery Technology: shows the share of sales by technology.
- Battery Capacity vs Driving Range: explores vehicle-level relationships.
- Data Explorer: provides a table of filtered records.

## 7. Limitations
The included data is synthetic and intended only to test the dashboard. Its charts must not be interpreted as official market statistics. Replace it with a documented source dataset before drawing real-world conclusions.

## 8. Conclusion
The dashboard demonstrates an end-to-end analytics workflow: loading data, filtering, aggregating, visualizing and presenting results in a web interface. It can be extended with a live database, verified data source, Tableau workbook and more detailed forecasting.
