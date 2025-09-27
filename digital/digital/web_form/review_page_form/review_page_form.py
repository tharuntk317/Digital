import frappe
def get_context(context):
    product_id = frappe.local.request.args.get("product_id") if frappe.local.request else None
    context.user = frappe.session.user
    if not product_id:
        context.error_message = "Product ID is missing. Cannot review."
        return
    try:
        context.product = frappe.get_doc("Digital Product", product_id)
        context.product_id = product_id  
    except frappe.DoesNotExistError:
        context.error_message = "Product not found."
