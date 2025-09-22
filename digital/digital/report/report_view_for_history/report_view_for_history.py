# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

# import frappe


# def execute(filters=None):
# 	columns, data = [], []
# 	return columns, data

# import frappe

# def execute(filters=None):
#     columns = [
#         {"label": "User", "fieldname": "user", "fieldtype": "Link", "options": "User", "width": 150},
#         {"label": "Product", "fieldname": "product", "fieldtype": "Data", "width": 180},
#         {"label": "Creator", "fieldname": "creator", "fieldtype": "Data", "width": 150},
#         {"label": "Price", "fieldname": "price", "fieldtype": "Currency", "width": 120},
#         {"label": "Payment ID", "fieldname": "payment_id", "fieldtype": "Data", "width": 180},
#         {"label": "Purchase Date", "fieldname": "purchase_date", "fieldtype": "Datetime", "width": 180}
#     ]
#     conditions = []
#     values = {}

#     if filters.get("user"):
#         conditions.append("user = %(user)s")
#         values["user"] = filters.get("user")

#     if filters.get("product"):
#         conditions.append("product LIKE %(product)s")
#         values["product"] = "%" + filters.get("product") + "%"

#     if filters.get("creator"):
#         conditions.append("creator LIKE %(creator)s")
#         values["creator"] = "%" + filters.get("creator") + "%"

#     if filters.get("payment_id"):
#         conditions.append("payment_id = %(payment_id)s")
#         values["payment_id"] = filters.get("payment_id")

#     if filters.get("from_date"):
#         conditions.append("purchase_date >= %(from_date)s")
#         values["from_date"] = filters.get("from_date")

#     if filters.get("to_date"):
#         conditions.append("purchase_date <= %(to_date)s")
#         values["to_date"] = filters.get("to_date")

#     condition_str = " AND ".join(conditions)
#     if condition_str:
#         condition_str = "WHERE " + condition_str

#     query = f"""
#         SELECT 
#             user,
#             product,
#             creator,
#             price,
#             payment_id,
#             purchase_date
#         FROM `tabPurchase History`
#         {condition_str}
#         ORDER BY purchase_date DESC
#     """

#     data = frappe.db.sql(query, values, as_dict=True)

#     return columns, data

import frappe

def execute(filters=None):
    filters = filters or {}

    # ------------------------
    # Columns for Table
    # ------------------------
    columns = [
        {"label": "User", "fieldname": "user", "fieldtype": "Link", "options": "User", "width": 150},
        {"label": "Product", "fieldname": "product", "fieldtype": "Data", "width": 180},
        {"label": "Creator", "fieldname": "creator", "fieldtype": "Data", "width": 150},
        {"label": "Price", "fieldname": "price", "fieldtype": "Currency", "width": 120},
        {"label": "Payment ID", "fieldname": "payment_id", "fieldtype": "Data", "width": 180},
        {"label": "Purchase Date", "fieldname": "purchase_date", "fieldtype": "Datetime", "width": 180}
    ]

    # ------------------------
    # Build Conditions
    # ------------------------
    conditions = []
    values = {}

    if filters.get("user"):
        conditions.append("user = %(user)s")
        values["user"] = filters.get("user")

    if filters.get("product"):
        conditions.append("product LIKE %(product)s")
        values["product"] = "%" + filters.get("product") + "%"

    if filters.get("creator"):
        conditions.append("creator LIKE %(creator)s")
        values["creator"] = "%" + filters.get("creator") + "%"

    if filters.get("payment_id"):
        conditions.append("payment_id = %(payment_id)s")
        values["payment_id"] = filters.get("payment_id")

    if filters.get("from_date"):
        conditions.append("purchase_date >= %(from_date)s")
        values["from_date"] = filters.get("from_date")

    if filters.get("to_date"):
        conditions.append("purchase_date <= %(to_date)s")
        values["to_date"] = filters.get("to_date")

    condition_str = " AND ".join(conditions)
    if condition_str:
        condition_str = "WHERE " + condition_str

    # ------------------------
    # Fetch Table Data
    # ------------------------
    query = f"""
        SELECT user, product, creator, price, payment_id, purchase_date
        FROM `tabPurchase History`
        {condition_str}
        ORDER BY purchase_date DESC
    """
    data = frappe.db.sql(query, values, as_dict=True)

    # ------------------------
    # Prepare Chart Data (product-wise per day)
    # ------------------------
    chart_data = frappe.db.sql(f"""
        SELECT DATE(purchase_date) as day, product, COUNT(*) as count
        FROM `tabPurchase History`
        {condition_str}
        GROUP BY DATE(purchase_date), product
        ORDER BY day ASC
    """, values, as_dict=True)

    # Organize chart by products
    products = list({d['product'] for d in chart_data})  # unique products
    days = sorted(list({d['day'] for d in chart_data}))
    
    datasets = []
    for product in products:
        values_list = []
        for day in days:
            found = next((d['count'] for d in chart_data if d['day'] == day and d['product'] == product), 0)
            values_list.append(found)
        datasets.append({"name": product, "values": values_list})

    chart = {
        "data": {
            "labels": [d.strftime("%Y-%m-%d") for d in days],
            "datasets": datasets
        },
        "type": "bar",  # or "line"
        "height": 300
    }

    return columns, data, None, chart

