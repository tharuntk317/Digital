import frappe
from datetime import datetime, timedelta
from collections import defaultdict

def get_context(context):
    start_date = datetime.now() - timedelta(days=30)

    payments = frappe.get_all(
        "Buyer Payment",
        fields=["product_price", "payment_time_and_data"],
        filters={"payment_time_and_data": [">=", start_date]},
        order_by="creation asc"
    )

    daily_totals = defaultdict(float)
    for p in payments:
        payment_date = p["payment_time_and_data"].strftime("%Y-%m-%d")
        daily_totals[payment_date] += float(p.get("product_price") or 0)

    sorted_dates = sorted(daily_totals)
    context.chart_data = {
        "labels": sorted_dates,
        "datasets": [daily_totals[d] for d in sorted_dates]
    }

    return context
