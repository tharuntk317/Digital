import frappe
def get_context(context):
    product_id = frappe.local.request.args.get("product_id") if frappe.local.request else None
    context.product_id = product_id
