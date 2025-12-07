---
name: saas-metrics-calculator
description: Calculate key BtoB SaaS metrics like LTV, CAC, ARR, and NRR using a Python script. Use this when the user asks to compute business health metrics or analyze unit economics.
---

# SaaS Metrics Calculator

This skill helps calculate essential BtoB SaaS metrics to evaluate product interaction and business health.

## Usage

Use the `metrics_calc.py` script to perform calculations.

### Commands

1.  **LTV (Lifetime Value)**
    ```bash
    python metrics_calc.py ltv --arpu <ARPU> --churn <CHURN_RATE_DECIMAL>
    ```
    *   `--arpu`: Average Revenue Per User (monthly)
    *   `--churn`: Monthly Churn Rate (e.g., 0.05 for 5%)

2.  **CAC (Customer Acquisition Cost)**
    ```bash
    python metrics_calc.py cac --marketing <MARKETING_SPEND> --sales <SALES_SPEND> --new_customers <COUNT>
    ```

3.  **ARR (Annual Recurring Revenue)**
    ```bash
    python metrics_calc.py arr --mrr <MRR>
    ```

4.  **NRR (Net Revenue Retention)**
    ```bash
    python metrics_calc.py nrr --start_mrr <START_MRR> --expansion <EXPANSION_MRR> --contraction <CONTRACTION_MRR> --churned <CHURNED_MRR>
    ```

## Examples

**Calculate LTV for ARPU $100 and 5% Churn:**
```bash
python metrics_calc.py ltv --arpu 100 --churn 0.05
```

**Calculate CAC with $5000 marketing, $3000 sales, and 10 new customers:**
```bash
python metrics_calc.py cac --marketing 5000 --sales 3000 --new_customers 10
```
