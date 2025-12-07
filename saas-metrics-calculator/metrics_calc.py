
import argparse
import sys

def calculate_ltv(arpu, churn_rate):
    if churn_rate == 0:
        return float('inf')
    return arpu / churn_rate

def calculate_cac(marketing_spend, sales_spend, new_customers):
    if new_customers == 0:
        return 0
    return (marketing_spend + sales_spend) / new_customers

def calculate_arr(mrr):
    return mrr * 12

def calculate_nrr(starting_mrr, expansion_mrr, contraction_mrr, churned_mrr):
    if starting_mrr == 0:
        return 0
    return ((starting_mrr + expansion_mrr - contraction_mrr - churned_mrr) / starting_mrr) * 100

def main():
    parser = argparse.ArgumentParser(description="Calculate BtoB SaaS Metrics")
    subparsers = parser.add_subparsers(dest="command", help="Metric to calculate")

    # LTV
    ltv_parser = subparsers.add_parser("ltv", help="Calculate Lifetime Value")
    ltv_parser.add_argument("--arpu", type=float, required=True, help="Average Revenue Per User (monthly)")
    ltv_parser.add_argument("--churn", type=float, required=True, help="Monthly Churn Rate (0.05 for 5%)")

    # CAC
    cac_parser = subparsers.add_parser("cac", help="Calculate Customer Acquisition Cost")
    cac_parser.add_argument("--marketing", type=float, required=True, help="Total Marketing Spend")
    cac_parser.add_argument("--sales", type=float, required=True, help="Total Sales Spend")
    cac_parser.add_argument("--new_customers", type=int, required=True, help="Number of New Customers Acquired")

    # ARR
    arr_parser = subparsers.add_parser("arr", help="Calculate Annual Recurring Revenue")
    arr_parser.add_argument("--mrr", type=float, required=True, help="Monthly Recurring Revenue Key Performance Indicator")

    # NRR
    nrr_parser = subparsers.add_parser("nrr", help="Calculate Net Revenue Retention")
    nrr_parser.add_argument("--start_mrr", type=float, required=True, help="MRR at start of period")
    nrr_parser.add_argument("--expansion", type=float, default=0, help="Expansion MRR (upsells/cross-sells)")
    nrr_parser.add_argument("--contraction", type=float, default=0, help="Contraction MRR (downgrades)")
    nrr_parser.add_argument("--churned", type=float, default=0, help="Churned MRR")

    args = parser.parse_args()

    if args.command == "ltv":
        result = calculate_ltv(args.arpu, args.churn)
        print(f"LTV: ${result:.2f}")
    elif args.command == "cac":
        result = calculate_cac(args.marketing, args.sales, args.new_customers)
        print(f"CAC: ${result:.2f}")
    elif args.command == "arr":
        result = calculate_arr(args.mrr)
        print(f"ARR: ${result:.2f}")
    elif args.command == "nrr":
        result = calculate_nrr(args.start_mrr, args.expansion, args.contraction, args.churned)
        print(f"NRR: {result:.2f}%")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
