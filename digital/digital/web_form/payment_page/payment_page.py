import frappe

def get_context(context):
    product_id = frappe.local.request.args.get("product_id") if frappe.local.request else None
    try:
        context.product = frappe.get_doc("Digital Product", product_id)
    except frappe.DoesNotExistError:
        context.error_message = "Product not found."
