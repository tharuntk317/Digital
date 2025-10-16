import frappe

def get_context(context):
    product_id = frappe.form_dict.name or frappe.throw("Product ID not provided")
    product = frappe.get_doc("Digital Product", product_id)

    creator_logo = display_name = None
    if product.creator:
        creator = frappe.get_doc("Creator Profile", product.creator)
        creator_logo, display_name = creator.logo, creator.display_name

    context.update({
        "doc": product,
        "creator_logo": creator_logo,
        "display_name": display_name
    })
    return context





# import frappe

# def get_context(context):
#     product_id = frappe.form_dict.name
#     if not product_id:
#         frappe.throw("Product ID not provided")
#     product = frappe.get_doc("Digital Product", product_id)
#     creator_logo = None
#     if product.creator:
#         creator = frappe.get_doc("Creator Profile", product.creator)
#         creator_logo = creator.logo
#         display_name = creator.display_name

#     context.doc = product
#     context.creator_logo = creator_logo
#     return context



