# import frappe

# @frappe.whitelist()
# def download_file(product_id):
#     file_url = frappe.db.get_value("Digital Product", product_id, "file")
#     if file_url:
#         return file_url
#     return None


# import frappe
# import os

# @frappe.whitelist()
# def download_file(product_id):
#     file_url = frappe.db.get_value("Digital Product", product_id, "file")
#     if not file_url:
#         frappe.throw("No file found for this product")

#     file_doc = frappe.get_doc("File", {"file_url": file_url})
#     file_path = file_doc.get_full_path()

#     if not os.path.exists(file_path):
#         frappe.throw("File not found on server")

#     # Set response headers to force download
#     frappe.local.response.filename = file_doc.file_name
#     frappe.local.response.filecontent = open(file_path, "rb").read()
#     frappe.local.response.type = "download"


# @frappe.whitelist()
# def mark_payment_success(docname, razorpay_payment_id):
#     doc = frappe.get_doc("Buyer Payment", docname)
#     doc.payment_status = "Paid"
#     doc.razorpay_payment_id = razorpay_payment_id
#     doc.save(ignore_permissions=True)
#     frappe.db.commit()
#     return {"status": "success"}

# import frappe
# from frappe.utils import now

# def record_purchase(doc, method):
#     """Triggered automatically when Buyer Payment is submitted"""
#     product_id = doc.product_id
#     payment_id = doc.name  # or doc.payment_id if you have a field

#     product = frappe.get_doc("Digital Product", product_id)

#     # assume Digital Product has a 'creator' link field
#     creator = product.creator if hasattr(product, "creator") else None

#     purchase = frappe.get_doc({
#         "doctype": "Purchase History",
#         "user": doc.owner,   # the buyer
#         "product": product.name,
#         "creator": creator,
#         "price": product.price,
#         "payment_id": payment_id,
#         "purchase_date": now()
#     })
#     purchase.insert(ignore_permissions=True)
#     frappe.db.commit()





