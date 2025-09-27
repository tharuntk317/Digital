import frappe
from frappe.model.document import Document
from frappe.utils import now

class BuyerPayment(Document):
    def after_insert(self):
        try:
            user = getattr(self, "user_name", None)
            product = getattr(self, "product_id", None)
            price = getattr(self, "product_price", 0)
            payment_id = getattr(self, "payment_id", None)

            try:
                price = float(price)
            except (TypeError, ValueError):
                price = 0

            if not user or not product:
                frappe.log_error(f"Missing user or product in Buyer Payment: {self.name}", "BuyerPayment")
                return

            frappe.get_doc({
                "doctype": "Purchase History",
                "user": user,
                "product": product,
                "price": price,
                "payment_id": payment_id,
                "purchase_date": now()
            }).insert(ignore_permissions=True)

            frappe.get_doc({
                "doctype": "Download Page",
                "user_name": user,
                "product_id": product,
                "product_price": price
            }).insert(ignore_permissions=True)

            creator_name = frappe.get_value("Digital Product", product, "creator")
            if creator_name:
                try:
                    creator_doc = frappe.get_doc("Creator Profile", creator_name)
                    if not creator_doc.wallet:
                        creator_doc.wallet = 0
                    creator_doc.wallet += price
                    creator_doc.save(ignore_permissions=True)
                except Exception as e:
                    frappe.log_error(f"Failed to update creator wallet: {e}", "BuyerPayment")
            else:
                frappe.log_error(f"No creator assigned for product {product}", "BuyerPayment")

            self.db_set("payment_status", "Success", update_modified=False)
            frappe.msgprint("Purchase successful! You can now download your product.", alert=True)

        except Exception as e:
            frappe.log_error(f"Error in Buyer Payment after_insert: {e}", "BuyerPayment")






# import frappe
# from frappe.model.document import Document
# from frappe.utils import now

# class BuyerPayment(Document):
#     def after_insert(self):
#         try:
#             user = getattr(self, "user_name", None)
#             product = getattr(self, "product_id", None)
#             price = getattr(self, "product_price", None)
#             payment_id = getattr(self, "payment_id", None)
#             if not user or not product:
#                 frappe.log_error(f"Missing user or product in Buyer Payment: {self.name}")
#                 return
#             frappe.get_doc({
#                 "doctype": "Purchase History",
#                 "user": user,
#                 "product": product,
#                 "price": price,
#                 "payment_id": payment_id,
#                 "purchase_date": now() 
#             }).insert(ignore_permissions=True)
#             frappe.get_doc({
#                 "doctype": "Download Page",
#                 "user_name": user,
#                 "product_id": product,
#                 "product_price": price
#             }).insert(ignore_permissions=True)
#             self.db_set("payment_status", "Success", update_modified=False)
#             frappe.msgprint(
#                 "Purchase successful! You can now download your product.",
#                 alert=True
#             )
#         except Exception as e:
#             frappe.log_error(f"Error creating related records for Buyer Payment {self.name}: {e}")


