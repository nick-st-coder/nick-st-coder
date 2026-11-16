# Hi, I'm Nick

**Data Science & ML** — I build end-to-end ML solutions: from exploratory analysis and feature engineering to model training, experiment tracking, and serving models behind real APIs.

I'm currently a computer programming student looking for **Data Science Internship**, and I use GitHub to document projects the way they'd be done in industry — with clean code, honest validation, and measurable business impact.

---

## 🚀 Featured Projects

### [Olist E-commerce Intelligence Platform](https://github.com/nick-st-coder/olist-intelligence)
An end-to-end data platform on the Brazilian E-Commerce Public Dataset by Olist (~100k orders, 2016–2018, 9 relational CSVs): ingestion → warehouse → BI → delivery-delay prediction → deployment → monitoring. Built local-first (Docker Compose, PostgreSQL, Airflow) with GCP as an optional target.

- **Data warehouse**: raw CSVs loaded into Postgres, transformed by **dbt** into a star schema (21 models, 90 tests) — with a **BigQuery** target sharing the same SQL, and a reconciliation step proving both warehouses produce identical figures (99,441 rows, 8.11% late rate)
- **Delivery-delay model**: predicts whether an order arrives later than promised, using **chronological splits only** (no leakage) and a leakage-safe seller-history feature built on a completion timeline
- **Logistic regression wins** over LightGBM/XGBoost — the signal is close to additive; **isotonic calibration** restores honest probabilities and a **cost-based threshold** (missed late order = 10× a false alarm) drives the decision
- **Money impact**: cuts the cost of late delivery by **~29% on validation** (≈ R$0.97 per order at R$50 per missed late order); SHAP shows lead time, geography, and seller record drive predictions
- **Serving & monitoring**: **FastAPI** (4 endpoints, refuses post-purchase fields, per-order SHAP explanations) + **Streamlit** UI, **Evidently** drift/performance replay, **MLflow** tracking, **Airflow** orchestration, **Power BI** report, and **CI** (lint, tests, dbt parse, Docker builds)
- Honest limitations documented: the label measures a promise (not delivery time), and the static dataset means monitoring is explicitly simulated

### [Customer Churn Prediction](https://github.com/nick-st-coder/churn-customer)
Predict whether a telecom customer will churn, so companies can run targeted retention campaigns instead of spending blindly.

- **LightGBM** with a custom decision threshold (0.36) tuned for the precision–recall trade-off — false negatives are the expensive error here
- Model catches **91% of actual churners**; business scenario shows an estimated **$20.5M net annual savings** on a 1M-customer base
- Full pipeline: EDA → feature engineering (VIF analysis, one-hot encoding) → modeling → **MLflow** tracking → **FastAPI + Gradio** serving → **Docker** (image optimized from 4GB → 2.5GB)
- Includes **unit tests** for the API and inference preprocessing

### [Rossmann Store Sales Forecasting](https://github.com/nick-st-coder/rossmann)
Forecast daily sales for **1,115 Rossmann drugstores** across Germany so managers can plan staffing, deliveries, and promotions ahead of time.

- **XGBoost** trained on engineered pandas features, validated with **chronological date-based CV** (no future leakage)
- Solved the structural-zero problem (closed stores) with a **two-stage model**: regressor on open rows, closed rows predicted as exactly 0
- Removed target leakage (`Customers` feature correlated ~0.90–0.996 with `Sales`)
- **Final RMSLE: 0.116** on held-out test data — the negative train/test gap confirms no overfitting
- Served via **FastAPI + Gradio**, containerized with **Docker**, tracked with **MLflow**

### [Online Retail Customer Segmentation](https://github.com/nick-st-coder/online-resail)
Segment customers of a UK online gift-ware retailer into actionable groups using unsupervised learning, so the business can target retention and marketing where it matters.

- **K-Means (k=3)** chosen via elbow, silhouette, and Davies-Bouldin — cross-checked with **GMM (BIC/AIC)** and an agglomerative dendrogram
- Cleaned **779,423 transactions → 5,878 customers**; engineered 11 behavioral + RFM-style features per customer
- Segments form a clear value ladder: occasional bulk buyers (34%) → everyday value shoppers (43%) → high-volume resellers (23%) who drive 8× the revenue of the middle segment
- Top 10% of customers generate **~64% of total revenue**; ~28% placed only one order
- Honest trade-offs documented: dropped ~25% of rows (missing `Customer ID`), removed 2 "whale" customers, and noted GMM's disagreement on k
- Served via **FastAPI + Gradio**, with **CI** (lint + tests) and `uv` for dependency management

---

## 🛠️ Skills

| Category | Tools |
|---|---|
| **Languages** | Python, SQL |
| **Data & ML** | pandas, NumPy, scikit-learn, LightGBM, XGBoost, Optuna, SHAP, matplotlib, seaborn |
| **Data Engineering** | dbt, PostgreSQL, BigQuery, Airflow, Pandera |
| **MLOps** | MLflow, Evidently, Docker, GitHub Actions |
| **Backend / Serving** | FastAPI, Gradio, Streamlit |
| **BI** | Power BI, Power Query, DAX |
| **Tooling** | Git, uv, ruff, Jupyter |

---

## 📫 Let's Connect

- [LinkedIn](https://www.linkedin.com/in/nikita-babukh-3a47a33a9/) · [Portfolio](https://your-portfolio.com) · [Email](babukhnikita@gmail.com)