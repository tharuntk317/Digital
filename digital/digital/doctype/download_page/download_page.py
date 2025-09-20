# Copyright (c) 2025, tharun and contributors
# For license information, please see license.txt

import frappe	
from frappe.model.document import Document


class DownloadPage(Document):
	pass

import os

@frappe.whitelist()
def download_file(product_id):
    # Get the file URL linked to the product
    file_url = frappe.db.get_value("Digital Product", product_id, "file")
    if not file_url:
        frappe.throw("No file found for this product")

    # Fetch the File document
    file_doc = frappe.get_doc("File", {"file_url": file_url})
    file_path = file_doc.get_full_path()

    if not os.path.exists(file_path):
        frappe.throw("File not found on server")

    # Return file as downloadable response
    frappe.local.response.filename = file_doc.file_name
    with open(file_path, "rb") as f:
        frappe.local.response.filecontent = f.read()
    frappe.local.response.type = "download"
