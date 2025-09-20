import frappe

def get_context(context):
    product_id = frappe.form_dict.name
    if not product_id:
        frappe.throw("Product ID not provided")
    product = frappe.get_doc("Digital Product", product_id)
    creator_logo = None
    if product.creator:
        creator = frappe.get_doc("Creator Profile", product.creator)
        creator_logo = creator.logo

    context.doc = product
    context.creator_logo = creator_logo
    return context



