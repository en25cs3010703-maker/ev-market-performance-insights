# Electric Vehicle Market Performance & Insights

An educational data analytics dashboard for exploring EV sales, manufacturers, battery technologies, vehicle categories, driving range and customer ratings.

## Features
- Interactive filters for year, vehicle category and manufacturer
- KPI cards for total sales, average range, average customer rating and manufacturer count
- Plotly charts: annual sales trend, manufacturer sales, battery technology share and battery capacity vs range
- CSV dataset and SQL schema/query examples
- Responsive Flask web dashboard

## Important data note
The included `data/ev_market_data.csv` is **synthetic sample data created for demonstration**. It is not official industry data. If submitting findings as real-world facts, replace it with a trusted, cited dataset.

## Run locally
Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Publish on GitHub
1. Sign in to GitHub and create a new **public** repository named `ev-market-performance-insights`.
2. Extract this project ZIP.
3. Upload all files and folders (keep the `data` and `templates` folders).
4. Commit the files. Your repository URL will look like `https://github.com/YOUR-USERNAME/ev-market-performance-insights` (replace `YOUR-USERNAME` with your actual username).

## Deploy a live demo on Render
1. Push the project to GitHub.
2. Sign in to Render and choose **New + → Web Service**.
3. Connect the repository.
4. Set **Build Command** to `pip install -r requirements.txt`.
5. Set **Start Command** to `gunicorn app:app`.
6. Choose a free/available instance option if offered, then deploy.
7. After a successful deploy, Render provides a public URL such as `https://your-service-name.onrender.com`. Use the exact URL shown by Render in Skill Wallet.

## Suggested Skill Wallet submission
- **Project title:** Electric Vehicle Market Performance & Insights
- **GitHub link:** your actual GitHub repository URL after upload
- **Demo link:** your actual Render URL after deployment
- **Tech stack:** Python, Flask, Pandas, Plotly, CSV, SQL
- **Skills:** Data collection, data preparation, data visualization, dashboard design, business insights

## SQL examples
See `sql/analysis_queries.sql` and `sql/schema.sql`.
