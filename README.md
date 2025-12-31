# Explainable AI – Credit Card Default Prediction

This repository presents an end-to-end **Explainable Artificial Intelligence (XAI)** case study focused on **credit card default prediction** using tabular financial data. The objective of the project is not only to achieve reasonable predictive performance, but to critically analyze, validate, and *act upon* model explanations in a realistic and high-stakes decision-making context.

---

## Problem Overview

The task is a **binary classification problem**: predicting whether a credit card client will default on their payment in the following month based on demographic information, credit limits, billing history, and repayment behavior over the previous six months. This scenario is particularly suitable for XAI, as credit risk models require transparency, robustness, and careful interpretation.

---

## Dataset

The project uses the **Default of Credit Card Clients Dataset**, publicly available on Kaggle. Each observation corresponds to a client and includes 25 variables covering:

- Demographic attributes (age, gender, education, marital status),
- Financial information (credit limit, bill amounts, payment amounts),
- Repayment status indicators over six months,
- A binary default outcome for the following month.

This dataset is widely used in credit risk research and provides a realistic benchmark for explainability analysis.

**Dataset source:**  
https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

---

## Model and Evaluation

A **Random Forest classifier** is used as the main predictive model. Rather than focusing on extensive hyperparameter tuning, the project builds on an existing baseline model to keep the emphasis on explainability and model understanding.

Model performance is evaluated using:
- Accuracy and confusion matrices for error analysis,
- **ROC-AUC**, which is emphasized due to class imbalance and the asymmetric costs typical in credit risk problems.

---

## Explainability Methods

Multiple complementary XAI techniques are applied:

- **Permutation Importance (ROC-AUC–based)** for global, performance-driven explanations,
- **SHAP** for both global (summary plots) and local (instance-level) explanations,
- **LIME** for local, human-readable explanations,
- **Sanity checks**, including drop-column tests and label randomization, to assess the faithfulness and stability of explanations.

The agreement and disagreement between these methods are critically analyzed to highlight their strengths and limitations.

---

## Actionable Use of XAI

Explainability is used as an **actionable tool** rather than a purely descriptive one. Global explanations and correlation analysis reveal redundancy and excessive reliance on short-term repayment indicators. Guided by these insights, new aggregated repayment features are introduced (mean, maximum delay, trend, and weighted moving average) to better capture long-term behavior.

Features with negative or negligible contribution, identified through permutation importance, are removed. The resulting model is more compact, interpretable, and stable, while maintaining comparable predictive performance.

---

## Baseline Reference

The initial modeling approach was inspired by the following Kaggle notebook, which served as a starting point for data exploration and baseline modeling:

G. Preda, *Default of Credit Card Clients – Predictive Models*, Kaggle Notebook  
https://www.kaggle.com/code/gpreda/default-of-credit-card-clients-predictive-models#Check-the-data

---

## Repository Structure

├── notebooks/ # Jupyter notebooks with experiments and analysis

├── src/ # Helper functions and utilities

├── report/ # Final report (PDF / DOCX)

├── requirements.txt # Python dependencies

└── README.md

## Reproducibility / How to Run

The project can be reproduced locally by following the steps below. The workflow consists of creating a virtual environment, installing dependencies, running the preprocessing script, and then exploring the notebooks.

```bash
# 1. Create virtual environment
python -m venv .venv

# 2. Activate virtual environment
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Run data preprocessing
cd src
python data_preprocessing.py

# 5. Explore and run notebooks