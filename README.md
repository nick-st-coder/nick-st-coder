# Hi, I'm Nick 👋

**Data Science & Machine Learning** — I build end-to-end ML solutions: from exploratory analysis and feature engineering to model training, experiment tracking, and serving models behind real APIs.

I'm currently a computer programming student focused on **Data Science**, and I use GitHub to document projects the way they'd be done in industry — with clean code, honest validation, and measurable business impact.

---

## 🚀 Featured Projects

### [Rossmann Store Sales Forecasting](https://github.com/nick-st-coder/rossmann)
Forecast daily sales for **1,115 Rossmann drugstores** across Germany so managers can plan staffing, deliveries, and promotions ahead of time.

- **XGBoost** trained on engineered pandas features, validated with **chronological date-based CV** (no future leakage)
- Solved the structural-zero problem (closed stores) with a **two-stage model**: regressor on open rows, closed rows predicted as exactly 0
- Removed target leakage (`Customers` feature correlated ~0.90–0.996 with `Sales`)
- **Final RMSLE: 0.116** on held-out test data — the negative train/test gap confirms no overfitting
- Served via **FastAPI + Gradio**, containerized with **Docker**, tracked with **MLflow**

### [Customer Churn Prediction](https://github.com/nick-st-coder/churn-customer)
Predict whether a telecom customer will churn, so companies can run targeted retention campaigns instead of spending blindly.

- **LightGBM** with a custom decision threshold (0.36) tuned for the precision–recall trade-off — false negatives are the expensive error here
- Model catches **91% of actual churners**; business scenario shows an estimated **$20.5M net annual savings** on a 1M-customer base
- Full pipeline: EDA → feature engineering (VIF analysis, one-hot encoding) → modeling → **MLflow** tracking → **FastAPI + Gradio** serving → **Docker** (image optimized from 4GB → 2.5GB)
- Includes **unit tests** for the API and inference preprocessing

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
| **Data & ML** | pandas, NumPy, scikit-learn, LightGBM, XGBoost, matplotlib, seaborn |
| **MLOps** | MLflow, Docker |
| **Backend / Serving** | FastAPI, Gradio |
| **Tooling** | Git, uv, Jupyter |

---

## 📚 Currently

- Building ML projects end-to-end and improving my ML engineering skills
- Focused on writing production-quality code: testing, reproducibility, and clean project structure

---

## 📫 Let's Connect

- [LinkedIn](https://www.linkedin.com/in/nikita-babukh-3a47a33a9/) · [Portfolio](https://your-portfolio.com) · [Email](babukhnikita@gmail.com)

---

![GitHub stats](https://github-readme-stats.vercel.app/api?username=nick-st-coder&show_icons=true)
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=nick-st-coder&layout=compact)
