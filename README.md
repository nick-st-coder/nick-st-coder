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

---

## 🛠️ Skills

| Category | Tools |
|---|---|
| **Languages** | Python, SQL |
| **Data & ML** | pandas, NumPy, scikit-learn, LightGBM, XGBoost, matplotlib |
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
