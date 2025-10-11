# import frappe
# from frappe.model.document import Document
# from frappe.utils import get_url
# import os


# class DownloadPage(Document):
#     def after_insert(self):
#         try:
#             product = getattr(self, "product_id", None)
#             if product:
#                 count = frappe.get_value("Digital Product", product, "download_count") or 0
#                 frappe.db.set_value("Digital Product", product, "download_count", count + 1)
#         except Exception as e:
#             frappe.log_error(f"Failed to increment download_count for product {product}: {e}", "DownloadPage")

#         if not self.product_id:
#             return
#         try:
#             product_doc = frappe.get_doc("Digital Product", self.product_id)
#             user_email = frappe.db.get_value("Buyer Profile", self.user_name, "email")
#             if not user_email:
#                 frappe.log_error(f"No email for {self.user_name}", "DownloadPage Email Error")
#                 return

#             attachments = []

#             purchase = frappe.get_all(
#                 "Purchase History",
#                 filters={"user": self.user_name, "product": self.product_id},
#                 fields=["name"],
#                 limit=1
#             )

#             if purchase:
#                 pdf = frappe.get_print(
#                     "Purchase History",
#                     purchase[0].name,
#                     print_format="Purchase History PDF",
#                     as_pdf=True
#                 )
#                 attachments.append({
#                     "fname": f"Purchase_{purchase[0].name}.pdf",
#                     "fcontent": pdf
#                 })

#             link = get_url(f"/download/{self.name}")
#             template = frappe.get_doc("Email Template", "Purchase Detail with Download File")
#             message = frappe.render_template(
#                 template.response_html,
#                 {"user_name": self.user_name, "product_name": product_doc.name, "download_link": link}
#             )

#             frappe.sendmail(
#                 recipients=user_email,
#                 subject=f"Your purchase of {product_doc.name} is ready",
#                 message=message,
#                 attachments=attachments,
#                 reference_doctype=self.doctype,
#                 reference_name=self.name,
#                 now=True
#             )

#         except Exception as e:
#             frappe.log_error(f"Error sending download email for {self.name}: {e}", "DownloadPage Error")



# @frappe.whitelist()
# def download_file(product_id):
#     product = frappe.get_doc("Digital Product", product_id)
#     if not product.file:
#         frappe.throw(_("No file found for this product"))
#     file_doc = frappe.get_doc("File", {"file_url": product.file})
#     file_path = file_doc.get_full_path()
#     if not os.path.exists(file_path):
#         frappe.throw(_("File not found on server"))
#     frappe.local.response.filename = file_doc.file_name
#     frappe.local.response.filecontent = open(file_path, "rb").read()
#     frappe.local.response.type = "download"

# @frappe.whitelist()
# def download_file(product_id):
#     f = frappe.get_doc("File", {"file_url": frappe.get_value("Digital Product", product_id, "file")})
#     if not f or not os.path.exists(f.get_full_path()): frappe.throw(_("File not found"))
#     frappe.local.respon se.filename, frappe.local.response.filecontent, frappe.local.response.type = f.file_name, open(f.get_full_path(), "rb").read(), "download"

# import frappe
# from frappe.model.document import Document
# from frappe.utils import get_url
# import os


# class DownloadPage(Document):
#     def after_insert(self):
#         try:
#             product = getattr(self, "product_id", None)
#             if product:
#                 count = frappe.get_value("Digital Product", product, "download_count") or 0
#                 frappe.db.set_value("Digital Product", product, "download_count", count + 1)
#         except Exception as e:
#             frappe.log_error(f"Failed to increment download_count for product {product}: {e}", "DownloadPage")

#         if not self.product_id:
#             return
#         try:
#             product_doc = frappe.get_doc("Digital Product", self.product_id)
#             user_email = frappe.db.get_value("Buyer Profile", self.user_name, "email")
#             if not user_email:
#                 frappe.log_error(f"No email for {self.user_name}", "DownloadPage Email Error")
#                 return

#             attachments = [p]

#             purchase = frappe.get_all(
#                 "Purchase History",
#                 filters={"user": self.user_name, "product": self.product_id},
#                 fields=["name"],
#                 limit=1
#             )

#             if purchase:
#                 pdf = frappe.get_print(
#                     "Purchase History",
#                     purchase[0].name,
#                     print_format="Purchase History PDF",
#                     as_pdf=True
#                 )
#                 attachments.append({
#                     "fname": f"Purchase_{purchase[0].name}.pdf",
#                     "fcontent": pdf,
#                 }),

#             link = get_url(f"/download/{self.name}")
#             p =  product_doc.file
#             template = frappe.get_doc("Email Template", "Purchase Detail with Download File")
#             message = frappe.render_template(
#                 template.response_html,
#                 {"user_name": self.user_name, "product_name": product_doc.name, "download_link": link}
#             )

#             frappe.sendmail(
#                 recipients=user_email,
#                 subject=f"Your purchase of {product_doc.name} is ready",
#                 message=message,
#                 attachments=attachments,
#                 reference_doctype=self.doctype,
#                 reference_name=self.name,
#                 now=True
#             )

#         except Exception as e:
#             frappe.log_error(f"Error sending download email for {self.name}: {e}", "DownloadPage Error")




# ===========================================================================================================
import frappe
from frappe.model.document import Document
from frappe.utils import get_url

class DownloadPage(Document):
    def after_insert(self):
        if not self.product_id:
            return

        try:
            # Increment download count
            count = frappe.get_value("Digital Product", self.product_id, "download_count") or 0
            frappe.db.set_value("Digital Product", self.product_id, "download_count", count + 1)

            product_doc = frappe.get_doc("Digital Product", self.product_id)
            user_email = frappe.db.get_value("Buyer Profile", self.user_name, "email")
            if not user_email:
                frappe.log_error(f"No email for {self.user_name}", "DownloadPage Email Error")
                return

            attachments = []

            # Attach Purchase History PDF
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

            # Attach the product file from the file field
            if product_doc.file:
                file_doc = frappe.get_doc("File", {"file_url": product_doc.file})
                file_content = file_doc.get_content()
                
                attachments.append({
                    "fname": file_doc.file_name,
                    "fcontent": file_content
                })

            # Generate download/view link for the product file (optional - for email body)
            file_link = get_url(product_doc.file)

            # Render email template
            template = frappe.get_doc("Email Template", "Purchase Detail with Download File")
            message = frappe.render_template(
                template.response_html,
                {
                    "user_name": self.user_name,
                    "product_name": product_doc.name,
                    "download_link": file_link
                }
            )

            # Send email with attachments
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


