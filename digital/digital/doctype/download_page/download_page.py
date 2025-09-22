import frappe
import os	
from frappe.model.document import Document


class DownloadPage(Document):
	pass

@frappe.whitelist()
def download_file(product_id):
    file_url = frappe.db.get_value("Digital Product", product_id, "file")
    if not file_url:
        frappe.throw("No file found for this product")
    file_doc = frappe.get_doc("File", {"file_url": file_url})
    file_path = file_doc.get_full_path()
    if not os.path.exists(file_path):
        frappe.throw("File not found on server")
    product = frappe.get_doc("Digital Product", product_id)
    current_count = product.download_count or 0
    product.download_count = int(current_count) + 1
    product.save(ignore_permissions=True)
    creator = frappe.get_doc("Creator Profile", product.creator)
    price = float(product.price or 0)
    creator.wallet = float(creator.wallet or 0) + price
    creator.save(ignore_permissions=True)
    frappe.db.commit()
    frappe.local.response.filename = file_doc.file_name
    with open(file_path, "rb") as f:
        frappe.local.response.filecontent = f.read()
    frappe.local.response.type = "download"
