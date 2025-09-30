import frappe
from frappe.model.document import Document
from frappe.utils import get_url
import os

class DownloadPage(Document):
    def after_insert(self):
        try:
            product = getattr(self, "product_id", None)
            if product:
                count = frappe.get_value("Digital Product", product, "download_count") or 0
                frappe.db.set_value("Digital Product", product, "download_count", count + 1)
        except Exception as e:
            frappe.log_error(f"Failed to increment download_count for product {product}: {e}", "DownloadPage")

        if not self.product_id:
            return
        try:
            product_doc = frappe.get_doc("Digital Product", self.product_id)
            user_email = frappe.db.get_value("Buyer Profile", self.user_name, "email")
            if not user_email:
                frappe.log_error(f"No email for {self.user_name}", "DownloadPage Email Error")
                return

            attachments = []

            purchase = frappe.get_all(
                "Purchase History",
                filters={"user": self.user_name, "product": self.product_id},
                fields=["name"],
                limit=1
            )

            if purchase:
                pdf = frappe.get_print(
                    "Purchase History",
                    purchase[0].name,
                    print_format="Purchase History PDF",
                    as_pdf=True
                )
                attachments.append({
                    "fname": f"Purchase_{purchase[0].name}.pdf",
                    "fcontent": pdf
                })

            link = get_url(f"/download/{self.name}")
            template = frappe.get_doc("Email Template", "Purchase Detail with Download File")
            message = frappe.render_template(
                template.response_html,
                {"user_name": self.user_name, "product_name": product_doc.name, "download_link": link}
            )

            frappe.sendmail(
                recipients=user_email,
                subject=f"Your purchase of {product_doc.name} is ready",
                message=message,
                attachments=attachments,
                reference_doctype=self.doctype,
                reference_name=self.name,
                now=True
            )

        except Exception as e:
            frappe.log_error(f"Error sending download email for {self.name}: {e}", "DownloadPage Error")



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
    frappe.local.response.filename = file_doc.file_name
    with open(file_path, "rb") as f:
        frappe.local.response.filecontent = f.read()
    frappe.local.response.type = "download"

