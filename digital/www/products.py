# import frappe

# def get_context(context):
#     context.products = frappe.get_all(
#         "Digital Product",
#         filters={"docstatus": 1},
#         fields=["name", "title", "price", "preview_image", "creator","category","download_count"]
#     )
#     creators = frappe.get_all("Creator Profile", fields=["name", "logo"])
#     context.creator_logos = {c.name: c.logo for c in creators}

#     return context


import frappe

def get_context(context):
    context.products = frappe.get_all(
        "Digital Product",
        filters={"docstatus": 1}, 
        fields=["name", "title", "price", "preview_image", "creator", "status", "category", "tags"]
    )
    context.categories = [row.category for row in frappe.get_all(
        "Digital Product",
        filters={"docstatus": 1},
        fields=["category"],
        distinct=True
    ) if row.category]
    creators = frappe.get_all("Creator Profile", fields=["name", "logo"])
    context.creator_logos = {c["name"]: c["logo"] for c in creators}

    return context
