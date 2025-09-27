def get_context(context):
    product_id = frappe.local.request.args.get("product_id")
    context.product_id = product_id
    context.user = frappe.session.user

    if not product_id:
        context.error_message = "Product ID is missing. Cannot download."
        return

