import frappe
from datetime import datetime, timedelta
from collections import defaultdict

def get_context(context):
    start_date = datetime.now() - timedelta(days=30)

    payments = frappe.get_all(
        "Buyer Payment",
        fields=["product_price", "creation"],
        filters={"creation": [">=", start_date]},
        order_by="creation asc"
    )
    daily_totals = defaultdict(float)
    for p in payments:
        daily_totals[p["creation"].strftime("%Y-%m-%d")] += float(p["product_price"])
    sorted_dates = sorted(daily_totals)
    context.chart_data = {
        "labels": sorted_dates,
        "datasets": [daily_totals[d] for d in sorted_dates]
    }
    return context
